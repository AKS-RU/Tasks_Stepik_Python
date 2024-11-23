# Хранитель архива
# Вы – главный программист в отделе архива следственного комитета. Вас попросили сделать особенный
# словарь ArchiveDict для архивного хранения дел. Его отличительной особенностью от обычного словаря
# заключается в невозможности удаления ключа. При любой попытке удалить значение из словаря должно
# вызываться исключение RuntimeError("Deletion not allowed")


from collections import UserDict


class ArchiveDict(UserDict):
    def pop(self, *args):
        raise RuntimeError('Дела нельзя удалять из архива')

    def popitem(self, *args):
        raise RuntimeError('Дела нельзя удалять из архива')

    def __delitem__(self, key):
        raise RuntimeError('Дела нельзя удалять из архива')


archive = ArchiveDict(
    {1: 'Дело № 1 о загадочном исчезновении обуви под кодовым названием «Пропала Пара»',
     4: 'Дело № 4: под юбкой правосудия: Расследование «Тайна Кружев»',
     10: 'Дело № 10: преступление на вечеринке: мотив «Скользкая Политика»'}
)

try:
    archive.pop(1)  # Дела нельзя удалять из архива
except RuntimeError:
    pass

try:
    archive.popitem(1)  # Дела нельзя удалять из архива
except RuntimeError:
    pass

try:
    del archive[10]  # Дела нельзя удалять из архива
except RuntimeError:
    pass

assert len(archive) == 3
archive[60] = 'Дело № 60: инцидент на трассе 60'
assert len(archive) == 4

print('Good')
