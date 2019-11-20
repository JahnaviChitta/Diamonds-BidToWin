from tkinter import *
import random
import tkinter.messagebox
from tkinter import simpledialog

scores = 0
shown_diamonds = []
turns = 0
comp_score = 0
unshown_diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
available_cBids = unshown_diamonds[:]
draw_list = []
def First_page():
    tk = Tk()
    tk.title("Diamonds")
    tk.configure(background = "coral")
    tk.geometry("800x650")

    def display_second_page():
        Second_page()
    def quit_game():
        tk.destroy()
        quit()

    quit_button = Button(tk, text = "Quit", width = 6, font = "none 15 bold", bg = "light sea green", command = quit_game)
    quit_button.place(x = 200, y = 350)

    play_button = Button(tk, text = "Play", width = 6, font = "none 15 bold", bg = "light sea green", command  = display_second_page)
    play_button.place(x = 200, y = 300)
    tk.mainloop()

def Second_page():
    tk = Tk()
    tk.title("Diamonds")
    tk.configure(background = "forest green")
    tk.geometry("800x650")
    def Continue():
        print("Continued") 
    def newgame():
        tk.destroy()
        Second_page()
    def exit_button():
        answer = tkinter.messagebox.askquestion("Exit?", "Do you really want to exit?", icon = "warning")
        if answer == "yes":
            tk.destroy()
            exit()
    def About():
        about_the_game = "     \n\nIt is an interesting game where you need to bid on diamond card that is turned up.You can play the game until all your cards are used.For the diamond to be yours, you need to bid the higher value card than your opponet(computer).If you bid the amount same that of the computer, the diamond goes into the DRAW BOX.The final scores will decide the winner.\nThis is how the game goes.Get started with the game...\n\n   "    
        tkinter.messagebox.showinfo("Diamonds", about_the_game, icon = "info")
       
    def hearts_button_selected():
        Remove_buttons()
        def hearts_loop():
            global shown_diamonds
            d = diamond_label()
            shown_diamonds.append(d)
            display_hearts()

        def display_hearts():
            is_hearts_displayed = True
            if No_of_cards > 7:
                for i in range(7):
                    Button(tk, image = player_cards[i], command = lambda i = i : hearts_card_value(i+1)).grid(row = 5, column = i )
                for i in range(7, No_of_cards):
                    Button(tk, image = player_cards[i], command = lambda i = i: hearts_card_value(i+1)).grid(row = 6, column = i - 7)

        def hearts_card_value(n):
            global scores
            global turns
            global comp_score
            turns += 1
            label = Label(tk, text = "Your\n Bid", bg = "forest green", fg = "black")
            label.grid(row = 7, column = 1)
            Label(tk, image = spades[n-1], anchor = CENTER).grid(row = 8, column = 1)
            if n <= 7:
                Button(tk, image = small_icon).grid(row = 5, column = n-1)
            else:
                Button(tk, image = small_icon).grid(row = 6, column = n-8)
            cBid = computer_display()
            
            if signum(n, cBid) == 1:
                scores += shown_diamonds[-1]
            elif signum(n, cBid) == -1:
                comp_score += shown_diamonds[-1]
            else:
                draw_list.append(shown_diamonds[-1])
            Label(tk, text = "Opponent\nScore: " + str(comp_score), bg = "forest green", fg = "pink", font = "none 13 bold").grid(row = 0, column = 6)
            Label(tk, text = str(Player_name) + "'s\nScore : " + str(scores), bg = "forest green", fg = "pink", font = "none 13 bold").grid(row = 1, column = 6)

            if len(unshown_diamonds):
                d = diamond_label()
                shown_diamonds.append(d)
                Display_result_of_turn(n, cBid, d)

            if turns == 13:
                Display_final_result(scores, comp_score)
                      
        player_cards = hearts[:]
        hearts_loop()

    def clubs_button_selected():
        def clubs_loop():
            Remove_buttons()
            global shown_diamonds
            d = diamond_label()
            shown_diamonds.append(d)
            display_clubs()

        def display_clubs():
            is_clubs_displayed = True
            for i in range(7):
                Button(tk, image = player_cards[i], command = lambda i = i: clubs_card_value(i+1)).grid(row = 5, column = i)
            for i in range(7, 13):
                Button(tk, image = player_cards[i], command = lambda i = i: clubs_card_value(i+1)).grid(row = 6, column = i - 7)

        def clubs_card_value(n):
            global scores
            global turns
            global comp_score
            turns += 1
            label = Label(tk, text = "Your\n Bid", bg = "forest green", fg = "black")
            label.grid(row = 7, column = 1)
            Label(tk, image = spades[n-1], anchor = CENTER).grid(row = 8, column = 1)
            if n <= 7:
                Button(tk, image = small_icon).grid(row = 5, column = n-1)
            else:
                Button(tk, image = small_icon).grid(row = 6, column = n-8)
                
            cBid = computer_display()            
            if signum(n, cBid) == 1:
                scores += shown_diamonds[-1]
            elif signum(n, cBid) == -1:
                comp_score += shown_diamonds[-1]
            else:
                draw_list.append(shown_diamonds[-1])
            Label(tk, text = "Opponent\nScore: " + str(comp_score), bg = "forest green", fg = "pink", font = "none 13 bold").grid(row = 0, column = 6)
            Label(tk, text = str(Player_name) + "'s\nScore : " + str(scores), bg = "forest green", fg = "pink", font = "none 13 bold").grid(row = 1, column = 6)

            if len(unshown_diamonds):
                d = diamond_label()
                shown_diamonds.append(d)
                Display_result_of_turn(n, cBid, d)
            if turns ==  13:
                Display_final_result(scores, comp_score)

        player_cards = clubs[:]
        clubs_loop()

    def spades_button_selected():        
        def spades_loop():
            Remove_buttons()
            global shown_diamonds
            d = diamond_label()
            shown_diamonds.append(d)
            display_spades()
            return d

        def display_spades():
            is_spades_displayed = True
            for i in range(7):
                Button(tk, image = player_cards[i], command = lambda i = i:spades_card_value(i+1)).grid(row = 5, column = i)
            for i in range(7, 13):
                Button(tk, image = player_cards[i], command = lambda i = i:spades_card_value(i+1)).grid(row = 6, column = i - 7)
        
        def spades_card_value(n):
            global scores
            global turns
            global comp_score
            turns += 1
            label = Label(tk, text = "Your\n Bid", bg = "forest green", fg = "black")
            label.grid(row = 7, column = 1)
            Label(tk, image = spades[n-1], anchor = CENTER).grid(row = 8, column = 1)
            if n <= 7:
                Button(tk, image = small_icon).grid(row = 5, column = n-1)
            else:
                Button(tk, image = small_icon).grid(row = 6, column = n-8)            
            cBid = computer_display()
            
            if signum(n, cBid) == 1:
                scores += shown_diamonds[-1]
            elif signum(n, cBid) == -1:
                comp_score += shown_diamonds[-1]
            else:
                draw_list.append(shown_diamonds[-1])
            Label(tk, text = "Opponent\nScore: " + str(comp_score), bg = "forest green", fg = "pink", font = "none 13 bold").grid(row = 0, column = 6)
            Label(tk, text = str(Player_name) + "'s\nScore: " + str(scores), bg = "forest green", fg = "pink", font = "none 13 bold").grid(row = 1, column = 6)
            if len(unshown_diamonds):
                d = diamond_label()
                shown_diamonds.append(d)
                Display_result_of_turn(n, cBid, d)
            if turns == 13:
                Display_final_result(scores, comp_score)
        player_cards = spades[:]        
        spades_loop()

    icon = PhotoImage(file = "diamond_icon_2.png")
    small = icon.zoom(21, 21)
    small_icon = small.subsample(50, 50)

    def diamond_label():
        global unshown_diamonds
        diamond_number = random.choice(unshown_diamonds)
        unshown_diamonds.remove(diamond_number)
        diamond_shownup = diamonds[diamond_number - 1]
        Label(tk, image = diamond_shownup, anchor = CENTER).grid(row = 1, column = 4)
        return diamond_number
            
    def computer_display():
        global available_cBids
        cBid = random.choice(available_cBids)
        available_cBids.remove(cBid)
        cBid_card = clubs[cBid - 1]
        Label(tk, text = "Opponet\nbid", bg = "forest green", fg = "black").grid(row = 7, column = 4)
        Label(tk, image = cBid_card).grid(row = 8, column = 4)
        return cBid

    def Display_result_of_turn(player_bid, computer_bid, d):
        if signum(player_bid, computer_bid) == 1:
            result_of_the_turn = "You got the diamond!!\n\nKeep rocking for the next diamond-" + str(d) + " also"
        elif signum(player_bid, computer_bid) == -1:
            result_of_the_turn = "Unlucky!!\n\nYou lost it\nTry for the diamond-" + str(d) + "  "
        else:
            result_of_the_turn = "It's a tie...\n\nJust miss...Go ahead, diamond-" + str(d) + " is waiting for your bid..."
        tkinter.messagebox.showinfo("Ohh!", result_of_the_turn)
     
    def Display_final_result(scores, comp_score):
        if signum(scores, comp_score) == 1:
            tkinter.messagebox.showinfo("Congrats!!", "Congratulations!!\nYou won the game.\n\nYour Score = "+str(scores) + "\nOpponet Score is "+str(comp_score))
        elif signum(scores, comp_score) == -1:
            tkinter.messagebox.showinfo("Ohh Noo!!", "You lost the game!\nThe scores are:\n\nYour score = "+str(scores) +"\nOpponet Score = "+str(comp_score) + "\n\nBetter Luck next time")
        else:
            tkinter.messagebox.showinfo("Oops!!", "It's a tie...\nThe scores being:\n\nYour Score = "+str(scores) + "\nOpponet Score = "+str(comp_score)+"\n\nBetter Luck next time")
        tk.destroy()
        quit()    

    def Remove_buttons():
        Label(tk, text = "All", width = 6, height = 2, font = "none 15 bold", bg = "forest green", fg = "purple3").grid(row = 1, column = 0)
        Label(tk, text = "The", width = 6, height = 2, font = "none 15 bold", bg = "forest green", fg = "purple3").grid(row = 1, column = 1)
        Label(tk, text = "Best!", width = 6, height = 2, font = "none 15 bold", bg = "forest green", fg = "purple3").grid(row = 1, column = 2)
        Label(tk, text = "     ", width = 6, height = 2, font = "none 15 bold", bg = "forest green").grid(row = 0, column = 0)

    def Ask_player_name():
        Player_name = simpledialog.askstring("Go!", "Enter Player Name*", parent = tk)
        if len(Player_name) > 9 or len(Player_name) == 0:
            tkinter.messagebox.showerror("Error", "Please enter name having atleast one and lessthan 10 characters")
            Ask_player_name()
        return Player_name
    
    def signum(a, b):
        if a - b > 0:
            return 1
        elif a - b < 0:
            return -1
        return 0

    menu = Menu(tk)
    tk.config(menu = menu)
    SubMenu = Menu(menu)
    menu.add_cascade(label = "Options", menu = SubMenu)
    SubMenu.add_command(label = "New Game", command = newgame)
    SubMenu.add_separator()
    SubMenu.add_command(label = "Continue", command = Continue)
    SubMenu.add_command(label = "Exit", command = exit_button)
    editMenu = Menu(menu)
    menu.add_cascade(label = "Help", menu = editMenu)
    editMenu.add_command(label = "About", command = About)
    
    No_of_cards = 13
    diamonds = []
    for i in range(1, No_of_cards + 1):
        card = "diamonds-" + str(i) + "-75.png"
        diamonds.append(PhotoImage(file = card))
    spades = []
    for i in range(1, No_of_cards + 1):
        card = "spades-" + str(i) + "-75.png"
        spades.append(PhotoImage(file = card))
    clubs = []
    for i in range(1, No_of_cards + 1):
        card = "clubs-" + str(i) + "-75.png"
        clubs.append(PhotoImage(file = card))
    hearts = []
    for i in range(1, No_of_cards + 1):
        card = "hearts-" + str(i) + "-75.png"
        hearts.append(PhotoImage(file = card))
    list_of_cards = [clubs, spades, hearts]
    
    Label(tk, text = "Choose", bg = "forest green", fg = "pink", font = "none 15 bold").grid(row = 0, column = 0)
    spades_button = Button(tk, text = "Spades", width = 5, font = "none 12 bold", command = spades_button_selected).grid(row = 1, column = 0)
    hearts_button = Button(tk, text = "Hearts", width = 5, font = "none 12 bold", command = hearts_button_selected).grid(row = 1, column = 1)
    clubs_button = Button(tk, text = "Clubs", width = 5, font = "none 12 bold", command = clubs_button_selected).grid(row = 1, column = 2)
    Label(tk, text = "Diamond\nto bid", bg = "forest green", fg = "pink", width = 8, font = "none 12 bold").grid(row = 0, column = 4)
    tkinter.messagebox.showinfo("Welcome to diamonds", "Choose the deck of cards you wanna play with...\nFor more info about the game, go to HELP\nClick OK to start the game.")
    
    Player_name = Ask_player_name()
    tk.mainloop()
#First_page()
Second_page()
