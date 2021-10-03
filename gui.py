# from tkinter import *

# root = Tk()
# root.geometry("300x200")

# w = Label(root, text ='GeeksForGeeks', font = "50")
# w.pack()

# Checkbutton1 = IntVar()
# Checkbutton2 = IntVar()
# Checkbutton3 = IntVar()

# Button1 = Checkbutton(root, text = "Tutorial",
# 					variable = Checkbutton1,
# 					onvalue = 1,
# 					offvalue = 0,
# 					height = 2,
# 					width = 10)

# Button2 = Checkbutton(root, text = "Student",
# 					variable = Checkbutton2,
# 					onvalue = 1,
# 					offvalue = 0,
# 					height = 2,
# 					width = 10)

# Button3 = Checkbutton(root, text = "Courses",
# 					variable = Checkbutton3,
# 					onvalue = 1,
# 					offvalue = 0,
# 					height = 2,
# 					width = 10)
	
# Button1.pack()
# Button2.pack()
# Button3.pack()

# mainloop()


from tkinter import *

top = Tk()
top.title("Word Meaning Scheduling")
top.geometry('1920x1080')

def helloCallBack():
#    tkMessageBox.showinfo( "Hello Python", "Hello World")
	print("button is Clicked")
 
# B = Button(top, text ="Hello", command = helloCallBack)
# B.pack()
MyButton1 = Button(top, text="Submit", width=10, command=helloCallBack)
MyButton1.grid(row=1, column=1)
top.mainloop()