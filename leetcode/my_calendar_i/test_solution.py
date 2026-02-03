import pytest

from leetcode_py import logged_test

from .helpers import assert_my_calendar, run_my_calendar
from .solution import MyCalendar


class TestTestMyCalendarI:
    def setup_method(self):
        self.solution = MyCalendar()

    @logged_test
    @pytest.mark.parametrize(
        "bookings, expected",
        [
            ([(10, 20), (15, 25), (20, 30)], [True, False, True]),
            ([(47, 50), (33, 41), (39, 48), (29, 34)], [True, True, False, False]),
            (
                [
                    (20, 29),
                    (13, 22),
                    (44, 50),
                    (1, 7),
                    (2, 10),
                    (14, 20),
                    (19, 25),
                    (36, 42),
                    (45, 50),
                ],
                [True, False, True, True, False, True, False, True, False],
            ),
            ([(10, 20)], [True]),
            ([(10, 20), (20, 30)], [True, True]),
            ([(10, 20), (19, 30)], [True, False]),
            ([(10, 20), (5, 15)], [True, False]),
            ([(10, 20), (5, 10)], [True, True]),
            ([(10, 20), (20, 25), (25, 30)], [True, True, True]),
            ([(0, 1000000000)], [True]),
            ([(10, 20), (10, 20)], [True, False]),
            ([(1, 10), (10, 20), (20, 30), (30, 40)], [True, True, True, True]),
            ([(1, 5), (5, 10), (10, 15), (2, 12)], [True, True, True, False]),
            (
                [(37, 50), (33, 50), (25, 42), (42, 50), (14, 25), (20, 30), (5, 17)],
                [True, False, False, False, True, False, False],
            ),
        ],
    )
    def test_my_calendar(self, bookings: list[tuple[int, int]], expected: list[bool]):
        result = run_my_calendar(MyCalendar, bookings)
        assert_my_calendar(result, expected)
