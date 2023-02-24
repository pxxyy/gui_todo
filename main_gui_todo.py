from function import get_todos, write_todos

while True:
    user_input = input('Type add, show, complete, edit or exit:')
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_input.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip()
            row = f'{index+1}. {item}'
            print(row)

    elif user_input.startswith('complete'):
        todos = get_todos()
        number_to_complete = int(input('Enter the number of todo that you have completed:'))
        number = number_to_complete - 1
        to_remove = todos[number].strip('\n')
        todos.pop(number)
        write_todos(todos)
        print(f'{to_remove} was removed from the list.')

    elif user_input.startswith('edit'):
        todos = get_todos()
        number_to_edit = int(input('Enter the number of todo that you wanna edit:'))
        number = number_to_edit - 1
        to_change = input('Enter the new todo to change the old todo:') + '\n'
        todos[number] = to_change
        write_todos(todos)

    elif user_input.startswith('exit'):
        print('Bye')
        break







