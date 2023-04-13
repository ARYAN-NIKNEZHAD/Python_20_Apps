import  functions
import PySimpleGUI as Psg

label = Psg.Text("Type in a to-do")
input_box = Psg.InputText(tooltip="Enter todo", key="todo")
add_button = Psg.Button("Add")
window = Psg.Window("My To-do App",
                    layout=[[label], [input_box], [add_button]],
                    font=("Helvetica", 20))
event = window.read()
print(event)

window.close()


