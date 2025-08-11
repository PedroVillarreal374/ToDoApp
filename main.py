from task_model import task_model

def main():
    task = TaskModel ("Estudiar para el examen")
    print (f"Tarea Creada: {task.get_task_name()}")

if _name_ == "_main_":
    main()