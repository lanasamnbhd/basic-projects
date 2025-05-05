import logic

import logic

def print_matrix(mat):
    for row in mat:
        print(row)

# driver code
if __name__=='__main__':
    ...

#driver code
if __name__=='__main__':
    #calling start game function to initialize the matrix
    mat=logic.start_game()

while(True):
    #taking the user input for next step
    x=input("press the command: ")
    #we have to move up
    if(x=='W'or x=='w'):
        mat,flag=logic.move_up(mat)

        #get the current state and print it
        status=logic.get_current_state(mat)
        print(status)

        #if game not over then continue and add a new two
        if(status=='GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
    #to move down
    elif(x=='S' or x=='s'):
        mat,flag=logic.move_down(mat)
        status=logic.get_current_state(mat)
        print(status)
        if(status=='GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
    #to move left
    elif(x=='A' or x=='a'):
        mat,flag=logic.move_left(mat)
        status=logic.get_current_state(mat)
        print(status)
        if(status=='GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
    #to move right
    elif(x=='D' or x=='d'):
        mat,flag=logic.move_right(mat)
        status=logic.get_current_state(mat)
        print(status)
        if(status=='GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
    
    else:
        print("invalid key pressed")

    print_matrix(mat)

