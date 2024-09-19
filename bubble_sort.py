

def bubble_sort(list_to_sort:list) ->(list, int):
    length:int = len(list_to_sort)
    iteration:int = 0
    for i in range(length):
        for j in range(length - i - 1):
            if list_to_sort[j] >= list_to_sort[j+1]:
                temp:list = list_to_sort[j]
                list_to_sort[j]= list_to_sort[j+1]
                list_to_sort[j+1]=temp
            iteration += 1
    return list_to_sort, iteration


