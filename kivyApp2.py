import kivy
# kivy.require('1.11.1')

from kivy.app import App, Builder
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.animation import Animation
from kivy.properties import ObjectProperty, ListProperty

# from kivy.config import Config
# Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class InitScr(Screen):
    self = ObjectProperty(None)

    def animate(self):
        anim = Animation(opacity=0, duration=1) + Animation(opacity=1, duration=1)
        anim += Animation(opacity=0, duration=1) + Animation(opacity=1, duration=1)
        anim.repeat = True
        anim.start(self.prompt)

    # animate(self.prompt)

    def on_touch_down(self, touch):
        sm.current = "MainScr"
        
class MainScr(Screen):
    pass

class WindowManager(ScreenManager):
    pass
    
sm = WindowManager()

kv_file = Builder.load_file('config.kv')
screens = [InitScr(name="InitScr"),
            MainScr(name="MainScr")]
for screen in screens:
    sm.add_widget(screen)

class MainApp(App):
    def build(self): 
        self.title = "CicacdaArchiver"
        return sm

MainApp().run()
