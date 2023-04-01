from random import randint

def player_choice(option_list):
    print('Take your choice..')
    for index, value in enumerate(option_list):
        print(f'{index} {value}')
    index_choice = int(input())
    return option_list[index_choice]
    
def computer_choice(option_list):
    index_choice = randint(0, 2)
    return option_list[index_choice]

def check_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'Draw!'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'scissors' and computer_choice == 'paper') or (player_choice == 'paper' and computer_choice == 'rock'):
        return 'Player won!'
    else:
        return 'Computer won!'

def play():
    game_options = ['rock', 'paper', 'scissors']
    player_option = player_choice(game_options)
    computer_option = computer_choice(game_options)
    print(f'''
Player choice is {player_option}
Computer choice is {computer_option} 
Result: {check_result(player_option, computer_option)}
''')

def main():
    print('Hello! Welcome to the Rock, paper, scissors!') 
    play_again = ''
    while play_again.lower() != 'n':
        play()
        print('''Do you want play again?
click y - 'yes' or n - 'no' ''')
        play_again = input()

main()