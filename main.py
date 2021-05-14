import  kivy
from kivy import Config

Config.set('graphics'  , 'multisamples'  , '0')


from kivy.uix.gridlayout import GridLayout
from kivy.app import  App
from  kivy.uix.textinput import TextInput
from kivy.uix.button import  Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
print(kivy.version)

from kivy.lang import Builder
dd = Builder.load_string("""
<Button>:
    font_size:30



<normal_button>
    final_answer:answer
    calculations: working_out

    GridLayout:

        cols:1
        size: root.width , root.height -30

        pos:0, 30
        GridLayout:



            cols: 1

            TextInput:
                font_size:70
                id:working_out
                multiline:False

            Label:

                font_size:30
                id:answer
                canvas.before:
                    Color:
                        rgba:0,1,0,1
                    Rectangle:
                        size:self.size
                        pos:self.pos

        GridLayout:

            cols:4
            Button:
                text:'1'
                on_press:root.pressed('1')



            Button:
                text:'2'
                on_press:root.pressed('2')
            Button:
                text:"3"
                on_press:root.pressed('3')
            Button:
                text:'x'
                on_press:root.pressed('x')
            Button:
                text:'4'
                on_press:root.pressed('4')

            Button:
                text:'5'
                on_press:root.pressed('5')
            Button:
                text:'6'
                on_press:root.pressed('6')
            Button:
                text:'/'
                on_press:root.pressed('/')
            Button:
                text:'7'
                on_press:root.pressed('7')
            Button:
                text:'8'
                on_press:root.pressed('8')
            Button:
                text:'9'
                on_press:root.pressed('9')
            Button:
                text:'-'
                on_press:root.pressed('-')
            Button:
                text:'C'
                on_press:root.calculations.text = ''
            Button:
                text:'0'
                on_press:root.pressed('0')

            Button:
                text:'.'
                on_press:root.pressed('.')
            Button:
                text:'+'
                on_press:root.pressed('+')
    GridLayout:
        cols:2
        size:root.width,30
        Button:
            text:'EXIT'
            on_press:exit()
        Button:
            font_size:10
            text:'app by leting'




""")


class normal_button(GridLayout):
    calculations = ObjectProperty(None)
    final_answer = ObjectProperty(None)

    def xtostar(self , digits):
        final = ''
        for digit in digits:
            if digit == 'x':
                digit = '*'
            final = final + digit
        return (final)

    def test_output(self):


        try:


            self.final_answer.text =str(( eval(self.xtostar( self.calculations.text))))
        except:
            print('cant do')
            pass

    def pressed(self, no):
        self.calculations.text = self.calculations.text + no
        self.test_output()
    pass
class calcu(App):
    def  build(self):

        return normal_button()

if __name__  == '__main__':
    calcu().run()