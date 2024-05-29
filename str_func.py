def str_to_upper(text: str) -> str:
    """
    Функция принимает текст и переводит все буквы в верхний регистр
    :param text: str
    :return: str
    """
    if type(text) is str:
        return text.upper()


def symbols_to_upper(text: str) -> str:
    """
    Функция принимает текст и переводит заглавные буквы кождого слова в верхний регистр
    :param text: str
    :return: str
    """
    if type(text) is str:
        return text.title()
