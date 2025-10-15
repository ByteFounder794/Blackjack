def blackjack():

    print("Welcome to blackjack")
    print("Would you like to play blackjack?")
    user_response = input().lower()

    if user_response == "yes":
        print("lets play blackjack")
    elif user_response == "no":
        print("Thank you for playing")

blackjack()
