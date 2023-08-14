import openai
import connection
from tkinter import *

#Interfaz principal
ChatGPT = Tk()
ChatGPT.title("Text-Davinci-003")
#ChatGPT.resizable(0,0)
ChatGPT.iconbitmap("bitmap.dll")
#Cuadro Abajo
Cuadro = Frame(ChatGPT,width="720", height="480")
Cuadro.pack(fill="both", expand=1)
Cuadro.config(bg="#C4D7D9")
Cuadro.config(bd=5)
Cuadro.config(relief="sunken")
logoUCI=PhotoImage(file="mascas.dll")
#Texto 1
Entradatext= Entry(Cuadro)
Entradatext.grid(row=1,column=1,sticky="w")

Textoo= Label(Cuadro,text="Buscar:", bg="#C4D7D9",font=("Comic Sans MS", 10))
Textoo.grid(row=1,column=0,sticky="e")

LgUCI= Label(Cuadro,image=logoUCI,bg="#C4D7D9")
LgUCI.grid(row=0, column=0)
#Fianl del cuadro
ChatGPT.mainloop()