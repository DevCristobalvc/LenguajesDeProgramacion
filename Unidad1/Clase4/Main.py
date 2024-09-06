def getTasks(priority, duration=0):
    tasks_db = {
        "high": [
            {"name": "finish front-end", "duration": 180},
            {"name": "begin back-end", "duration": 120}
        ],
        "medium": [
            {"name": "do the dishes", "duration": 60},
            {"name": "wash the dog", "duration": 45}
        ],
        "low": [
            {"name": "do the shopping", "duration": 90},
            {"name": "paint the walls", "duration": 45}
        ],
    }
    
    # Filtrar tareas por duración
    def filter_tasks(task_list, max_duration):
        return [task for task in task_list if task['duration'] <= max_duration]
    
    # Obtener tareas y aplicar filtro
    task_list = tasks_db.get(priority, [])
    task_list = filter_tasks(task_list, duration)
    
    # Generador para iterar sobre las tareas
    def tasks_stream(index=0):
        if index < len(task_list):
            yield task_list[index]
            yield from tasks_stream(index + 1)
    
    return tasks_stream()

# Pruebas del stream de tareas
priority = input("¿De qué prioridad desea ver las tareas? (high, medium, low): ").strip().lower()
duration = int(input("¿Qué duración máxima? (en minutos): "))

tasks_by_priority_duration = getTasks(priority, duration)

# Mostrar tareas filtradas
try:
    print(next(tasks_by_priority_duration))
    print(next(tasks_by_priority_duration))
    # Puedes seguir llamando a next(tasks_by_priority_duration) para obtener más tareas, si hay más disponibles.
except StopIteration:
    print("No hay más tareas disponibles.")
