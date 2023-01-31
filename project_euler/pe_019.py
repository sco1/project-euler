"""
Counting Sundays
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September, April, June and November. All the rest have thirty-one, saving February
alone, which has twenty-eight, rain or shine. And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible
by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec
2000)?
"""
import datetime as dt

START_DATE = dt.date(1901, 1, 1)
END_DATE = dt.date(2000, 12, 31)


def n_first_sundays(start_date: dt.date = START_DATE, end_date: dt.date = END_DATE) -> int:
    """Find the number of Sundays that fall on the first of the month in the given timespan."""
    # Since dt.date has a weekday method, we can just be lazy and check them all rather than writing
    # custom date stepping logic
    n_sundays = 0
    for year in range(start_date.year, end_date.year + 1):
        for month in range(1, 13):
            if dt.date(year, month, 1).weekday() == 6:
                n_sundays += 1

    return n_sundays


if __name__ == "__main__":
    print(f"Solution: {n_first_sundays()}")
