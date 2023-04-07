todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            file = open("todos", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos", "w")
            file.writelines(todos)
            file.close()

        case "show":
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index + 1} - {item}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")

            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case "exit":
            break

print("Bye!")
