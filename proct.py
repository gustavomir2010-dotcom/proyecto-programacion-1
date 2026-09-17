def validar_entrada_numerica(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número válido.")


def eliminar_tarea(lista_tareas):
    id_tarea = validar_entrada_numerica("Ingrese el ID de la tarea a eliminar: ")

    for tarea in lista_tareas:
        if tarea["id"] == id_tarea:
            lista_tareas.remove(tarea)
            print("Tarea eliminada correctamente.")
            return

    print("Error: no existe una tarea con ese ID.")