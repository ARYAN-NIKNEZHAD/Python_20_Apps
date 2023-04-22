FILE_PATH = "todos"


def get_todos(file_path=FILE_PATH):
    """
    Read a text file and return the list of todo items
    :param file_path
    """
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILE_PATH):
    """
    Write the todo items list in the next file
    :param todos_arg:
    :param file_path:
    """
    with open(file_path, "w") as file_local:
        file_local.writelines(todos_arg)
