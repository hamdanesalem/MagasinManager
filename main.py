from kivy.app import App
from kivy.uix.label import Label

class StoreApp(App):
    def build(self):
        return Label(text="StoreManager v4.0")

if __name__ == "__main__":
    StoreApp().run()
