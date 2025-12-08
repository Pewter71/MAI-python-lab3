#!/bin/python3


import os


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(a):
    count_dict = dict()
    sorted_list = []
    min_element = a[0]
    max_element = a[0]
    for i in a:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
        min_element = min(min_element, i)
        max_element = max(max_element, i)
    for i in range(min_element, max_element+1):
        if i in count_dict:
            sorted_list += [i] * count_dict[i]
    return sorted_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
