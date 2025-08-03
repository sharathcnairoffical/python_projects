import random

emojis = {'r': '🪨', 's': '✂️', 'p': '📄'}
choices = ['r', 'p', 's']  # As list can be modififed in the code
choices = tuple(choices)

while True:
    user_choice = input('Rock , Paper, or Scissors ? (r/p/s): ').lower()
    if user_choice not in choices:
        print("Invalid Choice!!")
        continue

    computer_choice = random.choice(choices)

    print(f'You Chose {emojis[user_choice]}')
    print(f'Computer Chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!!')
    elif (((user_choice == 'r' and computer_choice == 's')
          or (user_choice == 's' and computer_choice == 'p'))
          or (user_choice == 'p' and computer_choice == 'r')):
        print('You Win!!')
    else:
        print('You lose!!')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue =='n':
        break
