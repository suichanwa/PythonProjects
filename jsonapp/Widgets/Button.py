from tkinter import Button
import kivy
from kivy.uix.boxlayout import BoxLayout

class RootWidget(BoxLayout):
    def __inti__(self, **kwargs):
        super(RootWidget, self).__inti__(**kwargs)
        self.add_widget(Button(text="btn 1"))
        cb = CustomBtn()
        
        
    def btn_pressed(self, instance, pos):
        print('pos: printed from root widget: {pos}'.format(pos.pos))
        