def blackjack():

    print("Welcome to Blackjack")
    print("Would you like to play Blackjack?")
    user_response = input().lower()

    if user_response == "yes":
        print("lets play Blackjack")
    elif user_response == "no":
        print("Thank you for playing")

blackjack()