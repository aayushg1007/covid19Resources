from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image, AsyncImage


#verified delhi (remdesivir) -"not verified" -"unverified" -"needed" -"need" -"needs" -"required" -"require" -"requires" -"requirement" -"requirements" -"DM"
list_wanted = []



tips = "Tips \n1. Make sure search results are sorted by *Latest* \n2. Do NOT make Advanced Payments unless you are 100% sure about their authenticity "
KV ='''
Screen:
    ScrollView:
        MDBoxLayout:
            padding: "20dp"
            orientation:"vertical"
            size: root.width, root.height
            MDToolbar:
                title: "Covid-19 Resources"
            MDLabel:
                text: "Developed by FTC"
                text_size: "10dp", "10dp"
                size_hint_y: 0.1
            MDLabel:
                text: "Search"
                size: "48dp", "48dp"
                size_hint_y: 0.1
            MDLabel:
                canvas.before:
                    Color: 
                        rgba: (0, 0, 0, 0.2)
                    Rectangle:
                        size: self.size
                        pos: self.pos
                size_hint_y: None
                height: 5
            MDTextField:
                id: city
                mode: "rectangle"
                required: True
                size_hint_x: .5
                hint_text: "City Name"
            ScrollView:
                effect_cls: 'OpacityScrollEffect'
                size: 5,5
                MDGridLayout:
                    cols: 4
                    size_hint_y: None
                    MDLabel:
                        text: "    Beds"
                    MDCheckbox:
                        size_hint: None, None
                        size: "48dp", "48dp"
                        on_active: app.on_checkbox1_active(*args)
                    MDLabel:
                        text: "    Remidesivir"
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
            
                
            MDRectangleFlatButton:
                text: "Generate Link"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                on_release: app.gen_link()  
            
                    
    '''
class Covid_Resources(MDApp):
    
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
            joined_string = "+OR+".join(list_wanted)
            citystr=(self.root.ids["city"].text).lower()
            nr ='+-%22not+verified%22+-%22unverified%22+-%22needed%22+-%22need%22+-%22needs%22+-%22required%22+-%22require%22+-%22requires%22+-%22requirement%22+-%22requirements%22&f=live'
            link = "https://twitter.com/search?q="+"verified+"+citystr+"+"+"%28"+joined_string+"%29"+nr
            import webbrowser
            webbrowser.open(link)
        self.dialog = MDDialog(title="Link", text=tips, size_hint=(0.7, 1), buttons=[
            MDFlatButton(
                text="CONTINUE", 
                text_color=self.theme_cls.primary_color, 
                on_release= lambda x: link_open())])
        self.dialog.open()
     
    
    def build(self):
        return Builder.load_string(KV)        
Covid_Resources().run()
