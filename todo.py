from functions import get_todo, write_todo
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_input = input("select any one add, edit, show, complete or exit: ")
    final_input = user_input.strip().lower()


    if final_input.startswith('add'):
        todo = final_input[4:].title()

        todos = get_todo()
        todos.append(todo + '\n')

        write_todo(todos)


    elif final_input.startswith('show'):
        todos = get_todo()

        for index, items in enumerate(todos):
            items = items.strip('\n')
            print(f"{index + 1} - {items}")


    elif final_input.startswith('edit'):
        try:
            number = int(final_input[5:])
            f_number = number - 1

            todos = get_todo()

            edit_input = input("Enter the new todo: ")
            todos[f_number] = edit_input.title() + '\n'

            write_todo(todos)

        except ValueError:
            print("You entered something wrong")
            continue


    elif final_input.startswith('complete'):
        try:
            number = int(final_input[9:])
            todos = get_todo()
            final_input = number - 1
            todo_to_remove = todos[final_input].strip('\n')
            remove = todos.pop(final_input)
            write_todo(todos)
        except IndexError:
            print("This number does not exist...")
            continue


    elif final_input.startswith('exit'):
        break


    else:
        print("You entered something wrong")
print("Byeee..........")

