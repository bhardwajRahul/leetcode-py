def run_subarray_sum(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.subarray_sum(nums, k)


def assert_subarray_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
