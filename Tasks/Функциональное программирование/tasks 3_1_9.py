# Напишите функцию count_leap_years, которая принимает два года y1 и y2, причем y1 <= y2, и возвращает
# количество високосных лет в промежутке от y1 включительно до  y2 не включительно.
#
# При реализации функции count_leap_years используйте ранее созданную функцию is_leap.
#
# Напишите только определения необходимых функций.
#
# Sample Input 1:
#
# print(count_leap_years(2000, 2018))
# Sample Output 1:
#
# 5
# Sample Input 2:
#
# print(count_leap_years(2015, 2020))
# Sample Output 2:
#
# 1
# Sample Input 3:
#
# print(count_leap_years(1990, 2021))
# Sample Output 3:
#
# 8
# Sample Input 4:
#
# print(count_leap_years(1890, 2021))
# Sample Output 4:
#
# 32
# Sample Input 5:
#
# print(count_leap_years(2021, 2021))
# Sample Output 5:
#
# 0

def is_leap(year: int):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def count_leap_years(y1: int, y2: int):
    lst_year = [i for i in range(y1, y2) if is_leap(i)]
    return len(lst_year)

print(count_leap_years(2000, 2018))