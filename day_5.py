
# edit feature added
todo = []
while True:
    userAction = input("Type add, show, edit, delete or exit -")
    userAction = userAction.strip().lower()
    # strip for removing all the whitespace and lower for convert all the char to lowercase
    match userAction:
        case 'add':
            uInput = input("Enter a Todo - ")
            todo.append(uInput)
        case 'show':
            print("************* TO DO List ***********\n")
            for counter, i in enumerate(todo):
                i = i.title() # make all the word in title format
                print(f"{counter+1}. {i} ")
        case 'exit':
            break
        case 'edit':
            number = int(input("Enter the number of the todo from list(i.e. 1) - "))
            print(todo[number-1].title())
            todo.__setitem__(number-1, input(f"Enter new Todo_{number} - "))
        case 'delete':
            number = int(input("Enter the number of the todo to delete (i.e. 1) - "))
            todo.pop(number-1)
        case whatever:
            print("You have enter unknown command !!")
print("Program exit. Bye !")