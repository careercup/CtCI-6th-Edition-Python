from typing import Optional, Sequence


def index(nums: Sequence[int], target: int) -> Optional[int]:
    if not nums:
        return None
    # We cannot guarantee better than O(n) if there are duplicates.
    if nums[0] == nums[-1]:
        try:
            return nums.index(target)
        except ValueError:
            return None

    is_target_left_of_wraparound = target >= nums[0]
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        is_mid_left_of_wraparound = nums[mid] >= nums[0]
        if is_mid_left_of_wraparound and not is_target_left_of_wraparound:
            lo = mid + 1
        elif not is_mid_left_of_wraparound and is_target_left_of_wraparound:
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            assert nums[mid] == target
            return mid
    return None


test_cases = [
    # array, target, valid solutions
    ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5, 8),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 2, {0, 3, 4, 5, 6, 7, 8, 9}),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 3, 1),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 4, None),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 1, 2),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 8, None),
]


def test_index():
    for array, target, expected in test_cases:
        ind = index(array, target)
        if isinstance(expected, set):
            assert ind in expected
        else:
            error_msg = (
                f"array:{array} target:{target} calculated:{ind} expected:{expected}"
            )
            assert ind == expected, error_msg
