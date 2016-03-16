#tu jest moj main
from tkinter import *
from Samolot import *
def addPlane():
    # print(nazwaSamolotu.get())
    # print(odleglosc.get())
    # print(paliwo.get())
    # print(predkosc.get())
    plane = Samolot(nazwaSamolotu.get(), odleglosc.get(), paliwo.get(), predkosc.get())
    plane.poprawnosc()
    plane.print()
    plane.run()

def makeWindow():
    global nazwaSamolotu, odleglosc, paliwo, predkosc
    window = Tk()
    frame1 = Frame(window)
    frame1.pack()

    Label(frame1, text="Nazwa samolotu").grid(row=0, column=0, sticky=W)
    nazwaSamolotu = StringVar()
    name = Entry(frame1, textvariable=nazwaSamolotu)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Odległość do przebycia [km]").grid(row=1, column=0, sticky=W)
    odleglosc = DoubleVar()
    name = Entry(frame1, textvariable=odleglosc)
    name.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Ilosc paliwa [l] ").grid(row=2, column=0, sticky=W)
    paliwo = DoubleVar()
    name = Entry(frame1, textvariable=paliwo)
    name.grid(row=2, column=1, sticky=W)

    Label(frame1, text="Prędkość [km/h]").grid(row=3, column=0, sticky=W)
    predkosc = DoubleVar()
    name = Entry(frame1, textvariable=predkosc)
    name.grid(row=3, column=1, sticky=W)

    frame2 = Frame(window)
    frame2.pack()
    b1 = Button(frame2, text="Submit", command=addPlane)
    b1.pack(side=LEFT)
    return window

window = makeWindow()
window.mainloop()
window.quit()
