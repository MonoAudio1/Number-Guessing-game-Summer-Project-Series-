#number Guessing game
#imports
import math as math
import random as random
#varible for number of guesses

NumGuesses=int(input("How many guesses would you like? "))


LL=int(input("Enter the lowest limit for guess range: "))

print("Guessing from (Low limit) to (high limit) ")
HL=int(input("Enter the highest limit for the guess range: "))

CG= random.randint(LL,HL)
print("Guess range is from",LL,"to",HL)

def play():        
    Guess=int(input("Guess the number I am thinking: "))
    if Guess>HL:
        print("Guess is TOO HIGH")
    elif Guess<LL:
        print("Guess is TOO LOW")
    elif Guess>CG:
         print("Guess lower")
    else:
        print("guess higher")

#variable for computer number
# generates a number in the range set by numbers

Start=False


StartQ=input("Ready to start the game?(Y/N) ")
if StartQ=="y" or "Y" or "Yes":
    Start=True
    if Start==True:
        while Start==True:
            for i in range(NumGuesses):
                play()
                NumGuesses=NumGuesses-1
                print("Guesses left",NumGuesses)
                if NumGuesses==0:
                    print("Out of guesses")
            
        
elif StartQ=="n" or "N" or "No":
    print("Ok, why are you playing?")
else:
    print("Restart with valid input")
            
    