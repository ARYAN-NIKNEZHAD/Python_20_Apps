import  functions
import PySimpleGUI as Psg

label = Psg.Text("Type in a to-do")
input_box = Psg.InputText(tooltip="Enter todo", key="todo")
add_button = Psg.Button("Add")

list_box = Psg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = Psg.Button("Edit")
window = Psg.Window("My To-do App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=("Helvetica", 20))

while True:

    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case Psg.WIN_CLOSED:
            break

window.close()


