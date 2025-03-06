import random
n=random.randint(1,100)
a=-1
guesses = 1
while (a!=n):
    a=int(input("Guess the number : "))
    if (a>n):
        print("LOWER NUMBER PLEASE")
        guesses +=1                 

    elif (a<n):
        print("HEIGHER NUMBER PLEASE")
        guesses +=1                 

print(f"Congratulations !! you have guessed the number {n} correctly in  {guesses} attempt")

