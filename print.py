from data import little_random, big_random, little_sorted, big_sorted
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from typing import Callable


def print_list_it(sorting_function: Callable, nb_list: list, sorting_type: str, list_name: str) -> None:
    result_list, result_it = sorting_function(nb_list)
    print(f"With the {sorting_type} method, for the {list_name} list, the number of step(s) is {result_it}.")


print_list_it(quick_sort,little_random, "quick_sort", "little_random")
print_list_it(bubble_sort,little_random, "bubble_sort", "little_random")
print_list_it(quick_sort,little_sorted, "quick_sort", "little_sorted")
print_list_it(bubble_sort,little_sorted, "bubble_sort", "little_sorted")
print_list_it(quick_sort,big_random, "quick_sort", "big_random")
print_list_it(bubble_sort,big_random, "bubble_sort", "big_random")
print_list_it(quick_sort,big_sorted, "quick_sort", "big_sorted")
print_list_it(bubble_sort,big_sorted, "bubble_sort", "big_sorted")


# conseil :
# for dataset, dataset_name in [(little_random, "little_random"), (little_sorted, "little_sorted"),
#                               (big_random, "big_random"), (big_sorted, "big_sorted")]:
#     for sorting_fct, fct_name in [(quick_sort, "quick_sort"), (bubble_sort, "bubble_sort")]:
#         print_list_it(sorting_fct, dataset, fct_name, dataset_name)
