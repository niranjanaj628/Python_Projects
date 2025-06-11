from tkinter import *

window=Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=10,pady=10)

# label
label=Label(text="This is a label", font=("Arial",20,"bold"))
label['text']='New text'
# label.config('text'='new text')
# label.pack()
# label.place(x=100,y=100)
label.grid(column=0,row=0)
label.config(padx=10, pady=10)


# Button
def click():
    label['text']="The button was clicked!"
    new_text=input.get()
    label.config(text=new_text)
    
button= Button(text='Click me', command=click)
# button.pack()
button.grid(column=1,row=1)


new_button=Button(text='new button')
new_button.grid(column=2, row=0)

# enter
input=Entry()
# input.pack()
input.grid(column=3,row=2)


window.mainloop()