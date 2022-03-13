from tkinter import *
from backEnd import *
root = Tk()
root.title("Word Meaning Scheduling")
root.geometry('1920x1080')

# input for number of words required per day

readDataFromFile()


# input for each day of a week 
days = {'Sunday':IntVar(),'Monday':IntVar(),'Tuesday':IntVar(),'Wednesday':IntVar(),'Thursday':IntVar(),'Friday':IntVar(),'Saturday':IntVar()}

word = get_word_number()
no_of_word = StringVar(value = str(word))
dic = get_dic()
for k,v in dic.items():
    if dic[k] == 1:
        days[k] = IntVar(value = 1)


label1 = Label(root,text = "Enter the Number of Words you want to learn each day",width=100,height = 2,justify=CENTER,font=("bold",16))
label1.place(x = 90,y = 60)
label1.pack()
entry1 = Entry(root,width = 50,textvariable=no_of_word)
entry1.pack()



for day,value in days.items():
    l = Checkbutton(root, text=day, variable=days[day], width = 110, height=3,font = ("bold",12),justify=CENTER)
    l.pack(anchor = 'w')


def proceedFun():
    word = no_of_word.get()
    writeDataInFile(word,days)
    root.destroy()
    # getting days of the weeks
    

def closeWindow():
    root.destroy()
    
MyButton1 = Button(root, text="Submit", width=30,height = 3,justify=CENTER, command=proceedFun)
MyButton1.pack(anchor = 'w')
MyButton1.place(x = 400,y = 960)

MyButton1 = Button(root, text="Cancel", width=30,height = 3,justify=CENTER, command=closeWindow)
MyButton1.pack(anchor = 'w')
MyButton1.place(x = 1000,y = 960)

root.mainloop()

   
    