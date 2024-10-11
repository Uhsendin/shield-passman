class Menu:

    def menuRun(self):

        print("Welcome to Sheild Passman!")
        isProgramRunning = True
        while isProgramRunning:
            print("Menu:")
            print("1. Create a new password vault")
            print("2. Exit the Program")
            option = input("Choose (1, or 2): ")

            if option.lower() == "2":
                print("Goodbye!")
                isProgramRunning = False

            elif option.lower() == "1":
                print("You are in password vault")

            else:
                print(f"Please choose a valid option.")