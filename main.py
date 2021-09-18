from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.animation import Animation
#from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivymd.uix.list import OneLineListItem
from kivymd.uix.snackbar import Snackbar
from functools import partial
from kivy.config import Config
from manager import KV
import requests

sound = SoundLoader.load('intro.mp3')
if sound:
    sound.play()


# Window.size = (350, 600)

Config.set('kivy', 'keyboard_mode', 'systemanddock')

def berechnung_func(fd):
    if fd != None and '-' in fd:
        zl = fd.split('-')
        fdt = (280 / ((int(zl[1]) + 50) / int(zl[0]))) * 1000
    else:
        fdt = 0
        snackbar = Snackbar(text="fdt ist nicht korrekt eingegeben. Form für eingeben 6-1000")
        snackbar.open()
    return fdt


url1 = 'https://trainingapp-89911.firebaseio.com/Elstar.json'
url2 = 'https://trainingapp-89911.firebaseio.com/Red%20Prince.json'
url3 = 'https://trainingapp-89911.firebaseio.com/Breaburn.json'
url4 = 'https://trainingapp-89911.firebaseio.com/Boskoop.json'
url5 = 'https://trainingapp-89911.firebaseio.com/Gala.json'
url6 = 'https://trainingapp-89911.firebaseio.com/Holsteiner%20Cox.json'
url7 = 'https://trainingapp-89911.firebaseio.com/Kanzi.json'
url8 = 'https://trainingapp-89911.firebaseio.com/Jonagored.json'

g_list = {'Elstar': url1, 'Red Prince': url2, 'Breaburn': url3, 'Boskoop': url4, 'Gala': url5,
          'Holsteiner Cox': url6, 'Kanzi': url7, 'Jonagored': url8}



class MyApp(MDApp):
    g_list = {'Elstar': url1, 'Red Prince': url2, 'Breaburn': url3, 'Boskoop': url4, 'Gala': url5,
              'Holsteiner Cox': url6, 'Kanzi': url7, 'Jonagored': url8}

    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'
        scr = Builder.load_string(KV)
        return scr

    def on_start(self):
        self.anim_label()
        self.anim_lab()

    def anim_label(self, *args):
        widget = self.root.ids.menulabel1
        anim = Animation(x_hint=.55, duration=2)
        anim.start(widget)

    def anim_lab(self, *args):
        widget = self.root.ids.menulabel2
        anim = Animation(y_hint=.6, duration=2)
        anim.start(widget)

    def get_list(self, sorte,  *args):
        if self.root.ids.sorte.text in g_list:
            to_find = self.root.ids.sorte.text
            self.root.ids.s_name.text = to_find
            if self.root.ids.s_name.text == to_find:
                a = requests.get(g_list[to_find]).json()
                my_list = self.root.ids.container.children
                if len(my_list) == 0:
                    for i in a:
                        if i == None:
                            continue
                        self.root.ids.container.add_widget(OneLineListItem(text=f'{i}', on_release=self.delete_me))
        else:
            self.root.ids.s_name.text = 'Fdt'



    def get_new_statistik(self, infa, *args):
        name = self.root.ids.s_name.text
        result = requests.get(self.g_list[name]).json()
        to_firebase = self.root.ids.infa.text
        data = {len(result): to_firebase}
        requests.patch(self.g_list[name], json=data)
        self.root.ids.container.add_widget(OneLineListItem(text=to_firebase))


    def clear_widg(self):
        self.root.ids.container.clear_widgets()



    def delete_me(self, instance):
        but = MDFlatButton(text='ja', on_release=partial(self.remove_infa, instance))
        but1 = MDFlatButton(text='nein', on_release=self.my_callback)
        self.dialog = MDDialog(
            title="Loschen?",  size_hint_x=0.75,
            radius=[20, 7, 20, 7], buttons=[but, but1], auto_dismiss=False)
        self.dialog.open()

    def remove_infa(self,list_item_instance, instance):
        nahme = self.root.ids.s_name.text
        res = requests.get(self.g_list[nahme]).json()
        url = self.g_list[nahme]
        for i in enumerate(res):
            if list_item_instance.text == i[1]:
                dat = url.replace('.json',f'/{i[0]}.json')
                break

        self.root.ids.container.remove_widget(list_item_instance)
        requests.delete(dat)
        self.dialog.dismiss()
        self.root.current = 'statistik'

    def my_callback(self, instance):
        self.dialog.dismiss()


    def change_text(self):
        f = self.root.ids.text_input.text
        apfel_z = int(berechnung_func(f))
        self.root.ids.label_o.text = '-- ' + str(apfel_z) + ' --'
        self.root.ids.label_l.text = str(apfel_z-40) + ' -'
        self.root.ids.label_h.text = '- ' + str(apfel_z+30)




MyApp().run()