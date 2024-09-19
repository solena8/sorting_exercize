
# premier essai avant de chercher de l'aide :

# def quick_sort(nb_list)->list:
#     nb_list_smaller_or_equal:list =[]
#     nb_list_greater:list=[]
#     while len(nb_list) > 1:
#         for x in nb_list:
#             if (x <nb_list[-1]):
#                 nb_list_smaller_or_equal.append(x)
#                 quick_sort(nb_list_smaller_or_equal)
#                 nb_list_greater.append(x)
#                 quick_sort(nb_list_greater)
#     final_list:list = nb_list_smaller_or_equal + nb_list_greater
#     print(final_list)
#     return final_list


def quick_sort(nb_list:list)->(list, int):
    it: int = 0
    if len(nb_list) <= 1:
        return nb_list, it
    else:
        pivot:int= nb_list[-1]
        smaller:list = []
        greater:list = []
        for x in nb_list[:-1]: #tout sauf le dernier index de la liste
            it +=1
            if x <= pivot:
                smaller.append(x)
            else:
                greater.append(x)
        result_smaller, it_smaller = quick_sort(smaller)
        result_greater, it_greater = quick_sort(greater)
        result_list: list = result_smaller + [pivot] + result_greater
        it_result:int = it + it_smaller + it_greater
        return result_list, it_result


