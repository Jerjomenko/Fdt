
KV = '''
ScreenManager:  


    Screen:
        name: 'start'
        FloatLayout:
            canvas:
                Color:
                    rgba: app.theme_cls.primary_color
                Rectangle:
                    source: 'schadow.jpg'
                    size: self.size
                    pos: self.pos
            MDLabel:
                id: menulabel1
                x_hint: 1.5
                pos_hint:{'center_x': self.x_hint, 'center_y': .7}
                text: 'Fdt'
                font_style: 'H1'

            MDLabel:
                id: menulabel2
                y_hint: .1
                pos_hint:{'center_x':.55, 'center_y': self.y_hint}
                text: 'Elbe-Obst Sortierung'
                font_style: 'H5'

            MDRaisedButton:
                text: 'Berechnung'
                font_style: 'Body2'
                pos_hint:{'center_x':.75, 'center_y': .1}
                size_hint: (.3, .05)
                elevation:10
                on_release: root.current = 'berechnung'

            MDRaisedButton:
                text: 'Statistik'
                font_style: 'Body2'
                pos_hint:{'center_x':.75, 'center_y': .04}
                size_hint: (.3, .05)
                elevation:10
                on_release: root.current = 'statistik'


    Screen:
        name: 'statistik'
        FloatLayout:
            canvas:
                Color:
                    rgba: 54/255, 176/255, 166/255, .52
                Rectangle:
                    source: 'schadow.jpg'
                    size: self.size
                    pos: self.pos

            MDLabel:
                text: "Statistik"
                font_style: 'H3'
                pos_hint: {'center_x': .5, 'center_y': .7}
                halign: "center"

            MDTextField:
                id: sorte
                hint_text: 'sorte eintragen'
                current_hint_text_color: 0, 1, 0, 1
                pos_hint: {'center_x': .5, 'center_y': .5}
                size_hint: .8, None
                mode: 'fill'
                fill_color: 0, 0, 0, .1

            MDRoundFlatButton:
                id: button
                pos_hint: {'center_x': .5, 'center_y': .35}
                size_hint: .8, .09
                canvas:
                    Color:
                        rgba: (0.45, 0.45, 0.65, 0.30)
                    RoundedRectangle:
                        source: 'schadow.jpg'
                        size: self.size
                        pos: self.pos
                        radius:[20]
                text: 'Zum List'
                text_color: 0, 0, 0, 1
                md_bg_color: app.theme_cls.primary_color
                on_press: 
                    root.current = 'list'
                    app.get_list(sorte.text)
                    
            MDFloatingActionButton:
                icon: "arrow-left-thick"
                md_bg_color: 0.5, 0.5, 1, 1
                pos_hint: {'center_x': .14, 'center_y': .1}
                elevation: 12
                on_press: root.current = 'berechnung'
                
            MDFloatingActionButton:
                icon: "home"
                md_bg_color: 0.5, 0.5, 1, 1
                pos_hint: {'center_x': .87, 'center_y': .1}
                elevation: 12
                on_press: root.current = 'start'



    Screen:
        name: 'berechnung'
        FloatLayout:
            canvas:
                Color:
                    rgba: 160/255, 225/255, 1, .69
                Rectangle:
                    source: 'schadow.jpg'
                    size: self.size
                    pos: self.pos

            MDLabel:
                id: errorl
                text: 'Berechnung'
                font_style: 'H3'
                pos_hint: {'top': 1.3}
                halign: 'center'

            MDTextField:
                id: text_input
                hint_text: 'Fdt eingeben'
                helper_text: "Form fürs eingeben zum beispiel 6-1000"
                helper_text_mode: "on_focus"
                size_hint: .8, .1
                pos_hint: {'center_x': .5, 'top': .7}
                mode: 'rectangle'

            GridLayout:
                cols: 3
                pos_hint: {'top': .9}
                MDLabel:
                    id: label_l
                    text: 'min'
                    halign: 'center'
                    font_style: 'H6'

                MDLabel:
                    id: label_o
                    text: 'value'
                    halign: 'center'
                    font_style: 'H5'

                MDLabel:
                    id: label_h
                    text: 'max'
                    halign: 'center'
                    font_style: 'H6'

            BoxLayout:
                orientation: 'vertical'
                padding: [0, 0, 0, 60]
                spacing: 8
                MDRoundFlatButton:
                    pos_hint: {'center_x': .5, 'center_y': .65}
                    size_hint_x: .6
                    canvas:
                        Color:
                            rgba: (87/255, 46/255, 92/255, .68)
                        RoundedRectangle:
                            source: 'schadow.jpg'
                            size: self.size
                            pos: self.pos
                            radius: [20]
                    text: 'Go'
                    text_color: 0, 0, 0, 1
                    on_press: app.change_text()

                MDRoundFlatButton:
                    pos_hint: {'center_x': .5, 'center_y': .3}
                    size_hint_x: .6
                    canvas:
                        Color:
                            rgba: (230/255, 74/255, 65/255, .68)
                        RoundedRectangle:
                            source: 'schadow.jpg'
                            size: self.size
                            pos: self.pos
                            radius: [20]                           
                    text: 'Statistik'
                    text_color: 0, 0, 0, 1
                    on_press: root.current = 'statistik'

                MDRoundFlatButton:
                    pos_hint: {'center_x': .5, 'center_y': .15}
                    size_hint_x: .6
                    canvas:
                        Color:
                            rgba: (58/255, 77/255, 67/255, .68)
                        RoundedRectangle:
                            source: 'schadow.jpg'
                            size: self.size
                            pos: self.pos
                            radius: [20]  
                    text: 'Zurück'
                    text_color: 0, 0, 0, 1
                    on_press: root.current = 'start'



    Screen:
        name: 'list'
        canvas:
            Color:
                rgba: (61/255, 144/255, 116/255, 1)
            RoundedRectangle:
                pos: self.pos
                size: self.size
        on_leave: app.clear_widg()

        FloatLayout:
            MDLabel:
                id: s_name
                pos_hint: {'top': 1}
                size_hint: 1, .15
                text: 'Fdt'
                halign: 'center'
                font_style: 'H3'
                
            ScrollView:
                do_scroll_y: True
                do_scroll_x: False
                size_hint: .9, .8
                pos_hint: {"center_x": .5, "center_y": .39}  
                
                MDList:
                    id: container
                    size_hint_y: 2
                    pos_hint: {'top' : .85}

            MDFloatingActionButton:
                icon: "arrow-left-thick"
                md_bg_color: 0.5, 0.5, 1, 1
                pos_hint: {'center_x': .14, 'center_y': .2}
                elevation: 12
                on_press: root.current = 'statistik'
                
            MDFloatingActionButton:
                icon: "home"
                md_bg_color: 0.5, 0.5, 1, 1
                pos_hint: {'center_x': .87, 'center_y': .2}
                elevation: 12
                on_press: root.current = 'start'

            BoxLayout:
                padding: '10dp'
                spacing: '4dp'
                orientation: 'vertical'
                size_hint_y: .3
                MDTextFieldRect:
                    id: infa
                    size_hint: 1, None
                    height: "30dp" 

                MDRaisedButton:
                    text: 'Fdt sortirung zufügen' 
                    size_hint: 1, None 
                    md_bg_color:  (65/255, 190/255, 242/255, 0.5)  
                    elevation: 10  
                    on_press: app.get_new_statistik(infa.text)      


'''

