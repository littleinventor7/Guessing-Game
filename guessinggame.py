import random
def computerGuess(lowval,highval,randnum,count=0):
    if highval>=lowval:
        guess = lowval +(highval - lowval) // 2
        if guess == randnum:
            return count
        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1,randnum,count)
        else:
            count = count + 1
            return computerGuess(guess+1, highval,randnum,count)
    else :
        return -1

def level1():
    print("This is the Guessing Game")
    print("Let's start by LEVEL 1")
    randnum= random.randint(1,101)

    count = 0
    guess = -99
    while (guess != randnum ):
        guess = (int)(input("Enter your guess between 1 and 100 : "))
        if guess < randnum :
            print("Higher")
        elif guess > randnum :
            print("Lower")  
        else :
            print("You guessed it!")   
            break
        count= count + 1

    print("YOU took " + str(count)+" steps to guess the number")
    print("COMPUTER took " + str(computerGuess(0, 100,randnum)) + " steps to guess the number")
    print("Let's go LEVEL 2")
def level2():
    
    randnum= random.randint(1,1001)

    count = 0
    guess = -99
    while (guess != randnum ):
        guess = (int)(input("Enter your guess between 1 and 1000 : "))
        if guess < randnum :
            print("Higher")
        elif guess > randnum :
            print("Lower")  
        else :
            print("You guessed it!")   
            break
        count= count + 1

    print("YOU took " + str(count)+" steps to guess the number")
    print("COMPUTER took " + str(computerGuess(0, 1000,randnum)) + " steps to guess the number")
    print("Let's go LEVEL 3")
def level3():

    randnum= random.randint(-1000,1001)

    count = 0
    guess = -1001
    while (guess != randnum ):
        guess = (int)(input("Enter your guess between -1000 and 1000 : "))
        if guess < randnum :
            print("Higher")
        elif guess > randnum :
            print("Lower")  
        else :
            print("You guessed it!")   
            break
        count= count + 1

    print("YOU took " + str(count)+" steps to guess the number")
    print("COMPUTER took " + str(computerGuess(-10001, 1000,randnum)) + " steps to guess the number")
    
def level4():

    randnum= random.randint(1,27)       
    guesschar = (str)("")
    count = 0
    guess = -1001
    while (guess != randnum ):
        guesschar = (str)(input("Enter your guess between A and Z (just capital) : "))
        if  guesschar == "A":
            guess = 1
        if  guesschar == "B":
            guess = 2
        if  guesschar == "C":
            guess = 3
        if  guesschar == "D":
            guess = 4
        if  guesschar == "E":
            guess = 5
        if  guesschar == "F":
            guess = 6
        if  guesschar == "G":
            guess = 7
        if  guesschar == "H":
            guess = 8
        if  guesschar == "I":
            guess = 9
        if  guesschar == "J":
            guess = 10
        if  guesschar == "K":
            guess = 11
        if  guesschar == "L":
            guess = 12
        if  guesschar == "M":
            guess = 13
        if  guesschar == "N":
            guess = 14
        if  guesschar == "O":
            guess = 15
        if  guesschar == "P":
            guess = 16
        if  guesschar == "Q":
            guess = 17    
        if  guesschar == "R":
            guess = 18    
        if  guesschar == "S":
            guess = 19    
        if  guesschar == "T":
            guess = 20    
        if  guesschar == "U":
            guess = 21    
        if  guesschar == "V":
            guess = 22    
        if  guesschar == "W":
            guess = 23   
        if  guesschar == "X":
            guess = 24
        if  guesschar == "Y":
            guess = 25 
        if  guesschar == "Z":
            guess = 26                                                                                                     
        if guess < randnum :
            print("Higher")
        elif guess > randnum :
            print("Lower")  
        else :
            print("You guessed it!")   
            break
        count= count + 1

    print("YOU took " + str(count)+" steps to guess the number")
    print("COMPUTER took " + str(computerGuess(0, 26,randnum)) + " steps to guess the number")
    print("CONGRATULATIONS YOU FINISH THE GAME!")
level1()
level2()
level3()
level4()
    
