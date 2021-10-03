from tkinter import *

root = Tk()
root.title("Word Meaning Scheduling")
root.geometry('1920x1080')

no_of_word = IntVar()
label1 = Label(root,text = "Enter the Number of Words you want to learn each day",width=100,height = 2,justify=CENTER,font=("bold",16))
label1.place(x = 90,y = 60)
label1.pack()
entry1 = Entry(root,width = 50,textvariable=no_of_word)
entry1.pack()

days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
dayInput = [IntVar() for i in range(7)]
for x in range(len(days)):
    l = Checkbutton(root, text=days[x], variable=dayInput[x], width = 110, height=3,font = ("bold",12),justify=CENTER)
    l.pack(anchor = 'w')


def proceedFun():
    # getting number of words 
    words = int(no_of_word.get())
    # getting days of the weeks
    for c in dayInput:
        print(c.get())
    

def closeWindow():
    root.destroy()
    
MyButton1 = Button(root, text="Submit", width=30,height = 3,justify=CENTER, command=proceedFun)
MyButton1.pack(anchor = 'w')
MyButton1.place(x = 400,y = 960)

MyButton1 = Button(root, text="Cancel", width=30,height = 3,justify=CENTER, command=closeWindow)
MyButton1.pack(anchor = 'w')
MyButton1.place(x = 1000,y = 960)

root.mainloop()
