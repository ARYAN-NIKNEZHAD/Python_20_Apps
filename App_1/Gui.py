import  functions
import PySimpleGUI as Psg

label = Psg.Text("Type in a to-do")
input_box = Psg.InputText(tooltip="Enter todo")
add_button = Psg.Button("Add")
window = Psg.Window("My To-do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()


