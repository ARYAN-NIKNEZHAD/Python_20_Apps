import functions
import PySimpleGUI as Psg
import time
import os

if not os.path.exists("todos"):
    with open("todos", "w") as file:
        pass


Psg.theme("Black")
clock = Psg.Text("", key="clock")
label = Psg.Text("Type in a to-do")
input_box = Psg.InputText(tooltip="Enter todo", key="todo")
add_button = Psg.Button("Add", size=10)

list_box = Psg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=(45, 10))
edit_button = Psg.Button("Edit")
complete_button = Psg.Button("Complete")
exit_button = Psg.Button("Exit")
window = Psg.Window("My To-do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 20))

while True:

    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b, %d, %Y, %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                Psg.popup("Please select an item first!", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                Psg.popup("Please select an item first!", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case Psg.WIN_CLOSED:
            break

window.close()
