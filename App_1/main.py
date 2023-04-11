def get_todos(file_path):
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("files/todos")

        todos.append(todo + "\n")

        with open("files/todos", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        todos = get_todos("files/todos")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            print(f"{index + 1} - {item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("files/todos")
            new_todo = input("Enter new todo: ")

            todos[number] = new_todo + "\n"
            with open("files/todos", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("files/path")

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("files/todos", "w") as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list !"
            print(message)
        except IndexError:
            print("There is not item with that number.")
            continue

    elif "exit" in user_action:
        break
    else:
        print("The command that you enter is not valid!!")

print("Bye!")
