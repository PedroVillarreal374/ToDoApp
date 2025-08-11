from task_model import task_model

def main():
    task = TaskModel ("Estudiar para el examen")
    print (f"Tarea Creada: {task.get_task_name()}")

    task.mark_as_complete()
    print(f"Tarea Completada : {Task.is_completed()}")

if _name_ == "_main_":
    main()