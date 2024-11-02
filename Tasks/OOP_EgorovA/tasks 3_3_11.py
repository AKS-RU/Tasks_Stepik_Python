# Создание приложения для учета задач
# В этом задании вам нужно создать приложение для учета задач, используя классы Task, TaskList и TaskManager.
#
# Класс Task будет хранить информацию о задаче (название, описание, статус выполнения) и состоит из:
#
# метод  __init__ - принимает аргументы name , description и status  и сохраняет их в атрибуты экземпляра. По умолчанию
# значением аргумента status является False;
#
# метод display - печатает информацию о статусе задачи в следующем виде:
# {название задачи} (Сделана/Не сделана)
# В зависимости от статуса задачи выводится строка «Сделана» или  «Не сделана».
#
# Класс TaskList - содержит список задач и методы для добавления/удаления задач и состоит из:
#
# метод __init__ - создает пустой список задач в атрибуте tasks;
#
# метод add_task - принимает задачу и добавляет ее в конец списка задач;
#
# метод remove_task - принимает задачу и удаляет ее из списка задач.
#
# Класс TaskManager - содержит методы для отображения списка задач и изменения статуса выполнения задач и состоит из:
#
# метод __init__ - принимает экземпляр класса TaskList  и сохраняет его в атрибуте task_list;
#
# метод  mark_done - принимает задачу (экземпляр класса Task)  и устанавливает ей истинный статус выполнения (True);
#
# метод  mark_undone - принимает задачу (экземпляр класса Task)  и устанавливает ей ложный статус выполнения (False);
#
# метод  show_tasks - вызывает метод display(метод класса Task) для каждой хранящейся задачи в списке задач.


class Task:

    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        print(f'{self.name} {"(Сделана)" if self.status else "(Не сделана)"}')


class TaskList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class TaskManager:

    def __init__(self, task_list):
        self.task_list = task_list

    def mark_done(self, tasks):
        tasks.status = True

    def mark_undone(self, tasks):
        tasks.status = False

    def show_tasks(self):
        list(map(Task.display, self.task_list.tasks))


todo = TaskList()
assert todo.tasks == []

# Создаем несколько задач и добавляем их в список
task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
assert task1.name == 'Стирка'
assert task1.description == 'Постирать трусы, носки, слюнявчики'
assert task1.status is False
task1.display()

todo.add_task(task1)
assert len(todo.tasks) == 1

task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
assert task2.name == 'Продукты'
assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
assert task2.status is False

todo.add_task(task2)
assert len(todo.tasks) == 2

# Создаем менеджер задач и показываем список задач
manager = TaskManager(todo)
assert isinstance(manager.task_list, TaskList)
print('-----Список дел-----')
manager.show_tasks()

# Отмечаем первую задачу выполненной и показываем список задач
manager.mark_done(task1)
# Проверяем изменился ли статус 2мя способами
assert task1.status is True
assert manager.task_list.tasks[0].status is True

print('-----Список дел-----')
manager.show_tasks()

# Удаляем вторую задачу и показываем список задач
todo.remove_task(task2)

assert len(todo.tasks) == 1
assert len(manager.task_list.tasks) == 1

print('-----Список дел-----')
manager.show_tasks()
print('Все тесты пройдены успешно!')
