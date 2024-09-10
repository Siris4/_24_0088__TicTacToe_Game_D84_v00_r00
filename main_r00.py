import random
from random import randint

print("Welcome to Siris's Tic Tac Toe\n")

board_selection = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_board(board_selection):
    print(f" {board_selection[0]} | {board_selection[1]} | {board_selection[2]}")
    print("-----------")
    print(f" {board_selection[3]} | {board_selection[4]} | {board_selection[5]}")
    print("-----------")
    print(f" {board_selection[6]} | {board_selection[7]} | {board_selection[8]}")

print_board(board_selection)

print("\nA coin is flipped.")
coin_result = random.randint(0,1)
if coin_result == 0:
    print(f"\nThe coin landed on heads! The human goes first.")
    player_1st_choice = input("Please choose which number you want to place your O (between 1-9): ")
    print(f"You chose spot number: {player_1st_choice}")
    index_spot_chosen = int(player_1st_choice) - 1
    board_selection[index_spot_chosen] = 'O'
    print_board(board_selection)
else:
    print(f"\nThe coin landed on tails! 2nd player goes first.")
    print("The computer will place it's X on a spot.")
    computer_turn_1 = random.randint(1,10)
    print(f"The computer chose spot number: {computer_turn_1}")
    index_spot_chosen = int(computer_turn_1) - 1
    board_selection[index_spot_chosen] = 'X'
    print_board(board_selection)


index_spot_chosen = int(player_1st_choice) - 1 or int(computer_turn_1) - 1
print(f"The index chosen is: {index_spot_chosen}")
