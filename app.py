from kivy.app import App
from kivy.uix.button import Button

from main_screen.main_screen import CalculatorWidget


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
