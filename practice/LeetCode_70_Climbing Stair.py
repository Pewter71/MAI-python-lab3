class Solution:
    def climbStairs(self, n: int) -> int:
        fibo_list = [0, 1,  2 ]
        if n < 0:
            return -1
        elif n < 3:
            return fibo_list[n]
        else:
            for index in range(3, n+1):
                fibo_list.append(fibo_list[index-1] + fibo_list[index-2])
            return fibo_list[n]