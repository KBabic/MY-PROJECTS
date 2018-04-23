# poruka dobrodoslice

# While True petlja koja ce pokretati igru - iz petlje uvek treba da postoji izlaz

    # potrebno je pripremiti sve za pocetak igre: 
    # prikazati praznu tablu, 
    # dodeliti markere X i O igracima i 
    # odrediti ko ce prvi
    # kada su pripreme gotove, treba ih pitati jesu li spremni
    # ako su spremni, igra moze da pocne --> dobro je postaviti boolean koji ce voditi racuna o tome da li igra traje ili ne
    
        # Igrac 1 prvi bira poziciju za svoj marker
    
            # prvo se proverava da li je izabrao validnu poziciju
            # ako je validna, proverava se da li je zeljena pozicija slobodna
            # ako nije validna ili nije slobodna, trazi se da izabere ponovo dok ne bude validna ili slobodna
            # kada se marker postavi na poziciju, proverava se da li je ostvario pobedu
            # ako je pobedio, prekida se igra --> boolean na False
            # ako nije ostvario pobedu, proverava se da li je igra neresena
            # ako je nereseno, prekida se igra --> boolean na False
            # ako nije pobedio i nije nereseno, igrac 2 je na potezu
        
        # Igrac 2 bira poziciju i sve je isto kao kod Igraca 1

# ako ne zele da igraju ponovo, igra se definitivno zavrsava

from IPython.display import clear_output
import random

# ovom f-jom se definise kako tabla treba da izgleda
def display_board(board):
    clear_output()
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3]+' ')
    print('---'+'|'+'---'+'|'+'---')
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6]+' ')
    print('---'+'|'+'---'+'|'+'---')
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9]+' ')

# ovom f-jom se definise koji je ciji marker
# njen output je tuple ciji je prvi element marker za prvog igraca, a drugi element marker za drugog igraca
def player_input():
    
    marker = ''
    
    while not(marker.upper() == 'X' or marker.upper() =='O'):
        marker = input('Player 1, please choose X or O: ')
    
    if marker.upper() == 'X':
        (player1, player2) = ('X','O')
    else:
        (player1, player2) = ('O','X')
    return (player1, player2)

# ovom f-jom odredjuje se ko ce prvi da igra:

def choose_first():
    first = random.randint(1,2)
    if first == 1:
        return 'Player 1'
    else:
        return 'Player 2'

# ovom f-jom proverava se da li je pozicija slobodna:

def space_check(board, position):
    return board[position] == ' '

# ovom f-jom igrac 1 bira svoju poziciju:

def player_choice(board):
    
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Please choose your position from 1 to 9: '))
    return position

# ovom f-jom marker se postavlja na zeljenu poziciju
# rezultat ove f-je treba da bude azurirana tabla

def place_marker(board, marker, position):
    
    board[position] = marker    

# ovom f-jom proverava se da li je neko pobedio:

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

# ovom f-jom proverava se da li je igra neresena (tabla puna a niko nije pobedio):

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# na kraju je ostala f-ja koja proverava da li zele ponovo da igraju:

def replay():
    return input('Would you like to play again? ').lower()[0] == 'y'

# sada sklapamo celinu:

print ('Welcome to Tic Tac Toe Game!')

while True:
    
    the_board = [' ']*10
    player1_mark, player2_mark = player_input()
    print(f'Player 1 is {player1_mark}, Player 2 is {player2_mark}')
    turn = choose_first()
    print(turn + ' will play first')
    
    play_game = input('Are you ready to start the game? Yes or No')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_mark, position)
            
            if win_check(the_board, player1_mark):
                display_board(the_board)
                print('Congratulations, Player 1! You won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('This game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_mark, position)
            
            if win_check(the_board, player2_mark):
                display_board(the_board)
                print('Congratulations, Player 2! You won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('This game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break








