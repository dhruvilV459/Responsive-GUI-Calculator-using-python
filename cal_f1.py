from tkinter import *
expression = "" 


def clickbut(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 
def equalpress(): 
	try: 

		global expression 
		total = str(eval(expression)) 
		equation.set(total) 
		#expression = "" 

	except: 

		equation.set(" InValid Syntax ") 
		expression = "" 

def equalpress(event): 
	try: 

		global expression 
		total = str(eval(expression)) 
		equation.set(total) 
		#expression = "" 

	except: 

		equation.set(" error ") 
		expression = "" 


def clear(): 
	global expression 
	expression = "" 
	equation.set("") 

def clear1(event): 
	global expression 
	expression = "" 
	equation.set("")

def backspace():
        global expression
        expression=expression[:-1]
        equation.set(expression)

def backspace1(event):
        global expression
        expression=expression[:-1]
        equation.set(expression)


master = Tk() 

master.configure(background="#343434") 

master.title("Calculator") 


master.geometry("500x600")
#master.minsize(500,500)
equation = StringVar()
upper=Frame(master,width=50,height=30,relief=RAISED,)
upper.pack(side=TOP,expand=YES,fill=BOTH)

lower=Frame(master,height=50,relief=RAISED)
lower.pack(side=BOTTOM,fill=BOTH,expand=YES)

expression_field = Entry(upper,font=("arial",24,'bold'),state='disabled',bd=4,textvariable=equation,width=30,bg='#343434',fg='white',justify=RIGHT) 

expression_field.pack(side=TOP,fill=BOTH,expand=YES) 

equation.set('Enter your expression')

#photo = PhotoImage(file="download.png")

l1=Frame(master,width=50,height=40,bd=0,relief=RAISED)
l1.pack(side=TOP,fill=BOTH,expand=YES)

butback=Button(l1,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=backspace ,text="C",font=("Courier New",20,'bold'))
butback.pack(side=LEFT,fill=BOTH,expand=YES)

but7=Button(l1,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(7),text="7",font=("Courier New",20,'bold'))
but7.pack(side=LEFT,fill=BOTH,expand=YES)

but8=Button(l1,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(8),text="8",font=("Courier New",20,'bold'))
but8.pack(side=LEFT,fill=BOTH,expand=YES)

but9=Button(l1,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(9),text="9",font=("Courier New",20,'bold'))
but9.pack(side=LEFT,fill=BOTH,expand=YES)

butdiv=Button(l1,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut("/"),text="/",font=("Courier New",20,'bold'))
butdiv.pack(side=LEFT,fill=BOTH,expand=YES)


l2=Frame(master,width=50,height=40,bd=0,relief=RAISED)
l2.pack(side=TOP,fill=BOTH,expand=YES)

butclear = Button(l2,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=clear ,text="CE",font=("Courier New",20,'bold'))
butclear.pack(side=LEFT,fill=BOTH,expand=YES)

but4=Button(l2,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(4),text="4",font=("Courier New",20,'bold'))
but4.pack(side=LEFT,fill=BOTH,expand=YES)

but5=Button(l2,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(5),text="5",font=("Courier New",20,'bold'))
but5.pack(side=LEFT,fill=BOTH,expand=YES)

but6=Button(l2,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(6),text="6",font=("Courier New",20,'bold'))
but6.pack(side=LEFT,fill=BOTH,expand=YES)

butml=Button(l2,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut("*"),text="*",font=("Courier New",20,'bold'))
butml.pack(side=LEFT,fill=BOTH,expand=YES)



l3=Frame(master,width=50,height=40,bd=0,relief=RAISED)
l3.pack(side=TOP,fill=BOTH,expand=YES)

butmod=Button(l3,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut("%"),text="%",font=("Courier New",20,'bold'))
butmod.pack(side=LEFT,fill=BOTH,expand=YES)

but1=Button(l3,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(1),text="1",font=("Courier New",20,'bold'))
but1.pack(side=LEFT,fill=BOTH,expand=YES)

but2=Button(l3,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(2),text="2",font=("Courier New",20,'bold'))
but2.pack(side=LEFT,fill=BOTH,expand=YES)

but3=Button(l3,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(3),text="3",font=("Courier New",20,'bold'))
but3.pack(side=LEFT,fill=BOTH,expand=YES)

butsub=Button(l3,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut("-"),text="-",font=("Courier New",20,'bold'))
butsub.pack(side=LEFT,fill=BOTH,expand=YES)

#l4=Frame(master,width=50,height=20,bd=0,relief=RAISED)
#l4.pack(side=TOP,fill=BOTH,expand=YES)

butdot=Button(lower,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut("."),text=".",font=("Courier New",20,'bold'))
butdot.pack(side=LEFT,fill=BOTH,expand=YES)

but0=Button(lower,padx=27,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut(0),text="0",font=("Courier New",20,'bold'))
but0.pack(side=LEFT,fill=BOTH,expand=YES)

butequal=Button(lower,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=equalpress ,text="=" ,font=("Courier New",20,'bold'))
butequal.pack(side=LEFT,fill=BOTH,expand=YES)

butpl=Button(lower,padx=0,pady=0,bd=0,width=5,height=3,bg='#343434',fg='white',command=lambda:clickbut("+"),text="+",font=("Courier New",20,'bold'))
butpl.pack(side=LEFT,fill=BOTH,expand=YES)

"""but1.pack(fill=BOTH,expand=YES,side=TOP)
but2.pack(fill=BOTH,expand=YES,side=TOP)
but3.pack(fill=BOTH,expand=YES,side=TOP)
but4.pack(fill=BOTH,expand=YES,side=TOP)
but5.pack(fill=BOTH,expand=YES,side=TOP)
but6.pack(fill=BOTH,expand=YES,side=TOP)
but7.pack(fill=BOTH,expand=YES,side=TOP)


"""
master.bind(1,lambda event:clickbut(1))
master.bind(2,lambda event:clickbut(2))
master.bind(3,lambda event:clickbut(3))
master.bind(4,lambda event:clickbut(4))
master.bind(5,lambda event:clickbut(5))
master.bind(6,lambda event:clickbut(6))
master.bind(7,lambda event:clickbut(7))
master.bind(8,lambda event:clickbut(8))
master.bind(9,lambda event:clickbut(9))
master.bind(0,lambda event:clickbut(0))
master.bind("+",lambda event:clickbut("+"))
master.bind("-",lambda event:clickbut("-"))
master.bind("*",lambda event:clickbut("*"))
master.bind("/",lambda event:clickbut("/"))
master.bind("%",lambda event:clickbut("%"))
master.bind(".",lambda event:clickbut("."))
master.bind("<Escape>",clear1)
master.bind('<Return>',equalpress)
master.bind('<BackSpace>',backspace1)
#input('Enter to Exit')
master.mainloop()
input('Enter to Exit')
