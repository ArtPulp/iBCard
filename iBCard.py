from kivy.app import App
from kivy.uix.label import Label


class iBCardApp(App):
    def build(self):
        return Label(text="Hello, iBCard")


iBCardApp().run()