import biblioteca
from registro_usuarios import usuarios

def devolver_libro():
    nombre=input("ingrese el nombre del usuario\n").title()

    if nombre in usuarios and usuarios[nombre]:
        print("-------LIBRO ALQUILADO-------")
        for i , alquilados in enumerate (usuarios[nombre],1):
            print(f"{i}. {alquilados['nombre']} - fecha de devolucion {alquilados['fecha de devolucion']} genero: {alquilados['genero']}  ")

        indice=int(input("numero del libro que desea devolver: "))-1

        if 0 <= indice < len(usuarios[nombre]):
            modelo=usuarios[nombre][indice]["nombre"]
            biblioteca[modelo]["disponible"]+=1
            usuarios[nombre].pop(indice)
            print("el libro fue regresado de manera exitosa.")
        else :
            print("numero incorrecto del libro.")
    else :
        print("el cliente no tiene libros alquilados.")