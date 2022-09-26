import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
import json 
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

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
        
def show_json():
    with open('jsonapp/data.json') as json_file:
        data = json.load(json_file)
        print (data["age"])

class TestApp2(App):
    def get_x(label, ref_x):
        return label.center_x - label.texture_size[1]


class TestApp(App):

    @staticmethod
    def get_x(label, ref_x):
        """ Return the x value of the ref/anchor relative to the canvas """
        return label.center_x - label.texture_size[0] * 0.5 + ref_x

    @staticmethod
    def get_y(label, ref_y):
        """ Return the y value of the ref/anchor relative to the canvas """
        return label.center_y + label.texture_size[1] * 0.5 - ref_y

    def show_marks(self, label):

        for name, anc in label.anchors.items():
            with label.canvas:
                Color(1, 0, 0)
                Rectangle(pos=(self.get_x(label, anc[0]),
                               self.get_y(label, anc[1])),
                          size=(3, 3))

        for name, boxes in label.refs.items():
            for box in boxes:
                with label.canvas:
                    Color(0, 1, 0, 0.25)
                    Rectangle(pos=(self.get_x(label, box[0]),
                                   self.get_y(label, box[1])),
                              size=(box[2] - box[0],
                                    box[1] - box[3]))

    def build(self):
        label = Label(
            text='[anchor=a]a\nChars [anchor=b]b\n[ref=myref]ref[/ref]',
            markup=True,
            font_size = "23")
        Clock.schedule_once(lambda dt: self.show_marks(label), 1)
        return label

if __name__ == "__main__":
    TestApp().run()