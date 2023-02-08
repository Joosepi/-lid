import random as rd

cards = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
         '9': '9', '10': 'X', '11': 'J', '12': 'Q', '13': 'K', '11': 'A'}
cards_keys = list(cards.keys())
mängu_status = True
winner = None

def print_card_user(display_cards_arr):
    total_cards = len(display_cards_arr)
    for idx in range(total_cards):
        print('______________', end = '   ')
    print('\n')
    for idx in range(total_cards):
        print('|%s           |' % cards[display_cards_arr[idx]], end = '   ') 
    print('\n')
    for idx in range(total_cards):
        print('|            |', end = '   ')
    print('\n')
    for idx in range(total_cards):
        print('|            |', end = '   ')
    print('\n')
    for idx in range(total_cards):
        print('|           %s|' % cards[display_cards_arr[idx]], end = '   ')
    print('\n')
    for idx in range(total_cards):
        print('--------------', end = '   ')
    print('\n')
    
def win_determine(Persons_card_list, Computer_card_list):
    global winner
    Persons_card_list = [int(i) for i in Persons_card_list]
    Computer_card_list = [int(i) for i in Persons_card_list]
    if sum(Persons_card_list) == 21:
        winner = 'Player'
    if sum(Computer_card_list) == 21:
        winner = 'Computer'
    if sum(Persons_card_list) > 21:
        winner = 'Computer'
    if sum(Computer_card_list) > 21:
        winner = 'Player'
    if sum(Persons_card_list) + sum(Computer_card_list) < 42:
        if sum(Persons_card_list) > sum(Computer_card_list):
            winner = 'Player'
        if sum(Persons_card_list) < sum(Computer_card_list):
            winner = 'Computer'
    if sum(Persons_card_list) == sum(Computer_card_list):
        winner = 'Drew'

def reshuffle(Persons_cards, Computer_cards):
    Persons_cards = [int(i) for i in Persons_cards]
    Computer_cards = [int(i) for i in Computer_cards]
    if sum(Persons_cards) > 21:
        play()
    if sum(Computer_cards) > 21:
        play()
    if sum(Persons_cards) == 21:
        print('Player Wins - Blackjack')
    if sum(Computer_cards) == 21:
        print('Arvuti Wins - Blackjack')

def computer_move(Computer_cards):
    cards = [int(i) for i in Computer_cards]
    if 21 - sum(cards) <= 4:
        print('\nComputer Chose to Stand')
    else:
        Computer_cards.append(cards_keys[rd.randint(0, 12)])

def play():
    global mängu_status, winner
    Persons_cards = []
    Computer_cards = []
    for _ in range(2):
        Persons_cards.append(cards_keys[rd.randint(0, 12)])
        Computer_cards.append(cards_keys[rd.randint(0, 12)])
    reshuffle(Persons_cards, Computer_cards)
    print("Player Current Cards:\n")
    print_card_user(Persons_cards)
    while mängu_status == True:
        if winner == None:
            computer_move(Computer_cards)
            computer_chooses = input("""Hit or Stand?""")
            if computer_chooses.lower() == 'hit':
                Persons_cards.append(cards_keys[rd.randint(0, 12)])
                print(Persons_cards)
                print_card_user(Persons_cards)
            if computer_chooses.lower() == 'stand':
                win_determine(Persons_cards, Computer_cards)
                print("\nThe Winner is: %s" % winner)
                print("Arvuti kaartid:")
                print_card_user(Computer_cards)
                print(sum([int(i) for i in Persons_cards]), '-', sum([int(i) for i in Computer_cards]))
                quit()
play()