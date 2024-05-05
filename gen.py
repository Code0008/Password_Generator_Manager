#generador de contraseñas v0.3
import random
from tkinter import  *
from tkinter.scrolledtext import ScrolledText
import webbrowser

class Interfaz:
    count_passwords_generates = 0
    def __init__(self):
        self.main = main
    def make_interfaz(self):
        self.main = Tk()
        self.main.configure(bg="dark violet")
        self.main.geometry("1080x500")
        self.main.title("PASSWORD GEN")
        Interfaz.main_recomendations_text(self)
        Interfaz.buttons_recomendations(self)
        Interfaz.frame_contraseña(self)
        Interfaz.info_frame(self)
        self.main.mainloop()
    def frame_contraseña(self):
        self.frame = Frame(self.main, bg="cyan2")
        self.frame.pack( fill=BOTH,expand=1, padx=5)
    def main_recomendations_text(self):
        self.frame_recomendaciones = Frame(self.main, bg="blue")
        self.frame_recomendaciones.pack(fill=BOTH,side=LEFT, expand=1, padx=5, pady=5)
        self.text_widget = ScrolledText(self.main, state="disabled")
        self.text_widget.configure(bg="ivory3")
        self.text_widget.pack(padx=5, pady=5)
    def info_frame(self):
        self.boton = Button(self.frame, text="GENERAR CONTRASEÑA", command= lambda: Interfaz.insert_password(self), font=("Verdana", 15), bg='cyan3', fg='blue' )
        self.text_entry = Entry(self.frame)
        self.boton.pack(side=LEFT, padx=4, pady=5)
        self.text_entry.pack(side=LEFT,padx=4, pady=35)

    def buttons_recomendations(self):
        x = lambda: webbrowser.open('https://youtu.be/dQw4w9WgXcQ?si=e7sgqM3SLdvNOXd7')
        self.boton_infor = Button(self.frame_recomendaciones, text="BOTON INFORMACION", command=x,bg="cyan3", font=("Verdana", 12))
        self.boton_infor.pack( padx=5, pady=23)

    def make_password(self, longitud=None):
        letter = ['a','b','c','d','e','f','g','h','i','j','k','l']
        spcecial_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']
        nums = ["1","2","3","4","5","6","7","8","9"]
        pswd= []
        x=longitud
        while len(pswd)!=x:
            for _ in range(0, x):
                    if _ % 2 == 0:
                        pswd.append(random.choice(letter))
                        if len(pswd) == x: break
                    if _ % 2 != 0:
                        pswd.append(random.choice(spcecial_chars)) 
                        if len(pswd) == x: break
                    if _+2 % 2 != 0:
                        pswd.append(random.choice(nums))
                    if len(pswd) == x: break
        return ''.join(pswd)
                
    def insert_password(self):
        self.text_widget.configure(state="normal", font=("Verdana",10))
        try:
            longitud = int(self.text_entry.get())
            if longitud>100:
                self.text_widget.insert(END, f"\nLA CONTRASEÑA ES MAYOR A LO SOPORTADO\nY RECOMENDADO\n")
                return 0
            Interfaz.count_passwords_generates +=1 
            self.text_widget.insert(END, '|')
            for _ in range(0,50):
                self.text_widget.insert(END,'-') 
            self.text_widget.insert(END, f"|->Longitud({longitud})")   
            self.text_widget.configure(state="normal", font=("Verdana",10))
            self.text_widget.insert(END, f"\n|({Interfaz.count_passwords_generates}) Contraseña generada: {''.join(Interfaz.make_password(self, longitud))}\n")
        except ValueError as e:
            self.text_widget.insert(END, f"\nNO SE INGRESO NINGUN DIGITO!\n")
        finally:
            self.text_widget.config(state="disabled")
    
def main():
    inter = Interfaz()
    inter.make_interfaz()

if __name__ == '__main__':
    main()

