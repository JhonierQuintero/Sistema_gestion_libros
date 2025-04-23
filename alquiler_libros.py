import mostrar_libros
import biblioteca

usuarios={}

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