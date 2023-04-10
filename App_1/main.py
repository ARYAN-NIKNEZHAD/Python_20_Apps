while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("files/todos", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("files/todos", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        with open("files/todos", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            print(f"{index + 1} - {item}")
    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        with open("files/todos", "r") as file:
            todos = file.readlines()
        new_todo = input("Enter new todo: ")

        todos[number] = new_todo + "\n"
        with open("files/todos", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open("files/todos", "r") as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("files/todos", "w") as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list !"
        print(message)

    elif "exit" in user_action:
        break
    else:
        print("The command that you enter is not valid!!")

print("Bye!")
