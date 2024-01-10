from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

import webbrowser
from kivy.core.clipboard import Clipboard
from shareImageFile import Fileshare

# to connect python file to the kivy file
Builder.load_file('blueprintFrontend.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        timeNow = time.strftime('%Y%m%d-H%M%S')
        self.filepathway = "files/" + timeNow + ".png"
        self.ids.camera.export_to_png(self.filepathway)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepathway

class ImageScreen(Screen):
    def create_link(self):
            file_path = App.get_running_app().root.ids.camera_screen.filepathway
            fileshare = Fileshare(filepath = file_path)
            self.url = fileshare.share()
            self.ids.link.text = self.url
    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = "You Didn't Create A Link Yet"
    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = "Where's your link? You didn't create one yet"

class Rootwidget(ScreenManager):
    pass
class MainApp(App):
    def build(self):
        return Rootwidget()

MainApp().run()
