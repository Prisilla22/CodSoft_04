from tkinter import*
import random
top=Tk()
top.title('Rock Paper Scissor Game')
top.geometry('1500x1500')
top.config(bg='White')
bg = PhotoImage(file = "img.jpg")
canvas1 = Canvas(top, width = 1500, height = 1500) 
canvas1.pack(fill = "both", expand = True) 
canvas1.create_image( 200, 400, image = bg,anchor = "nw") 

def show():
    ch=choice_.get()
    output.config(text='Your Choice: '+str(ch))
    output.place(x=630,y=220)
    
    
choice_=StringVar()

#To enter user choice
Label(top,text="What will you like to choose").place(x=600,y=10)
Label(top,text=" Rock ").place(x=600,y=30)
Label(top,text=" Paper ").place(x=600,y=50)
Label(top,text=" Scissor ").place(x=600,y=70)
Label(top,text="Enter your choice:").place(x=600,y=100)
Entry(top,textvariable=choice_).place(x=600,y=120)

#submit button for user
Button(top,text="Submit",command=show).place(x=650,y=180)
output=Label(top,text="Your Choice:")

#for computer choice
def comp_choice():
    ch=choice_.get()
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    comp.config(text="Computer Choice: "+str(computer_choice))
    comp.place(x=610,y=300)
    output.config(text='Your Choice: '+str(ch))
    output.place(x=630,y=220)

#Who wins
    if(ch == "Rock"):
        if(computer_choice == "Rock"):
            result.config(text="It's a Tie")
            result.place(x=650,y=340)
        elif(computer_choice == "Paper"):
            result.config(text="Computer Wins")
            result.place(x=640,y=340)
        else:
            result.config(text="You Win")
            result.place(x=650,y=340)
    if(ch == "Paper"):
        if(computer_choice == "Rock"):
            result.config(text="You Win")
            result.place(x=650,y=340)
        elif(computer_choice == "Paper"):
            result.config(text="It's a Tie")
            result.place(x=650,y=340)
        else:
            result.config(text="Computer wins")
            result.place(x=640,y=340)
    if(ch == "Scissor"):
        if(computer_choice == "Rock"):
            result.config(text="Computer Wins")
            result.place(x=640,y=340)
        elif(computer_choice == "Paper"):
            result.config(text="You win")
            result.place(x=650,y=340)
        else:
            result.config(text="It's a Tie")
            result.place(x=650,y=340)
    
Button(top,text="Ask computer to choose",command=comp_choice).place(x=610,y=250)
result=Label(top,text="Result")
comp=Label(top,text="Computer Choice")


top.mainloop()