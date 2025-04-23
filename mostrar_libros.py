import biblioteca

def mostrar_libros ():
    print("-------LIBROS DISPONIBLES-------")
    for nombre_libro,info in biblioteca.items():
        print(f"{nombre_libro} : {info['disponible']} disponibles - genero: {info['genero']} ")