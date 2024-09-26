def main():
    name = ''
    last_name = ''

    while not name:
        name = input("¿Cúal es su primer nombre? > ")
        if not name:
            print("Ingrese un nombre.")
    
    while not last_name:
        last_name = input("¿Cúal es su apellido? > ")
        if not last_name:
            print("Ingrese un apelido.")
   
    print(f"Hola {name} {last_name}!")


if __name__ == '__main__':
    main()