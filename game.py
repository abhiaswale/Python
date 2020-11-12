numb = int(input("guess a number :"))
win=45
guess = 1
game = False
while not game:

    if numb == win:
        print(f"You Win you guessed it in {guess}")
        game = True
    else:  
        if numb >= win:
            print("number too high")
            guess += 1
            numb=int(input("Guess again"))
        else:
            print("number too low")        
            numb=int(input("Guess again"))
            guess +=1
