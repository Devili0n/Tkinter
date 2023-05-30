from gtts import gTTS
import os
from tkinter import*
import tkinter.messagebox
from PIL import Image,ImageTk


try:
    main_window=Tk()
    main_window.title("Text To Audio")
    main_window.geometry("1000x1000")
    main_window.state("zoomed")
    main_window.configure(bg="lightblue")
    try:
        def convert():
            #Converting the text into speech
            try:
                with open("new.txt","w") as wtf:
                    ft=txt.get("1.0",END)
                    wtf.write(ft)
                    wtf.close()
                with open("new.txt","r") as rtf:
                    rf=rtf.read()
                    tts=gTTS(text=rf,lang='en',slow=False)
                    tts.save('new.mp3')
                    gi=('file has creaated')
                    Label(main_window,text=gi,fg="purple",bg="lightblue",font=("Ariel 12 bold")).place(x=10,y=650)
            except:
                 tkinter.messagebox.showwarning(message="Please enter words properly!!!")
    except:
         tkinter.messagebox.showwarning(message="Please enter words properly!!!")
    t=("Text To Audio Conversion").center(100,"*")
    Label(main_window,text=t,fg="red",bg="lightblue",font=("Ariel 15 bold")).place(x=200,y=10)
    Label(main_window,text="Enter the text:-",fg="red",bg="lightblue",font=("Ariel 15 bold")).place(x=10,y=30)
    txt=Text(main_window,font=("Ariel 15 bold"),width=100,height=23)
    txt.place(x=10,y=60)
    Button(main_window,text="Submit",width=6,fg="white",bg="black",font=("Ariel 10 bold italic"),command=convert).place(x=50,y=620)
    Button(main_window,text="Exit",width=6,fg="white",bg="black",font=("Ariel 10 bold italic"),command=main_window.destroy).place(x=120,y=620)
    main_window.mainloop()
except:
    tkinter.messagebox.showwarning(message="Please enter words properly!!!")

