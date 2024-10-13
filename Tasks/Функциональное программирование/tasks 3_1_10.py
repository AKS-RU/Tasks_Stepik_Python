# Напишите функцию get_leap_years, которая принимает два года y1 и y2, причем y1 <= y2, и возвращает список,
# состоящий из високосных лет в промежутке от y1 включительно до  y2 не включительно. Года должны располагаться в
# нем в хронологическом порядке.
#
# При реализации функции get_leap_years используйте ранее созданную функцию is_leap.
#
# Напишите только определения необходимых функций.
#
# Sample Input 1:
#
# print(get_leap_years(2000, 2018))
# Sample Output 1:
#
# [2000, 2004, 2008, 2012, 2016]
# Sample Input 2:
#
# print(get_leap_years(2015, 2020))
# Sample Output 2:
#
# [2016]
# Sample Input 3:
#
# print(get_leap_years(1990, 2021))
# Sample Output 3:
#
# [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
# Sample Input 4:
#
# print(get_leap_years(1890, 2021))
# Sample Output 4:
#
# [1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
# Sample Input 5:
#
# print(get_leap_years(2021, 2021))
# Sample Output 5:
#
# []

def is_leap(year: int):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def get_leap_years(y1: int, y2: int):
    lst_year = [i for i in range(y1, y2) if is_leap(i)]
    return lst_year

print(get_leap_years(2000, 2018))