import tkinter as tk
import customtkinter as ctk

class App(): 
    def __init__(self):
        #general settings application
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self._app = ctk.CTk()
        self._app.geometry('350x450')
        self._app.resizable(False, False)
        self._app.title('Калькулятор')

        #num buttons
        self.__create_button('1', self.__button_1, 0.2, 0.4)
        self.__create_button('2', self.__button_2, 0.35, 0.4)
        self.__create_button('3', self.__button_3, 0.5, 0.4)
        self.__create_button('4', self.__button_4, 0.2, 0.5)
        self.__create_button('5', self.__button_5, 0.35, 0.5)
        self.__create_button('6', self.__button_6, 0.5, 0.5)
        self.__create_button('7', self.__button_7, 0.2, 0.6)
        self.__create_button('8', self.__button_8, 0.35, 0.6)
        self.__create_button('9', self.__button_9, 0.5, 0.6)
        self.__create_button('0', self.__button_0, 0.35, 0.7)

        #operation buttons
        self.__create_button('C', self.__button_clear, 0.65, 0.3)
        self.__create_button('<=', self.__button_backspace, 0.8, 0.3)
        self.__create_button('+', self.__button_plus, 0.8, 0.4)
        self.__create_button('-', self.__button_minus, 0.8, 0.5)
        self.__create_button('*', self.__button_multiply, 0.8, 0.6)
        self.__create_button('/', self.__button_divide, 0.8, 0.7)
        self.__create_button('=', self.__button_result, 0.8, 0.85)
        self.__create_button(',', self.__button_point, 0.5, 0.7)
        #string output information
        self.__create_textbox()
        self._output_string = ''

        self._app.mainloop()

    #function button-click reaction
    def __button_1(self):
        self.__write_output('1')
    def __button_2(self):
        self.__write_output('2')
    def __button_3(self):
        self.__write_output('3')
    def __button_4(self):
        self.__write_output('4')
    def __button_5(self):
        self.__write_output('5')
    def __button_6(self):
        self.__write_output('6')
    def __button_7(self):
        self.__write_output('7')
    def __button_8(self):
        self.__write_output('8')
    def __button_9(self):
        self.__write_output('9')
    def __button_0(self):
        self.__write_output('0')
    def __button_plus(self):
        self.__write_output('+')
    def __button_minus(self):
        self.__write_output('-')
    def __button_multiply(self):
        self.__write_output('*')
    def __button_divide(self):
        self.__write_output('/')
    def __button_backspace(self):
        self._output_string = self._output_string[:-1]
        self.__write_output('')
    def __button_clear(self):
        self._output_string = ''
        self.__write_output('')
    def __button_point(self):
        try:
            int(self._output_string[-1])
            self.__write_output(',')
        except:
            pass
    
    #main function
    def __button_result(self):
        if '+' in self._output_string:
            nums = self._output_string.split('+')
            self._output_string = str(int(nums[0]) + int(nums[1]))
        elif '-' in self._output_string:
            nums = self._output_string.split('-')
            self._output_string = str(int(nums[0]) - int(nums[1]))
        elif '*' in self._output_string:
            nums = self._output_string.split('*')
            self._output_string = str(int(nums[0]) * int(nums[1]))
        elif '/' in self._output_string:
            nums = self._output_string.split('/')
            self._output_string = str(int(nums[0]) / int(nums[1]))
        else:
            self._output_string = '0'
        self.__write_output('')

    #create stuffs
    def __create_button(self, text: str, anchor_func, posX:[float, int], posY:[float, int]) -> ctk.CTkButton:
        but = ctk.CTkButton(master=self._app, text=text, height=40, width=40,
        command=anchor_func, font=('Arial Bold', 24))
        but.place(relx=posX, rely=posY, anchor=tk.CENTER)
        return but
    def __create_textbox(self):
        self.output_panel = ctk.CTkTextbox(master=self._app, width=250, height=30, state=tk.DISABLED, 
        activate_scrollbars=False, font=('Arial', 24))
        self.output_panel.place(relx = 0.5, rely = 0.1, anchor = tk.CENTER)

    #write something
    def __write_output(self, text: str):
        self.output_panel.configure(state=tk.NORMAL)
        self._output_string += text
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
        self.output_panel.configure(state=tk.DISABLED)

def main():
    app = App()

if __name__ == '__main__':
    main()