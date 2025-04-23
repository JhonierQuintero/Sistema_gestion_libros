biblioteca={
    "Lord of mistery": {"disponible": 3, "genero": "misterio"},
    "La vida despues de la muerte": {"disponible": 2, "genero": "aventura"},
    "Shadow slave": {"disponible": 2, "genero": ",misterio"},
    "Reverend insanity": {"disponible": 1, "genero": "drama"},
    }

usuarios={}

def mostrar_libros ():
    print("-------LIBROS DISPONIBLES-------")
    for nombre_libro,info in biblioteca.items():
        print(f"{nombre_libro} : {info['disponible']} disponibles - genero: {info['genero']} ")

def alquilar_libro():
    nombre=input("ingrese el nombre del usuario\n").title()
    mostrar_libros()

    nombre_libro=input("ingrese el nombre del libro que desea alquilar\n").capitalize()

    if nombre_libro in biblioteca and biblioteca[nombre_libro]["disponible"]>0:
        fecha_devolucion=input("ingrese la fecha de devolucion del libro ej: 09/09/2023\n")

        if nombre not in usuarios:
            usuarios[nombre]=[]
        usuarios[nombre].append({'nombre': nombre_libro, 'fecha de devolucion': fecha_devolucion, "genero": biblioteca[nombre_libro]['genero']})
        
        biblioteca[nombre_libro]["disponible"]-=1
        print(f"nombre: {nombre_libro}, fecha de devolucion: {fecha_devolucion}")
    else:
        print(f"ese libro {nombre_libro} no existe o no esta disponible") 

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