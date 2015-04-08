import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button

tuotteet_taso1={"wheat":{"hinta":35,"tyyppi":"ruoka"},
                "pork":{"hinta":55,"tyyppi":"ruoka"},
                "sugar":{"hinta":5,"tyyppi":"ruoka"},
                "milk":{"hinta":12,"tyyppi":"ruoka"},
                "herbs",
                "wool",
                "cotton",
                "wood",
                "fish",
               "stone",
               "chicken",
                "fruits",
                "vegetables",
                "rice",
                "iron",
                "copper",
                "tin",
                "aluminium",
                "plants",
                "salt"}




class MyApp(App):
    def build(self):
        return Button(text='Hello World')

if __name__ == '__main__':
    MyApp().run()
