class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Некорректный индекс задачи.")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавляем задачи
    manager.add_task("Написать отчет", "2025-03-03")
    manager.add_task("Подготовить презентацию", "2025-03-09")

    # Выводим текущие задачи
    print("Текущие задачи:")
    manager.display_tasks()

    # Отмечаем задачу как выполненную
    manager.mark_task_completed(0)

    # Выводим обновленный список задач
    print("Обновленный список задач:")
    manager.display_tasks()

    # Выводим только текущие (не выполненные) задачи
    print("Не выполненные задачи:")
    current_tasks = manager.get_current_tasks()
    for task in current_tasks:
        print(task)