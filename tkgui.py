from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar

fenster = Tk()
fenster.title("Gui")

#Fenstergröße wie Pi Display
fenster.geometry("800x480")
fenster.overrideredirect(True)
fenster.attributes('-fullscreen', True)

#Eingabe
eingabe = Entry(fenster)
eingabe.pack()

#Label
label1 = Label()
label1.pack()

#progressbar
bar = Progressbar(fenster, length=200, maximum = 100)
bar.pack()

#slider
def progakt(event):
    bar['value'] = slider1.get()
    
slider1 = Scale(fenster, from_= 100, to = 0, tickinterval = 20)
slider1.pack()
slider1.bind('<B1-Motion>', progakt)

#spinbox
var = IntVar()
var.set(55)
spinb = Spinbox(fenster, from_=0, to=100, width = 5, textvariable=var)
spinb.pack()




#Seite weiter
def weiter():
    label1.configure(text = (eingabe.get()))

knopf_we = Button(fenster, text = "weiter", command = weiter).pack(fill=X)

def rechnen():
    try:
        x = float(eingabe.get())
        label1.configure(text=(x**0.5))
    except:
        #label1.configure(text = "Bitte eine Zahl eingeben")
        messagebox.showerror("Fehler", "Bitte eine Zahl eingeben")



#Seite zurück
def zurueck():
    print("zurueck")
  
knopf_zu = Button(fenster, text = "rechnen", command = rechnen).pack(fill=X)



#Verlassen per Knopfdruck
knopf_ex = Button(fenster, text = "Exit", command = exit).pack(fill=X)


mainloop()
