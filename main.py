import random
n=random.randint(1,100)
a=-1
guesses = 0
while (a!=n):
    guesses +=1
    a=int(input("Guess the number : "))
    if (a>n):
        print("LOWER NUMBER PLEASE")
    else:
        print("HEIGHER NUMBER PLEASE")
        
print(f"Congratulations !! you have guessed the number correct {guesses} attempt")
