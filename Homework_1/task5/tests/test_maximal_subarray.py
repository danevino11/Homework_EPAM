from typing import List

import pytest

from Homework_1.task5 import maximal_subarray_sum


@pytest.mark.parametrize(
    ["test_nums", "k", "expected"],
    
    [
    ([-5, -4, 3, 4], 3, 7), 
    ([-4, -5, -2, -3, 2], 4, 2),     # tests different cases
    ([1, -2, -6, -3, 1], 2, 1) 
    ]  
)
def test_maximal_subarray(test_nums, k, expected):
    actual = maximal_subarray_sum.find_maximal_subarray_sum(test_nums, k)
    assert actual == expected
