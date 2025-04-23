from alquilar_libros import alquilar_libro
from mostrar_libros import mostrar_libros
from devolver_libros import devolver_libro

while True :
    print("-----ALQUILER DE LIBROS------")
    print("1. mostra libros\n2. alquilar libros\n3. regresar libros\n0. salir")
    opcion=int(input("ingrese la opcion escogida: "))

    if opcion== 1 :
        mostrar_libros()
    elif opcion == 2:
        alquilar_libro()
    elif opcion == 3 :
        devolver_libro()
    elif opcion == 0:
        break
    else:
        print("opcion incorrecta intente de nuevo")