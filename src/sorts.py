

def bubble_sort(a: list[int]) -> list[int]:
    list_size = len(a)
    sorted_list = a.copy()
    for i in range(list_size):
        for j in range(0, list_size-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j +
                                            1] = sorted_list[j+1], sorted_list[j]
    return sorted_list
