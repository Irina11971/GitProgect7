from typing import Union


def get_expansion(name_file: str) -> Union [str, None]:
    """Принимает имя файла и выводит его расширение

    :param name_file (str): имя файла
    :return:
        str: расширение файла
        None: Расширение у файла определить невозможно
    """
    try:
        index = name_file.rfind(".")
        assert index != -1, f"Расширение у файла определить невозможно"
        return name_file[index + 1:]
    except AssertionError as e:
        print(e)


def execute_application():




if __name__ == "__main__":
    execute_application()

