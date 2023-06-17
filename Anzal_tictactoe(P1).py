
# This function includes the entire game and the game is started whenever we call this function
def tictactoe_game():
    print('Lets start the  TICTACTOE game \n')
    player_1 = str(input('Enter the first player name:  \n')).upper()
    player_2 = str(input('Enter the second player name:  \n')).upper()
    print(f'X for {player_1}, O for {player_2}')
    
    # creating the pattern used in the game
    def tictactoe_pattern(value):  
        print(' _ _ _ _ _ _')
        print(f"|_{value[0]}_|_{value[1]}_|_{value[2]}_|")   
        print(' _ _ _ _ _ _')
        print(f"|_{value[3]}_|_{value[4]}_|_{value[5]}_|")        
        print(' _ _ _ _ _ _')
        print(f"|_{value[6]}_|_{value[7]}_|_{value[8]}_|")   

    #list without any X or O value
    value = ['_' for i in range(9)]
    tictactoe_pattern(value)
    #this is a list with includes all possible winning combinations of the slots
    winning_list =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    #dictionary is created for storing all slots entered in respective X and O keys
    taken_slots = {'X':[],'O':[]}
    current_player = player_1
    # in this function, the number we entered as a slot will turn to corresponding  element(X or O) in pattern
    def values_in_pattern():
        for items in range(len(value)):
            if items+1 in taken_slots['X']:
                value[items]='X'
            elif items+1 in taken_slots['O']:
                value[items]='O'
    #condition for winning the game
    def for_win_condition():
        for i in winning_list:
                check_for_X = all( item in taken_slots['X'] for item in i)
                if check_for_X == True:
                    print(f'{current_player} has won the match')
                check_for_O = all( item in taken_slots['O'] for item in i)
                if check_for_O == True:
                    print(f'{current_player} has won the match')
                if check_for_O or check_for_X == True:
                    return True
    #condition for the tie            
    def for_tie_condition():
        if len(taken_slots['X'])+len(taken_slots['O']) == 9:
            print('Its a TIE')
            return True
                    

    # run in a loop till the game ends
    while True:
        # exception method for strictly choosing the number in between 1 to 9
        try:
            slot =int(input(f'enter the slot for {current_player}: \n'))
        # avoid value error      
        except ValueError:
            print('invalid input, enter a valid number')
            continue
        if slot<1 or slot>9:
            print('invalid input, enter a valid number')
            continue
        if value[slot-1]!='_':
            print('sorry, slot already taken')
            continue
        if current_player == player_1:
            taken_slots['X'].append(slot)
        if current_player == player_2:
            taken_slots['O'].append(slot)
            
        values_in_pattern()
        tictactoe_pattern(value)
        if for_win_condition() == True:
            break 
        if for_tie_condition()== True:
            break   
        if current_player == player_1:
            current_player = player_2
        elif current_player == player_2:
            current_player = player_1
            continue
   

tictactoe_game()
print('Game over \n')
#for quiting or restarting game
while True:
    print('enter 1 for restarting the game \n')
    print('enter any other number for quitting  the game \n')
    try:
        n = int(input('please enter the number: '))
    except ValueError:
        print('enter a valid input')
        continue
    if n == 1:
        tictactoe_game()
        continue
    else:
        print('THANK YOU!!!!!!!')
        break
   


    
    
   