from tkinter import *
import tkinter.font as f
import random
root = Tk()
root.title("Rock paper siccors game")
root.geometry("700x300")

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('sciccors',2)]

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text="Computer Won!!!!!")
    computor_score_label.config(text='Computer Score : ' +str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))
  
def player_wins():
    global computer_score, player_score
    player_score += 1
    winner_label.config(text="Player Won!!!!!")
    computor_score_label.config(text='Computer Score : ' +str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))

def tie():
    global computer_score, player_score
    winner_label.config(text="TIE!!!")
    computor_score_label.config(text='Computer Score : ' +str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))

def player_choice(player_input):
    global player_score, computer_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer_input)
    player_choice_label.config(text = 'Your selected : ' + player_input[0])
    computor_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if(player_input == computer_input):
        tie()

    #if player has chosen rock
    if(player_input[1] == 0):
        if (computer_input[1] == 1):
            #this means the computer wins
            computer_wins()
        elif (computer_input[1] == 2):
            #this means the player wins
            player_wins()
    #if player has paper
    elif(player_input[1] == 1):
        if(computer_input[1] == 0):
            #this means the player wins
            player_wins()
        elif (computer_input[1] == 2):
            #this means the computer wins
            computer_wins()
    #if the player has scissors
    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            #this means the coputer wins
            computer_wins()
        elif (computer_input[1] == 1):
            #this means the player wins
            player_wins()
    

#function to randomly select computer choice
def get_computer_choice():
    return random.choice(options)

game_title = Label(root,text="Rock, Paper, Sciccors game",font=f.Font(size=20),fg="grey")
game_title.pack()

winner_label = Label(root,text="Lets start the game",font=f.Font(size=13),fg="green",pady=8)
winner_label.pack()

frame=Frame(root)
frame.pack()

player_options = Label(frame,text="Your options:",font=f.Font(size=12),fg="grey")
player_options.grid(row=0,column=0,pady=8)

rock_btn = Button(frame,text="Rock",width=15,bd=0,bg="pink",pady=5,command = lambda: player_choice(options[0]))
rock_btn.grid(row=1,column=1,padx=8,pady=5)

paper_btn = Button(frame,text="Paper",width=15,bd=0,bg="silver",pady=5,command = lambda: player_choice(options[1]))
paper_btn.grid(row=1,column=2,pady=5,padx=8)

sciccors_btn = Button(frame,text="Sciccors",width=15,bd=0,bg="light blue",pady=5,command = lambda: player_choice(options[2]))
sciccors_btn.grid(row=1,column=3,pady=5,padx=8)

score_label = Label(frame,text="Score:",font=f.Font(size=12),fg="grey")
score_label.grid(row=2,column=0)

player_choice_label = Label(frame,text="You selected---",font=f.Font(size=12))
player_choice_label.grid(row=3,column=1,pady=5)

player_score_label = Label(frame,text="Your score:-",font=f.Font(size=12))
player_score_label.grid(row=3,column=2,pady=5)

computor_choice_label = Label(frame,text="computer selected---  ",font=f.Font(size=12))
computor_choice_label.grid(row=4,column=1,pady=5)

computor_score_label = Label(frame,text="Computer score:-",font=f.Font(size=12))
computor_score_label.grid(row=4,column=2,pady=5)

root.mainloop()








