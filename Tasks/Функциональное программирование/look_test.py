class Date:

    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year


class DateEurope(Date):

    def format(self):
        return f"{self._day:02}/{self._month:02}/{self._year:04}"

    def isoformat(self):
        return f"{self._year:04}-{self._month:02}-{self._day:02}"


class DateUSA(Date):

    def format(self):
        return f"{self._month:02}/{self._day:02}/{self._year:04}"

    def isoformat(self):
        return f"{self._year:04}-{self._month:02}-{self._day:02}"
        return f"{self._year:04}-{self._month:02}-{self._day:02}"


# d = DateUSA(1, 5, 890)
# print(d.format())
# print(d.isoformat())
# print(isinstance(d, DateEurope))
# print(isinstance(d, Date))
# print(isinstance(d, DateUSA))


def test_date_usa_format():
    date_usa = DateUSA(15, 3, 2023)
    assert date_usa.format() == "03/15/2023"
