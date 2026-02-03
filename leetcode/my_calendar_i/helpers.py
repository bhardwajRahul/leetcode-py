def run_my_calendar(solution_class: type, bookings: list[tuple[int, int]]):
    implementation = solution_class()
    results = []
    for start, end in bookings:
        results.append(implementation.book(start, end))
    return results


def assert_my_calendar(result: list[bool], expected: list[bool]) -> bool:
    assert result == expected
    return True
