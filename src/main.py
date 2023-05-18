from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.scatter import Scatter

from kivy.core.window import Window
from kivy.uix.widget import Widget
import kivy
import math
from kivy.config import Config
Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '1280')
kivy.require('1.9.0')

Window.fullscreen = 'auto'
Window.size = (720, 1280)
w_s=Window.size


txt1 =  "Введите ваш рост в сантиметрах: "
txt2 =  "Введите ваш вес в килограммах: "

the_weight = 1
the_height = 1

#the_height = float(input("Введите ваш рост в сантиметрах: "))  
#the_weight = float(input("Введите ваш вес в килограммах: "))  
# defining a function for BMI  

txt11 =  ""# txt1
txt12 = ""# txt2

#class MyWidget(Widget):
 
txtw = ["У вас излишне большой недостаток в весе.","У вас недостаточный вес.",
"У вас нормальный вес.","У вас избыточная вес.","У вас 1 степень ожирения.","У вас 2 степень ожирения.",
"У вас 3 степень ожирения." ]

class MyLabel(Label):
   def on_size(self, *args):
      self.text_size = self.size
 
class MainApp(App):

    def build(self):
        self.b = FloatLayout()

        mk = 100
        jl = 180
        jb = 20
        ng = 200
        amk =-700
        self.t = TextInput(font_size = 15,size_hint_y = None,height = 50
                    #  ,pos =(0, 500)) 
                      ,pos =(0, w_s[1]-mk*0+jl+ng+amk)) 
        self.ta = TextInput(font_size = 15,size_hint_y = None,height = 50
                      ,pos =(0, w_s[1]-mk*1+jl+ng+amk))        
      #  f = FloatLayout()
     #   self.s = Scatter()


        self.label = MyLabel(text=txt1,
                      size_hint=(.5, .5),
                      #pos_hint={'center_x': 1.0, 'center_y': 1.0},
                    #  ,pos =(80, 530))
                    halign="left", valign="middle",
                      pos =(jb, w_s[1]-mk*0+jl+amk))
        self.label1 = MyLabel(text=txt2,
                      size_hint=(0.5, 0.5),
                    halign="left", valign="middle",
                      #pos_hint={'center_x': 1.0, 'center_y': 1.0},
                    #  ,pos =(80, 460))
                      pos =(jb, w_s[1]-mk*1+jl+amk))
        zjl = 80
        self.label2 = MyLabel(text=txt11,
                    halign="left", valign="middle",
                     # pos_hint={'center_x': 1.0, 'center_y': 1.0},
                    # valign="middle"
                      size_hint=(0.5, 0.5),
                   #   ,pos =(80, 460))#
                      pos =(jb, w_s[1]-mk*2+amk+(zjl*0.9)))
        self.label3 = MyLabel(text=txt12,
                      #pos_hint={'center_x': 1.0, 'center_y': 1.0},
                     halign="left", valign="middle",
                     # valign="middle"
                      size_hint=(0.5, 0.5),
                     # ,pos =(80, 460))#
                      pos =(jb, w_s[1]-mk*3+amk+(zjl*1.7)))
            
    #  pos_hint={'center_x':  0, 'center_y': 0.0}, size_hint=(0, 0),
       
                   
        self.btn = Button(text ="Ввести данные",
                   font_size ="16sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(22, 22),
                   size_hint =(.19, .07),
                   pos =(10, w_s[1]-mk*1+jl+amk+100))
        #self.b.add_widget(self.s)
        self.b.add_widget(self.label)
        self.b.add_widget(self.t)
        self.b.add_widget(self.label1)
        self.b.add_widget(self.ta)
        self.b.add_widget(self.btn)
        self.b.add_widget(self.label2)
        self.b.add_widget(self.label3)
     #   t.bind(text = label.setter('text'))
     #   ta.bind(text = label1.setter('text'))
        self.label2.bind(size=self.label2.setter('text_size'))  
        self.label3.bind(size=self.label3.setter('text_size'))  
        self.btn.bind(on_press = self.callback)
        #btn.bind(on_press = self.callback(label.setter('text'),label1.setter('text')))
  

        # Привязка к этикетке

        return self.b
    


    def callback(self, event):
        the_weight = self.ta.text
        the_height =  self.t.text
        
        if ( the_weight.isdigit() == True and the_height.isdigit() == True):
            the_weight =  int(self.ta.text)
            the_height =  int(self.t.text)
            the_BMI =  round(the_weight / (the_height/100)**2,3  )
            # printing the BMI  
            txtbmi = "Ваш индекс массы тела равен:" + str(the_BMI) 
            print(txtbmi)  


            i = 0
            if the_BMI <= 16: 
                i = 0 
            elif the_BMI <= 18.5:  
                i = 1
            elif the_BMI <= 24.9:  
                i = 2
            elif the_BMI <= 29.9:  
                i = 3
            elif the_BMI <= 34.9:  
                i = 4
            elif the_BMI <= 39.9:  
                i = 5
            else:  
                i = 6
        

            print(txtw[i]) 


            
            
            txt11 =   txtbmi
            txt12 = txtw[i]
            

            self.label2.text = txt11
            self.label3.text = txt12



 
if __name__ == '__main__':
    app = MainApp()
    app.run()