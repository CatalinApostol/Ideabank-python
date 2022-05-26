import sys




# Personal Idea Bank
# The program starts with greeting message + input help button for the main menu
print("Hello and welcome to your personal Idea Bank where all your ideas can be stored for later usage, or deleted forever if not needed anymore")
print("Please use help to see all the options available")

# The idea bank instructions for main menu + loop 

command = ""
writing = False

def menu():
    while True:
        command = input("> ")
        if command == "help":
            print(""" 
    ################ Main Menu #################   
    #                                          #
    # Use --write to start writing your ideas  #
    # Use --list to list your ideas            #
    # use --delete to remove unwanted ideas    #
    # use --quit to quit                       #
    #                                          #
    ############################################    
        """)

        # This command gets user to write his/her ideas and list them + usage of Ctrl+C command wich gets the user back to the main menu!
        elif command == "--write":
            while True:
                try:
                    with open("idea_bank.txt", "a") as idea_bank:
                        idea = input("What is your new idea?(CTRL + C if you don't have any idea to write): ")
                        idea_bank.write(idea + "\n")
                        idea_bank.close()
                    with open("idea_bank.txt", "r") as idea_bank:
                        for i, line in enumerate(idea_bank):
                            print('{}.{}'.format(i+1, line.strip()))
                        idea_bank.close()
                except KeyboardInterrupt:
                    print("Welcome back to main menu")
                    return menu()                        


        # This command gets user to see his/her ideas then back to the main menu selection  
        elif command == "--list":
            with open("idea_bank.txt", "r") as idea_bank:
                for i, line in enumerate(idea_bank):
                    print('{}.{}'.format(i+1, line.strip()))
                idea_bank.close()

        
        #This command gets user to see his/her ideas then gives the posibility to delete them by writing it's line number.
        elif command == "--delete":
            while True:
                try:
                    user_input = input("Idea to be removed?: ")
                    with open('idea_bank.txt', 'r') as file_r:
                        lines = list(file_r)
                        line_del = lines[int(user_input) - 1]
                        with open('idea_bank.txt', 'w') as file_w:
                            for line in lines:
                                if line != line_del:
                                    file_w.write(line)
                except KeyboardInterrupt:
                    print("Welcome back to main menu")
                    return menu()


        #This command terminates the program.  
        elif command == "--quit":
            sys.exit("Have a really nice day!")
            break
        #This message occurs when user inputs unknows command by the program.
        else:
            print("Sorry, I don't Understand that!:")
        

           
menu()