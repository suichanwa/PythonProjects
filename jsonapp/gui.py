import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(
                    text='Hello from Kivy',
                    size_hint=(.5, .5),
                    pos_hint={'center_x': .5, 'center_y': .5},
                    font_size="34"
                )

        return label

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(self.username)
        self.add_widget = (Label(texr='name'))
        
        
    

if __name__ == "__main__":
    #app = MainApp()
    #app.run()
    pass