import random as rd

cards = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
         '9': '9', '10': 'X', '11': 'J', '12': 'Q', '13': 'K', '11': 'A'}
cards_keys = list(cards.keys())
mängu_status = True
winner = None

def print_card_user(display_kaart_arr):
    total_cards = len(display_kaart_arr)
    for idx in range(total_cards):
        print('______________', end = '   ')
    print('\n')
    for idx in range(total_cards):
        print('|%s           |' % cards[display_kaart_arr[idx]], end = '   ') 
    print('\n')
    for idx in range(total_cards):
        print('|            |', end = '   ')
    print('\n')
    for idx in range(total_cards):
        print('|            |', end = '   ')
    print('\n')
    for idx in range(total_cards):
        print('|           %s|' % cards[display_kaart_arr[idx]], end = '   ')
    print('\n')
    for idx in range(total_cards):
        print('--------------', end = '   ')
    print('\n')
    
def win_determine(Inimese_kaarti_list, Arvuti_kaarti_list):
    global winner
    Inimese_kaarti_list = [int(i) for i in Inimese_kaarti_list]
    Arvuti_kaarti_list = [int(i) for i in Arvuti_kaarti_list]
    if sum(Inimese_kaarti_list) == 21:
        winner = 'Player'
    if sum(Arvuti_kaarti_list) == 21:
        winner = 'Computer'
    if sum(Inimese_kaarti_list) > 21:
        winner = 'Computer'
    if sum(Arvuti_kaarti_list) > 21:
        winner = 'Player'
    if sum(Inimese_kaarti_list) + sum(Arvuti_kaarti_list) < 42:
        if sum(Inimese_kaarti_list) > sum(Arvuti_kaarti_list):
            winner = 'Player'
        if sum(Inimese_kaarti_list) < sum(Arvuti_kaarti_list):
            winner = 'Computer'
    if sum(Inimese_kaarti_list) == sum(Arvuti_kaarti_list):
        winner = 'Drew'

def reshuffle(Inimese_kaartid, Arvuti_kaartid):
    Inimese_kaartid = [int(i) for i in Inimese_kaartid]
    Arvuti_kaartid = [int(i) for i in Arvuti_kaartid]
    if sum(Inimese_kaartid) > 21:
        play()
    if sum(Arvuti_kaartid) > 21:
        play()
    if sum(Inimese_kaartid) == 21:
        print('Player Wins - Blackjack')
    if sum(Arvuti_kaartid) == 21:
        print('Arvuti Wins - Blackjack')

def computer_move(Arvuti_kaartid):
    cards = [int(i) for i in Arvuti_kaartid]
    if 21 - sum(cards) <= 4:
        print('\nComputer Chose to Stand')
    else:
        Arvuti_kaartid.append(cards_keys[rd.randint(0, 12)])

def play():
    global mängu_status, winner
    inimese_kaartid = []
    Arvuti_kaartid = []
    for _ in range(2):
        inimese_kaartid.append(cards_keys[rd.randint(0, 12)])
        Arvuti_kaartid.append(cards_keys[rd.randint(0, 12)])
    reshuffle(inimese_kaartid, Arvuti_kaartid)
    print("Player Current Cards:\n")
    print_card_user(inimese_kaartid)
    while mängu_status == True:
        if winner == None:
            computer_move(Arvuti_kaartid)
            Arvuti_valib = input("""Hit or Stand?""")
            if Arvuti_valib.lower() == 'hit':
                inimese_kaartid.append(cards_keys[rd.randint(0, 12)])
                print(inimese_kaartid)
                print_card_user(inimese_kaartid)
            if Arvuti_valib.lower() == 'stand':
                win_determine(inimese_kaartid, Arvuti_kaartid)
                print("\nThe Winner is: %s" % winner)
                print("Arvuti kaartid:")
                print_card_user(Arvuti_kaartid)
                print(sum([int(i) for i in inimese_kaartid]), '-', sum([int(i) for i in Arvuti_kaartid]))
                quit()
play()