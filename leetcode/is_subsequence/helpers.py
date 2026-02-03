def run_is_subsequence(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.is_subsequence(s, t)


def assert_is_subsequence(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
