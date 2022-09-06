import random
from tinge import colored

target = random.randint(1,100)

retries = 0
answered = False


print (colored("\n\n\tWelcome to The Number Guessing Game!!\n", "blue"))
print (colored("\tThe number you have to guess lies between 0 and 100\n", "blue"))
print (colored("\tYou only get 10 tries, so think Carefully :)\n", "blue"))
print (colored("\tEnter your guess to start the game\n", "blue"))

while (retries < 10):

    choice = int(input("\nEnter your guess: "))
    retries +=1

    if target != choice:

        if retries == 10:
            if target == choice:
                print ("\n\tYou guessed the correct number!!")
                print ("\n\tIt took you {} tries".format(retries))
                answered = True
                break;
            else:
                break;

        else:
            print (colored("\n\tWrong Guess!!","red"))
            if target > choice:
                
                print ("\n\tThe Number is greater than {}".format(choice))

            else:
                print ("\n\tThe Number is Smaller than {}".format(choice))
        print ("\n\tChances remaining: {}".format (10-retries))

    else:
        print (colored("\n\tYou guessed the correct number!!","green"))
        print ("\n\tIt took you {} tries".format(retries))
        answered = True

        break;


if answered == False:
    print (colored("\n\tOut of chances, You couldn't even guess a number :<", "red"))
    print ("\n\tThe Correct Answer is {}".format(target))
    print ("\n\tBetter luck next time :)")


    


    
