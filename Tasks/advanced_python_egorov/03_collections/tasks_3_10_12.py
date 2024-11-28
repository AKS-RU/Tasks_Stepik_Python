# История действий
# Двухсторонние очереди хороши для хранения истории пользовательских действий. Это позволяет
# отменять и повторять действия пользователя. Давайте на примере текстового редактора разберем
# такой пример

# Вам нужно создать класс TextEditor для текстового редактора, который использует deque для
# управления историей действий пользователя. Редактор должен поддерживать две основные операции:
#     отмену последнего действия и повтор последнего действия. Класс TextEditor состоит из:

# метод __init__, который создает редактор с пустым текстом, остальные атрибуты создавайте на
# свое усмотрение.

# метод add_text(text), который добавляет указанный текст в текущий текст редактора и сохраняет
# это действие в истории.

# метод undo(), который отменяет последнее действие пользователя. Если есть доступное действие
# для отмены, метод должен удалять последнее действие из истории и восстанавливать текст редактора к состоянию перед этим действием.

# метод redo(), который выполняет последнее отмененное действие. Если есть доступное действие
# для повтора, метод должен удалять последнее действие из истории отмен и применять его к
# тексту редактора.

# метод get_text(), который возвращает текущее состояние текста в редакторе


from collections import deque


class TextEditor:

    def __init__(self):
        self.editor = deque()
        self.save_undo = deque()

    def add_text(self, text):
        self.editor.append(text)

    def undo(self):
        self.save_undo.append(self.editor.pop())

    def redo(self):
        self.editor.append(self.save_undo.pop())

    def get_text(self):
        return ''.join(self.editor)


editor = TextEditor()
editor.add_text("Hello, ")
print(editor.get_text())
assert editor.get_text() == "Hello, "

editor.add_text("World!")
assert editor.get_text() == "Hello, World!"

editor.add_text(" How are you!")
assert editor.get_text() == "Hello, World! How are you!"

editor.undo()
assert editor.get_text() == "Hello, World!"

editor.redo()
assert editor.get_text() == "Hello, World! How are you!"

editor.undo()
assert editor.get_text() == "Hello, World!"

editor.undo()
assert editor.get_text() == "Hello, "

print('OK')
