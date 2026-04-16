import random as rand

def guess_game(m_chances):
    
    secret = rand.randint(1, 20)
    chances = 1
    
    print(f"Let's start! You've {m_chances} chances.")
    
    while(chances <= m_chances):
        num = int(input("Enter your guess: "))
        if(num == secret):
            print(f"Congratulations! You guessed the secret number in {chances} attempts")
            break
        elif(num < secret):
            print(f"Incorrect! The number is higher than {num}")
        else:
            print(f"Incorrect! The number is lower than {num}")
        chances += 1
    print(f"Game Over! The number was {secret}.")
    return False

while(True):
    print("Welcome to the - GUESS THE NUMBER - game")
    print("\nDIFFICULTY")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("0. Exit")
    opt = int(input("Enter the difficulty: "))

    if(opt == 0):
        print("Leaving...")
        break
    elif(opt == 1):
        max = 10
    elif(opt == 2):
        max = 5
    elif(opt == 3):
        max = 3
    else:
        print("Incorrect option")
        continue
    
    guess_game(max)

    keep = input("Wanna play again? (Y/N): ").upper()
    if keep != "Y":
        print("Quitting...")
        break