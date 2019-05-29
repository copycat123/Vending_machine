sodas = ["pepsi", "cherry coke", "sprite"]
chips = ["Doritos", "chetoz"]
candy = ["Snickers", "M&M", "Twizz"]

while True:
    choice = input("Would you like a SODAS, some CHIPS , or a CANDY? ").lower()
    try:

        if choice == "sodas":
            snack = sodas.pop()
        elif choice == "chips":
            snack = chips.pop()
        elif choice == "candy":
            snack = candy.pop()

        else:
            print("Sorry i didn't understand that.")
            continue
    except IndexError:
        print("Sorry all out of {}".format(choice))
    else:
        print("Here is your {}: {}".format(choice, snack))


'make further changes into file'
