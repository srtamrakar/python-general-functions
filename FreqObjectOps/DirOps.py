import os
import re
import glob
from typing import NoReturn, Callable, Optional, List


def normalize_returned_path(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        return DirOps.get_norm_path(func(*args, **kwargs))

    return wrapper


class DirOps(object):
    def __init__(self) -> NoReturn:
        pass

    @classmethod
    def get_norm_path(cls, file_path: str) -> str:
        return os.path.normcase(os.path.normpath(file_path))

    @classmethod
    @normalize_returned_path
    def get_abs_path(cls, file_path: str) -> str:
        return os.path.abspath(file_path)

    @classmethod
    @normalize_returned_path
    def get_dir_from_file_path(cls, file_path: str) -> str:
        return os.path.dirname(file_path)

    @classmethod
    def get_basename_from_file_path(cls, file_path: str) -> str:
        return os.path.splitext(os.path.basename(file_path))[0]

    @classmethod
    def get_file_extension_from_file_path(cls, file_path: str) -> str:
        return os.path.splitext(os.path.basename(file_path))[-1]

    @classmethod
    def exists_dir(cls, dir_: str) -> bool:
        if os.path.exists(dir_):
            return True
        return False

    @classmethod
    def filter_out_temporary_files(cls, file_list: List[str]) -> List[str]:
        temp_file_regex = re.compile(r".*~\$.*")
        temporary_file_list = list(filter(temp_file_regex.search, file_list))
        filtered_file_list = list(set(file_list).difference(set(temporary_file_list)))
        return filtered_file_list

    @classmethod
    def get_all_files_in_dir(
        cls, dir_: str, pattern: str = "*.*", recursive: bool = False
    ) -> List[str]:
        if recursive is True:
            file_pattern = os.path.join(dir_, "**", pattern)
        else:
            file_pattern = os.path.join(dir_, pattern)
        all_files_list = glob.glob(file_pattern, recursive=recursive)
        all_files_list = list(map(cls.get_norm_path, all_files_list))
        all_files_list = cls.filter_out_temporary_files(file_list=all_files_list)
        return all_files_list

    @classmethod
    @normalize_returned_path
    def get_latest_file_in_dir(cls, dir_: str, pattern: str = "*.*") -> Optional[str]:
        all_files_list = cls.get_all_files_in_dir(
            dir_=dir_, pattern=pattern, recursive=False
        )
        if len(all_files_list) < 1:
            return None
        latest_file = max(all_files_list, key=os.path.getctime)
        return latest_file
