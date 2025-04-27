# tareas.py

tareas = []

def crear_tarea():
    descripcion = input("Ingrese una nueva tarea: ")
    tareas.append({"descripcion": descripcion, "completada": False})
    print("Tarea agregada correctamente.")

def listar_tareas():
    if not tareas:
        print("No hay tareas registradass" \
        "s.")
        return
    print("\nLista de tareas:")
    for idx, tarea in enumerate(tareas, start=1):
        estado = "" if tarea["completada"] else "❌"
        print(f"{idx}. {tarea['descripcion']} [{estado}]")
        
def completar_tarea():
    listar_tareas()
    try:
        num = int(input("\nIngrese el número de la tarea a completar: "))
        tareas[num - 1]["completada"] = True
        print(" Tarea marcada como completada.")
    except (IndexError, ValueError):
        print(" Número de tarea inválido.")

def eliminar_tarea():
    listar_tareas()
    try:
        num = int(input("\nIngrese el número de la tarea a eliminar: "))
        tareas.pop(num - 1)
        print(" Tarea eliminada.")
    except (IndexError, ValueError):
        print(" Número de tarea inválido.")
