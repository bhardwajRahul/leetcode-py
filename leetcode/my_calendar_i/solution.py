class MyCalendar:
    # Time: O(n) per booking, O(n^2) total for n bookings
    # Space: O(n)
    def __init__(self):
        self.calendar: list[tuple[int, int]] = []

    # Time: O(n) per booking
    # Space: O(1)
    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if start < e and end > s:
                return False
        self.calendar.append((start, end))
        return True
