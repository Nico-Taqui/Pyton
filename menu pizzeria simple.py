def main():
    # Imprimir menú de opciones
    print("Bienvenido a la Pizzería!")
    print("Por favor, seleccione una opción:")
    print("1. Ver menú")
    print("2. Hacer un pedido")
    print("3. Salir")

    # Obtener la opción del usuario
    choice = int(input("Opción: "))
    
    # Ejecutar la opción seleccionada
    if choice == 1:
        show_menu()
        print("Opcion 1 (Hacer el pedido)")
        print("Opcion 2 (Volver al menu)")
        opcion = int(input("Desea ordenar algo mas?"))
        if opcion == 1:
            place_order()
        elif opcion == 2:
            main()
    elif choice == 2:
        place_order()
    elif choice == 3:
        print("Gracias por visitarnos!")
    else:
        print("Opción inválida.")

def show_menu():
    # Imprimir opciones de pizza
    print("Nuestras opciones de pizza incluyen:")
    print("1. Pepperoni")
    print("2. Vegetariana")
    print("3. Hawaiana")
    print("4. Suprema")
    

def place_order():
    # Obtener el número de pizza seleccionado
    choice = int(input("Seleccione el número de la pizza que desea: "))

    # Imprimir el pedido del usuario
    if choice == 1:
        print("Usted ha ordenado una pizza de Pepperoni.")
    elif choice == 2:
        print("Usted ha ordenado una pizza Vegetariana.")
    elif choice == 3:
        print("Usted ha ordenado una pizza Hawaiana.")
    elif choice == 4:
        print("Usted ha ordenado una pizza Suprema.")
    else:
        print("Opción inválida.")
    print("desea ordenar otra pizza?")
    print("Opcion 1 (Si)")
    print("Opcion 2 (No)")
    desicion = int(input(""))
    if desicion == 1:
        place_order()
    elif desicion == 2:
        main()
if __name__ == "__main__":
    main()
