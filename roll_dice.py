from tkinter import *
import random
 

root=Tk()
#define geometry
root.geometry("600x600")
 

l1=Label(root,font=("Helvetica",300))
 
def roll():
    #create a number variable in which the list of all the ASCII characters of the string will be stored
    #Use backslash because unicode must have a backslash 
    dice=['\u2687','\u2681','\u2682','\u2683','\u2684','\u2685','\u2686']
    #configure the label
    l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()
     
b1=Button(root,text="Roll the Dice!!!",foreground='red',command=roll)
b1.place(x=300,y=0)
b1.pack()
 
root.mainloop()


