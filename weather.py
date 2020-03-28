from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line


class Weather(Widget):
    pass


class PongApp(App):
    def build(self):
        return Weather()


if __name__ == '__main__':
    PongApp().run()
