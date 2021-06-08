import tkinter
import random # For random functions

window = tkinter.Tk()
window.title("DiceThrower")

def RandomNumber():
    MyRandom = random.randint(1,6)
    dice_thrown.configure(text="Dice thrown: " + str(MyRandom))
 
MyTitle = tkinter.Label(window, text="Throw A Dice!",font="Verdana 16 bold")
MyTitle.pack()
 
MyButton = tkinter.Button(window, text="OK", command=RandomNumber)
MyButton.pack()
 
dice_thrown = tkinter.Label(window, font="Helvetica 16 bold")
dice_thrown.pack()
 
window.mainloop()
