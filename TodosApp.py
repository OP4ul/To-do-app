from functions import get_todos, updated_todos

while True:
    user_input = input("Type add,show,edit,complete or exit: ")
    user_input.strip()

    if user_input.startswith("add"):
        try:
            todo = user_input[4:]
            todos = get_todos()
            todos.append(todo + '\n')
            updated_todos(todos)
        except ValueError:
            print("Enter a valid command")
            continue

    elif user_input.startswith("show"):
        try:
            todos = get_todos()

            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        except ValueError:
            print("Enter a valid command")
            continue

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:]) - 1
            new_todo = input("Enter your new todo: ")
            todos = get_todos()
            todos[number] = new_todo.strip() + "\n"
            updated_todos(todos)

        except ValueError:
            print("Your command isn't valid")
            continue
    elif user_input.startswith("complete"):
        try:
            number = int(user_input[8:]) - 1
            todos = get_todos()
            todos_to_remove = todos[number].strip('\n')
            todos.pop(number)
            updated_todos(todos)
            message = f"{todos_to_remove} is removed from the list"
            print(message)
        except ValueError:
            print("Enter a valid command")
            continue
    elif user_input.startswith("exit"):
        break
    else:
        print("Command not valid")

print("Bye!")



