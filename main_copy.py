from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image, AsyncImage
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty

list_wanted = []

tips = "This Link will redirect you to Twitter Recent Covid Resorces Post \n\nTips: \n  -Do NOT make Advanced Payments unless you are 100% sure about their authenticity "

Builder.load_string('''
<Screen_Manager>:
    id: screen_manager
    MenuScreen:
        id: menu
        name: "menu"
    NextScreen:
        id: next1
        name:"next1"
<MenuScreen>:
    NavigationLayout:
        id: nl
        ScreenManager:
            id: scr_mngr
            Screen:
                id: screen1
                MDBoxLayout:
                    id: bl
                    orientation:"vertical"
                    spacing: "10dp"
                    MDToolbar:
                        title: "Covid-19 Resources"
                        size_hint_y: None
                        left_action_items: [["menu", lambda x: nav_d.toggle_nav_drawer()]]
                    MDLabel:
                        text: "  Search"
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        halign: "center"
                        canvas.before:
                            Color: 
                                rgba: (0, 0, 0, 0.2)
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        size_hint_y: None
                        height: 5
                    MDTextField:
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        id: city
                        mode: "rectangle"
                        required: True
                        size_hint_x: .5
                        hint_text: "Enter city name"
                    ScrollView:
                        effect_cls: "ScrollEffect"
                        MDStackLayout:
                            padding: "10dp"
                            spacing: "10dp"
                            size_hint_y: None
                            height: self.minimum_height                            
                            
                            MDGridLayout:
                                cols: 4
                                size_hint_y: None
                                height: self.minimum_height
                                MDLabel:
                                    text: "    Beds"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox1_active(*args)
                                MDLabel:
                                    text: "    Remdesivir"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox2_active(*args)
                                MDLabel:
                                    text: "    ICU"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox3_active(*args)
                                MDLabel:
                                    text: "    Plasma"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox4_active(*args)
                                MDLabel:
                                    text: "    Oxygen"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox5_active(*args)
                                MDLabel:
                                    text: "    Ventilator"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox6_active(*args)
                                MDLabel:
                                    text: "    Tests"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox7_active(*args)
                                MDLabel:
                                    text: "    Fabiflu"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox8_active(*args)
                                MDLabel:
                                    text: "    Favipiravir"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox9_active(*args)
                                MDLabel:
                                    text: "    Tocilizumab"
                                MDCheckbox:
                                    size_hint: None, None
                                    size: "48dp", "48dp"
                                    on_active: app.on_checkbox10_active(*args) 
                                MDLabel:
                                    text: "    Other: "  
                            
                                MDTextFieldRect:
                                    id: other
                                    mode: 'rectangle'
                                    required: False
                                    size_hint_x: .30
                                    size_hint_y: None
                                    height: self.minimum_height
                                    
                    MDFloatingActionButton:
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        icon: "arrow-right"
                        md_bg_color: app.theme_cls.primary_color
                        on_release: root.save()
                        on_release: root.manager.transition.direction = 'left'
                        on_release: root.manager.current = 'next1'
                        
                        padding: "20dp"
        
        MDNavigationDrawer:
            id: nav_d   
            BoxLayout:
                padding: "10dp"
                spacing: "10dp"
                orientation: "vertical"
                Image:
                    source: "download.jpg"
                MDLabel:
                    text: "Developed by Aayush"
                    
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "aayushg.1007@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: "Source Code"
                            on_release: app.sourcecode()
                        TwoLineListItem:
                            text: "Check for App Updates"
                            secondary_text: "v0.3"
                            on_release: app.update_app()
<NextScreen>:
    NavigationLayout:
        ScreenManager: 
            Screen:
                name: "next1"
                halign: "center"
                MDBoxLayout:
                    spacing: "20dp"
                    orientation: "vertical"
                    MDToolbar:
                        title: "Covid-19 Resources"
                        size_hint_y: None
                        left_action_items: [["arrow-left", lambda x:root.manager.change_screen('menu')]]
                    MDLabel:
                        halign: "center"
                        text: "TIPS: "
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        halign: "center"
                        text: "- Make sure search results are sorted by *Latest* "
                        font_style: 'Caption'
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                    Image:
                        source: "i.jpg"
                        size_hint_y: None
                        size: "80dp", "80dp"
                    
                    MDLabel:
                        halign: "center"
                        canvas.before:
                            Color: 
                                rgba: (0, 0, 0, 0.1)
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        size_hint_y: None
                        height: 5
                    MDLabel:
                        halign: "center"
                        font_style: 'Caption'

                    MDFillRoundFlatIconButton:
                        text: "Generate Link"
                        icon: "twitter"
                        md_bg_color: app.theme_cls.primary_color
                        on_release: app.gen_link()
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        
                    Widget:
                    

    
''')
class MenuScreen(Screen):
    def save(self):
        self.error1 = MDDialog(title="Error", text='Enter City Name')
        if (self.ids.other.text) !="":
            list_wanted.append(self.ids.other.text)

        joined_string = "+OR+".join(list_wanted)
        citystr= self.ids.city.text           
        nr ='+-%22not+verified%22+-%22unverified%22+-%22needed%22+-%22need%22+-%22needs%22+-%22required%22+-%22require%22+-%22requires%22+-%22requirement%22+-%22requirements%22&f=live'
        global link
        link = "https://twitter.com/search?q="+"verified+"+citystr+"+"+"%28"+joined_string+"%29"+nr
        print(link)
    pass

