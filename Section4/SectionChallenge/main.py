menu = "Please chose your option from the list below:\n" \
       "1) Learn Python\n" \
       "2) Learn Java\n" \
       "3) Go swimming\n" \
       "4) Have dinner\n" \
       "5) Go to sleep\n" \
       "0) exit\n"
choice = None
print(menu)
while choice != 0:
    choice = int(input("What do you want to do?: "))
    if choice == 0:
        print("Goodbye!")
        break
    elif choice > 5:
        print(menu)
    else:
        print("You chose option {}".format(choice))
