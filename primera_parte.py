while True:
    a = 1
    task_desc = input(f"|describa la tarea a realizar, numero de tarea: {a}|  ")
    if not task_desc.strip():
        print("por favor, ingrese algun caracter")
    else:
        print(f"entendido! la tarea numero {a} sera {task_desc}")
        a += 1
    
    break