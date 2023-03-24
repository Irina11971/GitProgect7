from typing import Union

def get_expansion(name_file: str) -> str:
    """Принимает имя файла и выводит его расширение

    :param name_file (str): имя файла
    :return:
        str: расширение файла
    """
    try:
        index = name_file.rfind(".")
        if index == -1:
            raise Exception(f"Расширение у файла определить невозможно")
        return name_file[index + 1:]
    except Exception as e:
        print(e)


def execute_application():

    name_file = "file.txt"
    print(get_expansion(name_file))



if __name__ == "__main__":
    execute_application()

