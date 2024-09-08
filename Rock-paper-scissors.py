import random
start = input('You have started the game rock-scissors-paper. Would you like to play? (Enter "+" or "-"): ')

if start == '+':
    print(f'\nIf you want to finish, enter "-"')
    print(f'If you want to know the score, enter "s".\n')

    player_ball = 0
    computer_ball = 0
    
    while True:
        user = input("Enter rock, paper or scissors? ")
        list_play = ['rock', 'scissors', 'paper']
        
        if user in list_play:
            rand = random.choice(list_play)
            print(f"Opponent's move: {rand}")
            
            if rand == 'rock' and user == 'scissors':
                print(f'The computer won :( \n')
                computer_ball += 1
            elif rand == 'rock' and user == 'paper':
                print(f'You win!!!\n')
                player_ball += 1
            elif rand == 'scissors' and user == 'rock':
                print(f'You win!!!\n')
                player_ball += 1
            elif rand == 'scissors' and user == 'paper':
                print(f'The computer won :( \n')
                computer_ball += 1
            elif rand == 'paper' and user == 'scissors':
                print(f'You win!!!\n')
                player_ball += 1
            elif rand == 'paper' and user == 'rock':
                print(f'The computer won :( \n')
                computer_ball += 1
            elif rand == user:
                print(f'You have a tie!\n')
        elif user == 's':
            print(f'Your points: {player_ball}. Computer points: {computer_ball}\n')
        elif user == '-':
            print(f'\nYour points: {player_ball}. Computer points: {computer_ball}')
            print(f'Come back again!\n')
            break

