from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

from libs.screens.home_page import HomePage, HomePage2


class InstagramApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.load_all_kv_files()

        sm = ScreenManager()
        sm.add_widget(HomePage(name='menu'))
        sm.add_widget(HomePage2(name='settings'))

        return sm

    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/appbar.kv')
        Builder.load_file('libs/components/story_creator.kv')
        Builder.load_file('libs/components/bottom_nav.kv')
        Builder.load_file('libs/components/circular_avatar_image.kv')
        Builder.load_file('libs/components/post_card.kv')


if __name__ == "__main__":
    InstagramApp().run()
