from FreqObjectOps.ListOps import ListOps

list_with_duplicates = [1, 1, 2, 3]
unique_list = [1, 2, 3]
list_one = [1, 2, 3, 4]
list_two = [2, 3, 4, 5]
list_common = [2, 3, 4]
list_union = [1, 2, 3, 4, 5]
list_of_lists = [[1, 2], [3, 4, 5]]
flattened_list = [1, 2, 3, 4, 5]


def test_get_unique_list():
    assert (
        ListOps.remove_duplicates(
            list_with_duplicates, should_sort=True, should_reverse=False
        )
        == unique_list
    )


def test_get_common_items():
    assert ListOps.get_intersection(list_one, list_two) == list_common


def test_get_all_items():
    assert ListOps.get_union(list_one, list_two) == list_union


def test_get_flat_list():
    assert ListOps.get_flat_list(list_of_lists) == flattened_list
