# Обратное преобразование
# В базовом курсе по python есть задача RGB , в которой необходимо по трем целым числам получить цвет в формате RGB.
# Сейчас вам предстоит выполнить обратное преобразование
#
# Ваша задача создать функцию from_hex_to_rgb, которая принимает на вход строку - закодированный код цвета в формате
# RGB и возвращает кортеж из трех значений (оттенок_красного, оттенок_зеленого, оттенок_синего). Вот посмотрите примеры:
#
# from_hex_to_rgb(#000000) => (0, 0, 0)
# from_hex_to_rgb(#FFFFFF) => (255, 255, 255)
# from_hex_to_rgb(#FF0000) => (255,0, 0)
# from_hex_to_rgb(#00FF00) => (0,255, 0)
# from_hex_to_rgb(#0000FF) => (0,0,255)
# from_hex_to_rgb(#FFFFFF) => (255,255,255)
# from_hex_to_rgb(#87CEEB) => (135,206,235)
# from_hex_to_rgb(#87CEFA) => (135,206,250)
# from_hex_to_rgb(#191970) => (25,25,112)
# Как только функция будет готова, ее необходимо использовать внутри функции convert_to_rgb, которая принимает список
# строк, содержащих информацию о цветах в формате RGB. Функция convert_to_rgb должна расшифровать каждый цвет и
# вернуть список кортежей.
#
# Sample Input 1:
#
# print(from_hex_to_rgb('#B22222'))
# print(from_hex_to_rgb('#FFFFFF'))
# print(from_hex_to_rgb('#000000'))
# print(from_hex_to_rgb('#87CEEB'))
# print(from_hex_to_rgb('#191970'))
# Sample Output 1:
#
# (178, 34, 34)
# (255, 255, 255)
# (0, 0, 0)
# (135, 206, 235)
# (25, 25, 112)
# Sample Input 2:
#
# colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50']
# print(convert_to_rgb(colors))
# Sample Output 2:
#
# [(178, 34, 34), (220, 20, 60), (255, 0, 0), (255, 99, 71), (255, 127, 80)]
# Sample Input 3:
#
# colors = ['#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32']
# print(convert_to_rgb(colors))
# Sample Output 3:
#
# [(238, 232, 170), (189, 183, 107), (240, 230, 140), (128, 128, 0), (255, 255, 0), (154, 205, 50)]


from functools import wraps


def from_hex_to_rgb(color: str)->tuple[int, int, int]:
    return ((int(color[1:3], 16)), (int(color[3:5], 16)), (int(color[5:], 16)))


def convert_to_rgb(values: list) -> list[tuple[int, int, int]]:
    return list(map(from_hex_to_rgb, values))


print(from_hex_to_rgb('#B22222'))
print(from_hex_to_rgb('#FFFFFF'))
print(from_hex_to_rgb('#000000'))
print(from_hex_to_rgb('#87CEEB'))
print(from_hex_to_rgb('#191970'))
