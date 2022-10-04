def start():
    answer = "dog"
    guess_count = 0
    guess_limit = 3
    
    print("You have 3 chances to guess the animal I am thinking of")
    
    while guess_count < guess_limit:
        guess = input("Guess an animal: ").lower()
        guess_count += 1
        if guess == answer:
            print("You win!")
            break
        elif guess == quit:
            break
        else:
            print("That is incorrect. Try again")

    return None 

start()