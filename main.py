from tkinter import * 
import tkinter.font as font
import random

game_window = Tk()
game_window.title("Rock Paper Scissors Game")

app_font = font.Font(size = 12)

game_title = Label(game_window, text = "Rock Paper Scissors", font = font.Font(size = 20), fg = 'grey')
game_title.pack()

winner_label = Label(game_window, text = "Player Won!!", fg = "green", font = font.Font(size = 14))
winner_label.pack()

frame = Frame(game_window)
frame.pack()

player_options = Label(frame, text = "Your Options :", font = font.Font(size = 15), fg = "grey")
player_options.grid(row = 0, column = 0, padx = 8, pady = 5)

rock_button = Button(frame, text = "Rock", bg = "pink", padx = 8, pady = 5)
rock_button.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_button = Button(frame, text = "Paper", bg = "silver", padx = 8, pady = 5)
paper_button.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_button = Button(frame, text = "Scissors", bg = "lightblue", padx = 8, pady = 5)
scissors_button.grid(row = 1, column = 3, padx = 8, pady = 5)

score = Label(frame, text = "Score :", font = font.Font(size = 15), fg = "grey")
score.grid(row = 2, column = 0, padx = 8, pady = 5)

players_choice_label = Label(frame, text = "Player chose : ---", font = font.Font(size = 12))
players_choice_label.grid(row = 3, column = 1, padx = 8, pady = 5)

players_score_label = Label(frame, text = "Player score : ---", font = font.Font(size = 12))
players_score_label.grid(row = 3, column = 2, padx = 8, pady = 5)

computer_choice_label = Label(frame, text = "Computer chose : ---", font = font.Font(size = 12))
computer_choice_label.grid(row = 4, column = 1, padx = 8, pady = 5)

computer_score_label = Label(frame, text = "Computer score : ---", font = font.Font(size = 12))
computer_score_label.grid(row = 4, column = 2, padx = 8, pady = 5)

game_window.geometry('700x300')
game_window.mainloop()