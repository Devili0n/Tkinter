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
                #Storing the text into the text file
                with open("new.txt","w") as wtf:
                    ft=txt.get("1.0",END)
                    wtf.write(ft)
                    wtf.close()
                #Reading the text from text file for conversion
                with open("new.txt","r") as rtf:
                    rf=rtf.read()
                    tts=gTTS(text=rf,lang='en',slow=False)
                    tts.save('new.mp3')
                #Alert message for audio successfully created
                    tkinter.messagebox.showinfo("Alert",message="Conversion Successfully!!!")
            except:
                #If any error display this message                
                 tkinter.messagebox.showwarning(message="Please enter words properly!!!")
        def playsound():
            try:
                os.system("new.mp3")
            except:
                tkinter.messagebox.showwarning(message="Please enter words properly!!!")
    except:
         tkinter.messagebox.showwarning(message="Please enter words properly!!!")
    #Title of window
    t=("Text To Audio Conversion").center(100,"*")
    Label(main_window,text=t,fg="red",bg="lightblue",font=("Ariel 15 bold")).place(x=200,y=10)
    Label(main_window,text="Type here:-",fg="red",bg="lightblue",font=("Ariel 15 bold")).place(x=10,y=30)
    #Box for typing
    txt=Text(main_window,font=("Ariel 15 bold"),width=100,height=20)
    txt.place(x=100,y=60)
    # Button for submitting text
    Button(main_window,text="Submit",width=6,fg="white",bg="black",font=("Ariel 10 bold italic"),command=convert).place(x=50,y=580)
    # Button for playing audio file
    Button(main_window,text="Play",width=6,fg="white",bg="black",font=("Ariel 10 bold italic"),command=playsound).place(x=120,y=580)
    # Button for exit from the window
    Button(main_window,text="Exit",width=6,fg="white",bg="black",font=("Ariel 10 bold italic"),command=main_window.destroy).place(x=190,y=580)
    
    main_window.mainloop()
except:
    tkinter.messagebox.showwarning(message="Please enter words properly!!!")

