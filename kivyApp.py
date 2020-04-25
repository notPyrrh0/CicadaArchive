from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import ObjectProperty

# Initial Screen with cicada logo and prompt
class InitScr(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = [10, 20]
    
        # Cicada Ascii art
        self.cicada = Image()
        self.cicada.source = "src/cicada2.jpg"
        self.cicada.size_hint = (1, .75)
        
        self.lbl = Label()
        self.font_name = "src/DejaVuSansMono.ttf"
        self.lbl.text = """Thank you for helping to keep this archive up to date. Before you can create a 
        pull request, you need to update the tags of the files you've added."""
        self.lbl.halign = "center"        
        self.lbl.size_hint = (1, .15)
        self.lbl.font_size = 17


        self.prompt = Label()
        self.prompt.font_name = "src/DejaVuSansMono.ttf"
        self.prompt.text = "|========[  Click anywhere to continue  ]========|"
        self.prompt.halign = "center"        
        self.prompt.size_hint = (1, .10)
        self.prompt.font_size = 15
        self.animate()

        self.add_widget(self.cicada)
        self.add_widget(self.lbl)
        self.add_widget(self.prompt)

        # <!-- massive clusterfuck-->
        # anim = Animation(t=zero, duration=0.1) + Animation(t=zero, duration=1)
        # anim += Animation(t=full, duration=0.1) + Animation(t=full, duration=1)
        # anim.start(self.prompt)
        # anim.repeat = True

    ## FINALLY FUCKING SOLVED IT! Okay Im sleeping now :p
    def animate(self):
        anim = Animation(opacity=0, duration=1) + Animation(opacity=1, duration=1)
        anim += Animation(opacity=0, duration=1) + Animation(opacity=1, duration=1)
        anim.repeat = True
        anim.start(self.prompt)
        # < ------------------ >

    self = ObjectProperty(None)
    
    def on_touch_down(self, touch):
        main_app.screen_manager.current = "MainScr"


class MainScr(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.padding = [100, 100]
        self.spacing = 15

        self.autotag = Button() 
        self.autotag.text = "Autotag"
        
        self.tag = Button() 
        self.tag.text = "Tag"
        
        self.help = Button() 
        self.help.text = "Help Menu"
        
        self.add_widget(self.autotag)
        self.add_widget(self.tag)
        self.add_widget(self.help)

class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.title = "CicadaArchive"
        
        # Initial Screen
        self.init_scr = InitScr()
        screen = Screen(name="InitScreen")
        screen.add_widget(self.init_scr)
        self.screen_manager.add_widget(screen) 
        
        # Main Screen
        self.main_scr = MainScr()
        screen = Screen(name="MainScr")
        screen.add_widget(self.main_scr)
        self.screen_manager.add_widget(screen)
          
        return self.screen_manager

if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()