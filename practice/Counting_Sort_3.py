# Enter your code here. Read input from STDIN. Print output to STDOUT
def countingSort(a):
    result = [0]*100
    for i in a:
        result[i] += 1
    for i in range(1, 100):
        result[i] = result[i] + result[i-1]
    return result


n = int(input())
input_list = []
for i in range(n):
    a = [x for x in input().split()]
    for j in a:
        if j.isdigit():
            input_list.append(int(j))
result = countingSort(input_list)
for i in result:
    print(i, end=" ")
