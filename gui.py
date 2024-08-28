import functions
import FreeSimpleGUI as sg
import time


sg.theme("DarkGreen")
clock = sg.Text('', key='clock', font=("Times New Roman",12))
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))

add_button = sg.Button("Add", size=(10,1))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


#  widgets
window = sg.Window("My To-Do App", layout=[[clock],[label], [input_box,add_button],
                                            [list_box, edit_button, complete_button],
                                            [exit_button]], font=("Helvetica", 12))

while True:
    event, values = window.read(timeout=100)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.updated_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.updated_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font= ("Helvetica",13))
            except ValueError:
                sg.popup("Please input a new todo after selecting an item from the list, then press edit.", font=("Helvetica", 13))
                selected_todo = values['todos'][0].strip('\n')
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                #todos.remove(todo_to_complete)
                functions.updated_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font= ("Helvetica",13))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break
    #updating time caused an error where closing the window was generating an type.update error
    #placing the line at the end of match-case solved it.
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

window.close()