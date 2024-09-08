from tkinter import *
import tkinter.font as f
root = Tk()
root.title("Rock paper siccors game")
root.geometry("700x300")
root.config(background="light grey")

heading = Label(root,text="Rock, Paper, Sciccors game",font=f.Font(size=20),fg="grey")
heading.pack()

footer = Label(root,text="Lets start the game",font=f.Font(size=13),fg="green")
footer.pack()

frame=Frame(root)
frame.pack()

label1 = Label(frame,text="Your options:",font=f.Font(size=12),fg="grey")
label1.grid(row=0,column=0,pady=8)

rock = Button(frame,text="Rock",width=15,bd=0,fg="black",bg="pink",pady=5,padx=8)
rock.grid(row=1,column=1)

paper = Button(frame,text="Paper",width=15,bd=0,fg="black",bg="silver",pady=5,padx=8)
paper.grid(row=1,column=2)

sciccors = Button(frame,text="sciccors",width=15,bd=0,fg="black",bg="light blue",pady=5,padx=8)
paper.grid(row=1,column=3)

label2 = Label(frame,text="Score:",font=f.Font(size=12),fg="grey")
label






