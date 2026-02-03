def run_find_circle_num(solution_class: type, is_connected: list[list[int]]):
    implementation = solution_class()
    return implementation.find_circle_num(is_connected)


def assert_find_circle_num(result: int, expected: int) -> bool:
    assert result == expected
    return True
