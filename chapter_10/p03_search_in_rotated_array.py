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


def test_find_5_in_15_16_19_20_25_1_3_4_5_7_10_14() -> None:
    assert index([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=5) == 8


def test_find_2_in_2_3_1_2_2_2_2_2_2_2() -> None:
    assert index([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=2) in {0, 3, 4, 5, 6, 7, 8, 9}


def test_find_3_in_2_3_1_2_2_2_2_2_2_2() -> None:
    assert index([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=3) == 1


def test_find_4_in_2_3_1_2_2_2_2_2_2_2() -> None:
    assert index([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=4) is None


def test_find_1_in_2_3_1_2_2_2_2_2_2_2() -> None:
    assert index([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=1) == 2


def test_find_8_in_2_3_1_2_2_2_2_2_2_2() -> None:
    assert index([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], target=8) is None
