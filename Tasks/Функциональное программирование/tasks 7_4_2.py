from inspect import getgeneratorstate

def my_coro(a):
    print(f'Запускаем корутину со значением a={a}')
    b = yield a
    print(f'Получено значение b={b}')
    try:
        c = yield a+b
        print(f'Получено значение c={c}')
    except StopIteration:
        print('GEN_CLOSED')
    else:
        None





coro = my_coro(7)
print(getgeneratorstate(coro))
next(coro)
print(getgeneratorstate(coro))
print(coro.send(23))
print(getgeneratorstate(coro))
print(coro.send(100))
coro.close()
print(getgeneratorstate(coro))