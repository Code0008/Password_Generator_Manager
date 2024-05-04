#generador de contraseñas v0.2
import random
from tkinter import  *
from tkinter.scrolledtext import ScrolledText
class Interfaz:
    count_passwords_generates = 0
    def __init__(self):
        self.main = main
    def make_interfaz(self):
        self.main = Tk()
        self.main.configure(bg="dark violet")
        self.main.geometry("1080x500")
        self.main.title("PASSWORD GEN")
        self.text_widget = ScrolledText(self.main, state="disabled")
        self.text_widget.configure(bg="ivory3")
        self.text_widget.pack(padx=5, pady=5)
        self.frame = Frame(self.main, bg="cyan2")
        self.frame.pack(fill=BOTH, expand=1, padx=5)
        self.boton = Button(self.frame, text="GENERAR CONTRASEÑA", command= lambda: Interfaz.insert_password(self), width=200, height=200, font=("Verdana", 40), bg='cyan3', fg='blue' )
        self.boton.pack(side=BOTTOM, padx=4, pady=5)
        self.main.mainloop()
    def make_password(self):
        letter = ['a','b','c','d','e','f','g','h','i','j']
        spcecial_chars = ['!','"','#','$','%','&',"'", '(',')'] 
        nums = ["1","2","3","4","5","6","7"]
        pswd= []
        
        while len(pswd)!=16:
            for _ in range(0, 16):
                    if _ % 2 == 0:
                        pswd.append(random.choice(letter))
                        if len(pswd) == 16: break
                    if _ % 2 != 0:
                        pswd.append(random.choice(spcecial_chars)) 
                        if len(pswd) == 16: break
                    if _-2 % 2 != 0 or _+2 % 2 == 0:
                        pswd.append(random.choice(nums))
                        if len(pswd) == 16: break
        return ''.join(pswd)
                
    def insert_password(self):
        Interfaz.count_passwords_generates +=1 
        self.text_widget.configure(state="normal", font=("Verdana",10))
        self.text_widget.insert(END, '|')
        for _ in range(0,50):
            self.text_widget.insert(END,'-') 
        self.text_widget.insert(END,'|')   
        self.text_widget.configure(state="normal", font=("Verdana",10), fg='dark green')
        self.text_widget.insert(END, f"\n|({Interfaz.count_passwords_generates}) Contraseña generada: {''.join(Interfaz.make_password(self))}\n")
        self.text_widget.config(state="disabled")

def main():
    inter = Interfaz()
    inter.make_interfaz()

if __name__ == '__main__':
    main()
# Lo mejore en la misma madrugada que abuso
