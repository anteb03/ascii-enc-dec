from tkinter import *
from tkinter import messagebox
import base64
import os

def dekriptiraj():
    screen2=Toplevel(screen)
    screen2.title("Dekriptirana poruka")
    screen2.geometry("400x200")

    message=unos1.get(1.0, END)
    decode_message= message.encode("ascii")
    base64_bytes=base64.b64decode(decode_message)
    decrypt=base64_bytes.decode("ascii")

    text2=Text(screen2,relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=180)
    text2.insert(END,decrypt)

def enkriptiraj():
    screen1=Toplevel(screen)
    screen1.title("Enkriptirana poruka")
    screen1.geometry("400x200")

    message=unos1.get(1.0, END)
    encode_message= message.encode("ascii")
    base64_bytes=base64.b64encode(encode_message)
    encrypt=base64_bytes.decode("ascii")

    text2=Text(screen1,relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=180)
    text2.insert(END,encrypt)

def main_screen():
    global unos1
    global screen
    screen=Tk()
    screen.geometry("380x250")
    screen.title("Enkr/dekr")
    tekst1=Label(text="Unesi tekst:")
    tekst1.pack()
    tekst1.place(x=155, y=40)
    unos1= Text(bg="white",relief=GROOVE,wrap=WORD,width=30,height=3)
    unos1.place(x=65, y=70)
    Button(text="Enkriptiraj",height=2,width=23,bg="#ed3833",fg="white",bd=0,command=enkriptiraj).place(x=10, y=150)
    Button(text="Dekriptiraj",height=2,width=23,bg="#00bd56",fg="white",bd=0,command=dekriptiraj).place(x=200, y=150)
    screen.mainloop()
main_screen()

