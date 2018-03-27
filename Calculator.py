from tkinter import *

window=Tk()
window.title("Calculator")
#window.geometry('600x480')
window.configure(bg='powder blue')
text_input=StringVar()

#buttonClick is used to set the value of the any operator

operator=" "
def buttonClick(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)

def clearDisplay():
    global operator
    operator=" "
    text_input.set(" ")

def cal():
    global operator
    calculation=str(eval(operator))
    text_input.set(calculation)
    operator=' '

# this will take the input
textDisplay=Entry(window,font=('arial',20),textvariable=text_input,bd=7,insertwidth=4).grid(columnspan=4)



##########################################################################################################################
#command=lamda:buttonClick(7) is call the funtion where 7 is passed as a number it will use to set into the inputDisplay
btn7=Button(window,text="7",font=('arial',20,'bold'),padx=16,pady=8,bg='powder blue',command=lambda:buttonClick(7))\
    .grid(row=1,column=0)
btn8=Button(window,text="8",font=('arial',20,'bold'),padx=16,pady=8,bg='powder blue',command=lambda:buttonClick(8))\
    .grid(row=1,column=1)
btn9=Button(window,text="9",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick(9))\
    .grid(row=1,column=2)
division_btn=Button(window,text="/",font=('arial',20,'bold'),padx=18,pady=8,bg='powder blue',command=lambda:buttonClick('/'))\
    .grid(row=1,column=3)


######################################################################################################################
#for the next row we have to put the value row=2
btn4=Button(window,text="4",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick(4))\
    .grid(row=2,column=0)
btn5=Button(window,text="5",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick(5))\
    .grid(row=2,column=1)
btn6=Button(window,text="6",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick(6))\
    .grid(row=2,column=2)
multiply_btn=Button(window,text="x",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick('*'))\
    .grid(row=2,column=3)

#####################################################################################################################

btn1=Button(window,text="1",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick(1))\
    .grid(row=3,column=0)
btn2=Button(window,text="2",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick(2))\
    .grid(row=3,column=1)
btn3=Button(window,text="3",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick(3))\
    .grid(row=3,column=2)
subtract_btn=Button(window,text="-",font=('arial',20,'bold'),padx=18,pady=8,bg='powder blue',command=lambda:buttonClick('-'))\
    .grid(row=3,column=3)

#################################################################################################################
dot_btn=Button(window,text=".",font=('arial',20,'bold'),padx=18,pady=8,bg='powder blue',command=lambda:buttonClick('.')).\
    grid(row=4,column=0)
zero_btn=Button(window,text="0",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick(0)).\
    grid(row=4,column=1)
###############################################################################################################################

equal_btn=Button(window,text="=",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=cal).\
    grid(row=4,column=2)
plus_btn=Button(window,text="+",font=('arial',20,'bold'),padx=15,pady=8,bg='powder blue',command=lambda:buttonClick('+')).\
    grid(row=4,column=3)

######################################################################################################################

clear_btn=Button(window,text="del",font=('arial',20,'bold'),padx=8,pady=8,bg='powder blue',command=clearDisplay).\
    grid(row=5,column=0)




window.mainloop()