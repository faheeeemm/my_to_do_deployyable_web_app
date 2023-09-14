FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """
            Reads the Todos List from the file.
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, file_path=FILEPATH):
    """
        Writes the Todos into the file.
    """
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_local)