class NextScreen(Screen):
    
    pass

class Screen_Manager(ScreenManager):
    def change_screen(self, screen):
        self.transition.direction = 'right'
        self.current = 'menu'
    pass

class Test(MDApp):
    def update_app(self):
        import webbrowser
        webbrowser.open('https://covid19resourcesapp.blogspot.com/2021/04/updates-for-covid-19-resources-app.html')

    def sourcecode(self):
        import webbrowser
        webbrowser.open('https://github.com/aayushg1007/Covid19ResourcesApp')
        

    def on_checkbox1_active(self, checkbox, value):
        if value:
            list_wanted.append("beds")
            list_wanted.append("bed")
            print(list_wanted)
        else:
            list_wanted.remove("beds")
            list_wanted.remove("bed")
            print(list_wanted)
    def on_checkbox2_active(self, checkbox, value):
        if value:
            list_wanted.append("remdesivir")
            print(list_wanted)
        else:
            list_wanted.remove("remdesivir")
            print(list_wanted)
    def on_checkbox3_active(self, checkbox, value):
        if value:
            list_wanted.append("icu")
            print(list_wanted)
        else:
            list_wanted.remove("icu")
            print(list_wanted)
    def on_checkbox4_active(self, checkbox, value):
        if value:
            list_wanted.append("plasma")
            print(list_wanted)
        else:
            list_wanted.remove("plasma") 
            print(list_wanted)
    def on_checkbox5_active(self, checkbox, value):
        if value:
            list_wanted.append("oxygen")
            print(list_wanted)
        else:
            list_wanted.remove("oxygen") 
            print(list_wanted)
    def on_checkbox6_active(self, checkbox, value):
        if value:
            list_wanted.append("ventilator")
            list_wanted.append("ventilators")
            print(list_wanted)
        else:
            list_wanted.remove("ventilator") 
            list_wanted.remove("ventilators")
            print(list_wanted)
    def on_checkbox7_active(self, checkbox, value):
        if value:
            list_wanted.append("tests")
            list_wanted.append("testing")
            list_wanted.append("test")
            print(list_wanted)
        else:
            list_wanted.remove("tests")
            list_wanted.remove("testing")
            list_wanted.remove("test") 
            print(list_wanted)
    def on_checkbox8_active(self, checkbox, value):
        if value:
            list_wanted.append("fabiflu")
            print(list_wanted)
        else:
            list_wanted.remove("fabiflu") 
            print(list_wanted)
    def on_checkbox9_active(self, checkbox, value):
        if value:
            list_wanted.append("favipiravir")
            print(list_wanted)
        else:
            list_wanted.remove("favipiravir") 
            print(list_wanted)
    def on_checkbox10_active(self, checkbox, value):
        if value:
            list_wanted.append("tocilizumab")
            print(list_wanted)
        else:
            list_wanted.remove("tocilizumab") 
            print(list_wanted)
    def gen_link(self):
        def link_open():
            import webbrowser
            webbrowser.open(link)
        self.dialog = MDDialog(title="Link", text=tips, size_hint=(0.7, 1), buttons=[
                MDFlatButton(
                    text="LINK", 
                    text_color=self.theme_cls.primary_color, 
                    on_release= lambda x: link_open())
                ])

        self.dialog.open()

    def build(self):        
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(NextScreen(name='next1'))
        
        return Screen_Manager()       
Test().run()
