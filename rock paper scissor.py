import sys,random
win = 0
loss = 0
ties = 0
q= quit
while True:
    while True:
        print(" pls choose q-quit or p-paper or s-scissor or r-rock")
        choice=input()
        if choice==q:
            sys.exit()
        if choice=='p' or choice=='r' or choice=='s':
            break
    print("The user choice is ",choice)

#display the computer choice
    com_choice=random.randint(1,3)
    if com_choice==1:
        com_move='r'
        print("Computer choice is rock")
    elif com_choice==2:
        com_move='p'
        print("Computer choice is paper")
    else:
        com_move='s'
        print("Computer choice is scissor")

#display and record the wins or ties or loss
    if choice==com_move:
        print("It is tie")
        ties=ties+1
    elif(choice=='r')and(com_move=='s'):
        print("user wins")
        win=win+1
    elif(choice=='r')and(com_move=='p'):
        print("user win")
        win=win+1
    elif(choice=='s')and(com_move=='p'):
        print("user wins")
        win=win+1
    elif(choice=='s')and(com_move=='r'):
        print("user loss")
        loss=loss+1
    elif(choice=='p')and(com_move=='r'):
        print("user loss")
        loss=loss+1
    elif(choice=='p')and(com_move=='s'):
        print("user loss")
        loss=loss+1
    print('win='+str(win)+'loss='+str(loss)+'tie = ' + str(ties))

