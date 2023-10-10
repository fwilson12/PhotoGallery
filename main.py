from kivy.app import App
from kivy.uix.screenmanager import Screen


class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def displayimage(self):
        return images[index]
    def advance(self):
        global index, images
        if index < len(images):
            index += 1
    def back(self):
        global index, images
        if index > 0:
            index -= 1



images = ['erosionbird.jfif''smurfcat.jfif']
index = 0
PhotoGalleryApp().run()

