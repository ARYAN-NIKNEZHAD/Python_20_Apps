import  functions
import PySimpleGUI as Psg

label = Psg.Text("Type in a to-do")
input_box = Psg.InputText(tooltip="Enter todo", key="todo")
add_button = Psg.Button("Add")
window = Psg.Window("My To-do App",
                    layout=[[label], [input_box], [add_button]],
                    font=("Helvetica", 20))

while True:

    event, value = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case Psg.WIN_CLOSED:
            break

window.close()


