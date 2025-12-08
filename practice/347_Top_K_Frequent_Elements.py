from typing import List


class Solution:
    def quick_sort(self, a: list[tuple[int, int]]) -> list[tuple[int, int]]:
        if len(a) < 2:
            return a
        pivot = a[0][1]
        left = [(x[0], x[1]) for x in a if x[1] > pivot]
        middle = [(x[0], x[1]) for x in a if x[1] == pivot]
        right = [(x[0], x[1]) for x in a if x[1] < pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = dict()
        for i in nums:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] += 1
        count_list = list(count_dict.items())
        count_list = self.quick_sort(count_list)
        result = [x[0] for x in count_list]
        return result[:k]
