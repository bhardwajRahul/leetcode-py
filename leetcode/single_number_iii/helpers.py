def run_single_number(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.single_number(nums)


def assert_single_number(result: list[int], expected: list[int]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
