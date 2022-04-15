from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("307x340")
#create textbox
txtBox = Entry(root,font=("default",18),borderwidth=4)
txtBox.grid(row=0,column=0,columnspan=4,padx=5,pady=20)



def buttonClicked(number):
	existingNum = txtBox.get()
	txtBox.delete(0,END)
	txtBox.insert(0,existingNum+str(number))

def clearButton():
	txtBox.delete(0,END)

def calcOperation(operator):
	global first_number
	global whatOperation

	temp = txtBox.get()
	whatOperation = operator
	first_number = int(temp)
	if (first_number is None) or (whatOperation is None):
		return
	txtBox.delete(0,END)

def equalCalculation():
	second_number = txtBox.get()

	if whatOperation is None: return
	elif whatOperation == "+":
		calculate = first_number + int(second_number)
	elif whatOperation == "-":
		calculate = first_number - int(second_number)
	elif whatOperation == "*":
		calculate = first_number * int(second_number)
	elif whatOperation == "/":
		calculate = first_number / int(second_number)
	else: return

	txtBox.delete(0,END)
	txtBox.insert(0,calculate)

def displayButtons():
	#create buttons
	button_1 = Button(root,text="1",padx=30,pady=20, command=lambda: buttonClicked(1))
	button_2 = Button(root,text="2",padx=30,pady=20, command=lambda: buttonClicked(2))
	button_3 = Button(root,text="3",padx=30,pady=20, command=lambda: buttonClicked(3))
	button_4 = Button(root,text="4",padx=30,pady=20, command=lambda: buttonClicked(4))
	button_5 = Button(root,text="5",padx=30,pady=20, command=lambda: buttonClicked(5))
	button_6 = Button(root,text="6",padx=30,pady=20, command=lambda: buttonClicked(6))
	button_7 = Button(root,text="7",padx=30,pady=20, command=lambda: buttonClicked(7))
	button_8 = Button(root,text="8",padx=30,pady=20, command=lambda: buttonClicked(8))
	button_9 = Button(root,text="9",padx=30,pady=20, command=lambda: buttonClicked(9))
	button_0 = Button(root,text="0",padx=30,pady=20, command=lambda: buttonClicked(0))

	button_add = Button(root,text="+",padx=28,pady=20, command=lambda: calcOperation("+"))
	button_subtract = Button(root,text="_",padx=29,pady=20, command=lambda: calcOperation("-"))
	button_multiply = Button(root,text="*",padx=29,pady=20, command=lambda: calcOperation("*"))
	button_divide = Button(root,text="/",padx=29,pady=20, command=lambda: calcOperation("/"))
	button_equals = Button(root,text="=",padx=29,pady=20, command=equalCalculation)
	button_clear = Button(root,text="C",padx=29,pady=20, command=clearButton)

	#order the buttons
	button_1.grid(row=3,column=0)
	button_2.grid(row=3,column=1)
	button_3.grid(row=3,column=2)
	button_4.grid(row=2,column=0)
	button_5.grid(row=2,column=1)
	button_6.grid(row=2,column=2)
	button_7.grid(row=1,column=0)
	button_8.grid(row=1,column=1)
	button_9.grid(row=1,column=2)
	button_0.grid(row=4,column=0)

	button_add.grid(row=4,column=3)
	button_subtract.grid(row=3,column=3)
	button_multiply.grid(row=2,column=3)
	button_divide.grid(row=1,column=3)
	button_equals.grid(row=4,column=2)
	button_clear.grid(row=4,column=1)


displayButtons()
root.mainloop()
