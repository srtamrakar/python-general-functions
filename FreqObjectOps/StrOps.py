import re
import unidecode
from typing import NoReturn


class StrOps(object):
    def __init__(self) -> NoReturn:
        pass

    @classmethod
    def is_camel_case(cls, text: str = None) -> bool:
        """
        :param text: str
        :return:
            whether text is in camelcase
        """
        if text is None:
            return False
        invalid_content_regexp = re.compile(
            r"""[`~!@#$%^&*()\-_=+[\]{};':"\\\|,\./<>?]|\s"""
        )
        if invalid_content_regexp.search(text):
            return False
        if text in [text.lower(), text != text.upper()]:
            return False
        return True

    @classmethod
    def remove_accent(cls, text: str = None) -> str:
        """
        :param text: str
        :return:
            text without accents
        """
        return unidecode.unidecode(text)

    @classmethod
    def clean_snake_case(cls, text: str = None) -> str:
        """
        :param text: str
        :return:
            cleaned snake case as str
        """
        snake_clean = re.sub("_+", "_", cls.remove_accent(text))
        return snake_clean

    @classmethod
    def text_to_alpha_numeric(cls, text: str = None, replace_string: str = None) -> str:
        """
        :param text: str
        :param replace_string: str
        :return:
            text with non-alpha characters replaced by replace_string
        """
        if replace_string is None:
            replace_string = "_"
        alphanumeric = re.sub("[^a-zA-Z0-9]+", replace_string, cls.remove_accent(text))
        return alphanumeric

    @classmethod
    def text_to_camel_case(cls, text: str = None, case: str = None) -> str:
        """
        :param text: str
        :param case: str (lower / upper)
            case of returned text
        :return:
            camelCase representation of a text
        """
        if case is None:
            case = "lower"
        camel_case = cls.remove_accent(text).title().replace("_", "")
        camel_case = re.sub(r"[^a-zA-Z0-9]+", "", camel_case)
        camel_case = camel_case.replace(" ", "")
        if case.lower() == "lower":
            camel_case = camel_case[0].lower() + camel_case[1:]
        return camel_case

    @classmethod
    def camel_case_to_snake_case(cls, text: str = None, case: str = None) -> str:
        """
        :param text: str
        :param case: str (lower / upper)
            case of returned text
        :return:
            snake_case representation of a text
        """
        if case is None:
            case = "lower"
        first_cap_regexp = re.compile("(.)([A-Z][a-z]+)")
        all_cap_regexp = re.compile("([a-z])([A-Z0-9])")

        snake_temp = first_cap_regexp.sub(r"\1_\2", cls.remove_accent(text))
        snake = all_cap_regexp.sub(r"\1_\2", snake_temp).lower()
        snake_clean = cls.clean_snake_case(snake)
        if case.lower() == "upper":
            snake_clean = snake_clean.upper()
        return snake_clean

    @classmethod
    def text_to_snake_case(cls, text: str = None, case: str = None) -> str:
        """
        :param text: str
        :param case: str (lower / upper)
            case of returned text
        :return:
            snake_case representation of a text
        """
        if cls.is_camel_case(text=text):
            return cls.camel_case_to_snake_case(text=text, case=case)
        else:
            return cls.camel_case_to_snake_case(
                cls.text_to_camel_case(text=text), case=case
            )
