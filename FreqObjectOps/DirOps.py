import os.path
import sys
import re
import glob
from typing import NoReturn, Callable, Optional, List

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def normalize_returned_path(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        return DirOps.get_norm_path(func(*args, **kwargs))

    return wrapper


class DirOps(object):
    def __init__(self) -> NoReturn:
        pass

    @classmethod
    def get_norm_path(cls, file_path: str = None) -> str:
        """
        :param file_path: str
        :return:
            normalized file_path as str
        """
        return os.path.normcase(os.path.normpath(file_path))

    @classmethod
    @normalize_returned_path
    def get_abs_path(cls, file_path: str = None) -> Optional[str]:
        """
        :param file_path: str
        :return:
            absolute file_path as str
        """
        if file_path is None:
            return None
        return os.path.abspath(file_path)

    @classmethod
    @normalize_returned_path
    def get_directory_from_file_path(cls, file_path: str = None) -> Optional[str]:
        """
        :param file_path: str
        :return:
            directory as str
        """
        if file_path is None:
            return None
        return os.path.dirname(file_path)

    @classmethod
    def get_basename_from_file_path(cls, file_path: str = None) -> Optional[str]:
        """
        :param file_path: str
        :return:
            basename as str
        """
        if file_path is None:
            return None
        return os.path.splitext(os.path.basename(file_path))[0]

    @classmethod
    def get_file_extension_from_file_path(cls, file_path: str = None) -> Optional[str]:
        """
        :param file_path: str
        :return:
            file extension as str
        """
        if file_path is None:
            return None
        return os.path.splitext(os.path.basename(file_path))[-1]

    @classmethod
    def exists_folder(cls, folder_path: str = None) -> bool:
        """
        :param folder_path: str
        :return:
            whether the folder exists as bool
        """
        if folder_path is None:
            return False
        if os.path.exists(folder_path):
            return True
        return False

    @classmethod
    def get_filtered_list_without_temporary_files(
        cls, file_list: List[str] = None
    ) -> List:
        """
        :param file_list: list
            list of filename
        :return:
            filtered list of non-temporary filename
        """
        temp_file_regex = re.compile(r".*~\$.*")
        try:
            temporary_files = list(filter(temp_file_regex.search, file_list))
            files_filtered = list(set(file_list) - set(temporary_files))
            return files_filtered
        except:
            return file_list

    @classmethod
    def get_all_files_in_directory(
        cls, folder_path: str = None, pattern: str = None, recursive: bool = False
    ) -> Optional[List]:
        """
        :param folder_path: str
        :param pattern: str
        :param recursive: bool
            whether to get files from sub-directories as well
        :return:
            list of filename inside folder_path
        """
        if folder_path is None:
            return None
        if pattern is None:
            pattern = "*.*"  # e.g. *.xlsx
        if recursive is True:
            file_pattern = os.path.join(folder_path, "**", pattern)
        else:
            file_pattern = os.path.join(folder_path, pattern)
        all_files_list = glob.glob(file_pattern, recursive=recursive)
        all_files_list = list(map(cls.get_norm_path, all_files_list))
        all_files_list = cls.get_filtered_list_without_temporary_files(
            file_list=all_files_list
        )
        return all_files_list

    @classmethod
    @normalize_returned_path
    def get_latest_file_in_directory(
        cls, folder_path: str = None, pattern: str = None
    ) -> Optional[str]:
        """
        :param folder_path: str
        :param pattern: str
        :return:
            file_path of the last updated file from the directory as str
        """
        if folder_path is None:
            return None
        if not pattern:
            pattern = "*.*"  # e.g. *.xlsx
        all_files_list = cls.get_all_files_in_directory(
            folder_path=folder_path, pattern=pattern, recursive=False
        )
        if len(all_files_list) < 1:
            return None
        latest_file = max(all_files_list, key=os.path.getctime)
        return latest_file
