from typing import NoReturn, List


class ListOps(object):
    def __init__(self) -> NoReturn:
        pass

    @classmethod
    def remove_duplicates(
        cls,
        unfiltered_list: list,
        should_sort: bool = False,
        should_reverse: bool = False,
    ) -> list:
        unique_list = list(set(unfiltered_list))
        if should_sort is True:
            unique_list.sort(reverse=should_reverse)
        return unique_list

    @classmethod
    def get_intersection(cls, list_one: list, list_two: list) -> list:
        return list(set(list_one).intersection(list_two))

    @classmethod
    def get_union(cls, list_one: list, list_two: list) -> list:
        return list(set(list_one).union(list_two))

    @classmethod
    def get_flat_list(cls, list_of_lists: List[list] = None) -> list:
        flat_list = [item for sub_list in list_of_lists for item in sub_list]
        return flat_list
