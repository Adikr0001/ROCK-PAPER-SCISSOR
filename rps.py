import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
while True:
    print('Enter your choice : 1 for rock , 2 for paper , 3 for scissor')
    choice = int(input('Enter your choice:'))
    while choice > 3 or choice < 1:
        print("Enter a valid choice")
    if choice==1:
        print("Rock")
    elif choice==2:
        print("Paper")
    else:
        print("Scissor") 

    print("User's choice is:",choice)
    print("wait for computer to play")


     comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1,3)
 
    if comp_choice==1:
        print("Rock")
    elif comp_choice==2:
        print("Paper")
    else:
        print("Scissor") 

   

    print("Computer's choice is:", comp_choice)
    
    if choice==comp_choice:
        print("Its a draw")
    elif (choice==1 and comp_choice==2):
        print("Computer wins")
    elif (choice==3 and comp_choice==1):
        print("Computer wins")
    elif (choice==2 and comp_choice==3):
        print("Computer wins")
    else:
        print("User wins")

print("THANKS FOR PLAYING")
