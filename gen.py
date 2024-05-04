#generador de contraseñas v0.1
import random
from tkinter import  *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

class Interfaz:
    def __init__(self):
        self.main = main
    def make_interfaz(self):
        self.main = Tk()
        self.main.configure(bg="SlateBlue2")
        self.main.geometry("1080x500")
        self.main.title("PASSWORD GEN")
        self.text_widget = ScrolledText(self.main, state="disabled")
        self.text_widget.pack(padx=5, pady=5)
        self.frame = Frame(self.main, bg="DeepSkyBlue2")
        self.frame.pack(fill=BOTH, expand=1, padx=5)
        self.boton = Button(self.frame, text="GENERAR CONTRASEÑA", command= lambda: Interfaz.make_password(self), width=200, height=200, font=("Verdana", 40), bg='cyan', fg='blue' )
        self.boton.pack(side=BOTTOM, padx=4, pady=5)
        self.main.mainloop()
    def make_password(self):
        letter = ['a','b','c','d','e','f','g','h','i','j']
        spcecial_chars = ['!','"','#','$','%','&',"'", '(',')'] 
        nums = ["1","2","3","4","5","6","7"]
        pswd= []
        for _ in range(4):
                pswd.append(random.choice(letter))
                pswd.append(random.choice(spcecial_chars)) 
                pswd.append(random.choice(nums))

        self.text_widget.configure(state="normal", font=("Verdana",10))
        self.text_widget.insert(END, f"\nContraseña generada: {''.join(pswd)} ")
        self.text_widget.config(state="disabled")

def main():
    inter = Interfaz()
    inter.make_interfaz()

if __name__ == '__main__':
    main()
