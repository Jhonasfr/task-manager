# main.py

import tareas

def menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tareas.crear_tarea()
        elif opcion == "2":
            tareas.listar_tareas()
        elif opcion == "3":
            tareas.completar_tarea()
        elif opcion == "4":
            tareas.eliminar_tarea()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    menu()
