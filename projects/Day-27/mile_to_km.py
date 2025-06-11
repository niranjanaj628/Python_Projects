from tkinter import *

window=Tk()
window.title("Miles to km converter")
window.minsize(width=350, height=200)

def converter(): 
    miles=float(input.get())
    km=miles*1.6
    print(km)
    label_2=Label(text=f'is equal to      {round(km,2)}       km')
    label_2.place(x=130, y=40)

input=Entry()
label_1=Label(text='  Miles')
label_2=Label(text='is equal to      0       km')
button=Button(text='Calculate', command=converter)

input.place(x=130,y=20)
label_1.place(x=210,y=20)
label_2.place(x=130, y=40)
button.place(x=160,y=60)

window.mainloop()