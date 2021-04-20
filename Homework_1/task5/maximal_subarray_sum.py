"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List

def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    list_of_sums = []
    nums.sort(reverse=True)
    sub_array = nums[:k]
    first_sum = sub_array[0]
    for j in sub_array[1:]:
        if first_sum < first_sum + j:
            first_sum = first_sum + j
        else:                                # in case all the other elements except one are less than zero
            list_of_sums.append(first_sum)
        list_of_sums.append(first_sum)
    return max(list_of_sums)
