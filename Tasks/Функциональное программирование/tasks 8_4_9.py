# Превращаем вложенный словарь в плоский
# Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен. Ключами словаря на
# любом уровне могут быть только строки, значениями - только числа.
#
# Учитывая указанные выше условия, ваша задача состоит в том, чтобы преобразовать этот вложенный словарь в плоский
# (состоящий только из одного уровня), где ключи формируются конкатенацией вложенных ключей, соединенных знаком _
#
# Для этого необходимо определить рекурсивную функцию flatten_dict. Она должна принимать вложенный словарь и
# возвращать плоский
#
# Ваша задача только написать определение функции flatten_dict
#
# Sample Input 1:
#
# print(flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}))
# Sample Output 1:
#
# {'Q_w_E_r_T_y': 123}
# Sample Input 2:
#
# print(flatten_dict({'Germany_berlin': 7,
#                     'Europe_italy_Rome': 3,
#                     'USA_washington': 1,
#                     'USA_New York': 4}))
# Sample Output 2:
#
# {'Germany_berlin': 7, 'Europe_italy_Rome': 3, 'USA_washington': 1, 'USA_New York': 4}
# Sample Input 3:
#
# print(flatten_dict({"a": 1,
#                     "b": {
#                         "c": 2,
#                         "d": 3,
#                         "e": {
#                             "f": 4,
#                             '6': 100,
#                             '5': {"g": 6},
#                             "l": 1,
#                         }
#                     }}))
# Sample Output 3:
#
# {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'b_e_6': 100, 'b_e_5_g': 6, 'b_e_l': 1}
# Sample Input 4:
#
# print(flatten_dict({'a': 100, 'b': 200}))
# Sample Output 4:
#
# {'a': 100, 'b': 200}



# def flatten_dict(dct: dict[str:int])->dict[str:int]:
#     result = {}
#     keys = ''
#     for key, item in dct.items():
#         if isinstance(item, dict):
#             k = flatten_dict(item)
#             keys=f'{key}_{k}'
#             result.setdefault(key,0)
#             return keys
#         else:
#             pass
#             # keys= f'{keys}_{key}'
#             # print(keys, item)
#
#     return result

def flatten_dict(dct: dict[str:int])->dict[str:int]:
    result = {}
    for key, item in dct.items():
        if isinstance(item, dict):
            sub_dict = flatten_dict(item)
            result |= {f'{key}_{k}': v for k, v in sub_dict.items()}
            return result
        else:
            result.setdefault(key,item)

    return result




# print(flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}))
# print(flatten_dict({'Germany_berlin': 7,
#                     'Europe_italy_Rome': 3,
#                     'USA_washington': 1,
#                     'USA_New York': 4}))
# print(flatten_dict({"a": 1,
#                     "b": {
#                         "c": 2,
#                         "d": 3,
#                         "e": {
#                             "f": 4,
#                             '6': 100,
#                             '5': {"g": 6},
#                             "l": 1,
#                         }
#                     }}))

print(flatten_dict({'a': 100, 'b': 200}))
