import json
import os
import modules.Estructurasdatos as es
from modules.f_generales import limpiar_p,validartipo,pausar_p
import modules.menus as menus
import time as t
#permite cargar un archivo.json en un variable como un diccionario,esto permite trabajar
#con toda la informacion que tiene el json, si el archivo no se encuentra devuelve un
#diccionario vacio
def leer_json(archivo):
    try:
        with open(archivo, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
#Permite agregar informacion al diccionario,se almacena el archivo en un diccionario y luego
#luego se le agrega al diccionario, al final con la funcion escribir sobreescribe el archivo.json
def actualizar_json(archivo,msg):
    diccionario = leer_json(archivo)
    diccionario.update(msg)
    escribir_json(archivo,diccionario)
#Permite sobreescribir el archivo.json, casi siempre se le envia un diccionario para que
#lo sobreescriba al archivo original
def escribir_json(archivo,msg):
    with open(archivo,'w',encoding="utf-8") as file:
        json.dump(msg,file,indent=4,ensure_ascii=False)
#si el archivo no existe, crea el archivo con una estructura de iniciacion sencilla
#la estructura que se agrega al diccionario es dicionario = {libros:'',peliculas:'',musica:''}
def inizializar_archivo(archivo):
    if not os.path.isfile(archivo):
        escribir_json(archivo,es.estructura_inicializacion)
#carga el archivo.json, luego pide los datos necesarios crea un diccionario con los datos
#al final se le agrega al diccionario.json el diccionario con los datos que le pedimos al usurio
#y sobreescribe el archivo original
def agregar_libro(archivo):
    diccionario = leer_json(archivo)
    while True:
        nombre_libro = input('Ingrese el nombre del libro que desea agregar ')
        if nombre_libro in diccionario['libros']:
            print('el libro ya esta registrado')
        else:
            break
    autor = input(f'Ingrese el autor de {nombre_libro} ')
    genero = input(f'Ingrese el genero de {nombre_libro} ')
    valoracion = validartipo('int',f'Ingrese la valoracion de {nombre_libro} (1-100) ')
    while valoracion < 1 or valoracion > 100:
        print('la valoracion solo es entre (1-100)')
        valoracion = validartipo('int',f'Ingrese la valoracion de {nombre_libro} (1-100)')
    nuevo_libro = {nombre_libro:{
    'autor':autor,
    'genero':genero,
    'valoracion':valoracion }}
    diccionario['libros'].update(nuevo_libro)
    escribir_json(archivo,diccionario)
    print((f"✅ {nombre_libro} agregado exitosamente"))
    pausar_p()
    limpiar_p()
#es casi la misma funcion que la de agregar libro y la misma que se va a usar con la musica
#solo que llena los datos para las peliculas
def agregar_pelicula(archivo):
    diccionario = leer_json(archivo)
    while True:
        nombre_pelicula = input('Ingrese el nombre de la pelicula que desea agregar ')
        if nombre_pelicula in diccionario['libros']:
            print('el equipo ya esta registrado')
        else:
            break
    autor = input(f'Ingrese el autor de {nombre_pelicula} ')
    genero = input(f'Ingrese el genero de {nombre_pelicula} ')
    valoracion = validartipo('int',f'Ingrese la valoracion de {nombre_pelicula} (1-100)')
    while valoracion < 1 or valoracion > 100:
        print('la valoracion solo es entre (1-100)')
        valoracion = validartipo('int',f'Ingrese la valoracion de {nombre_pelicula} (1-100)')
    nueva_peli = {nombre_pelicula:{
    'autor':autor,
    'genero':genero,
    'valoracion':valoracion }}
    diccionario['peliculas'].update(nueva_peli)
    escribir_json(archivo,diccionario)
    print((f"✅ {nombre_pelicula} agregado exitosamente"))
    pausar_p()
    limpiar_p()
def agregar_musica(archivo):
    diccionario = leer_json(archivo)
    while True:
        nombre_musica = input('Ingrese el nombre de la cansion que desea agregar ')
        if nombre_musica in diccionario['libros']:
            print('el equipo ya esta registrado')
        else:
            break
    autor = input(f'Ingrese el autor de {nombre_musica} ')
    genero = input(f'Ingrese el genero de {nombre_musica} ')
    valoracion = validartipo('int',f'Ingrese la valoracion de {nombre_musica} (1-100)')
    while valoracion < 1 or valoracion > 100:
        print('la valoracion solo es entre (1-100)')
        valoracion = validartipo('int',f'Ingrese la valoracion de {nombre_musica} (1-100)')
    nueva_musica = {nombre_musica:{
    'autor':autor,
    'genero':genero,
    'valoracion':valoracion }}
    diccionario['musica'].update(nueva_musica)
    escribir_json(archivo,diccionario)
    print((f"✅ {nombre_musica} agregado exitosamente"))
    pausar_p()
    limpiar_p()
#esta funcion como las la de ver peliculas y musica recorre el diccionario de su 
#determinada catergoria y va imprimiendo la informacion de cada elemento
def ver_libros(archivo):
    diccionario = leer_json(archivo)
    n_libro = 1
    for libro in diccionario["libros"]:
        print(f"""
===============================================================             
El libro #{n_libro} se llama {libro} su autor es {diccionario['libros'][libro]["autor"]}
su genero es {diccionario['libros'][libro]["genero"]} y lo valoraste con {diccionario['libros'][libro]["valoracion"]}/100
===============================================================""")
        n_libro += 1
        t.sleep(0.5)
    pausar_p()
def ver_peliculas(archivo):
    diccionario = leer_json(archivo)
    n_libro = 1
    for libro in diccionario["peliculas"]:
        print(f"""
===============================================================             
La pelicula #{n_libro} se llama {libro} su autor es {diccionario['peliculas'][libro]["autor"]}
su genero es {diccionario['peliculas'][libro]["genero"]} y lo valoraste con {diccionario['peliculas'][libro]["valoracion"]}/100
===============================================================""")
        n_libro += 1
        t.sleep(0.5)
    pausar_p()
def ver_musica(archivo):
    diccionario = leer_json(archivo)
    n_libro = 1
    for libro in diccionario["musica"]:
        print(f"""
===============================================================             
La cancion #{n_libro} se llama {libro} su autor es {diccionario['musica'][libro]["autor"]}
su genero es {diccionario['musica'][libro]["genero"]} y lo valoraste con {diccionario['musica'][libro]["valoracion"]}/100
===============================================================""")
        n_libro += 1
        t.sleep(0.5)
    pausar_p()
#esta funcion le pide al usuario el titulo que desea buscar,luego si lo encuentra
#en cualquier categoria imprime los datos del elemento buscado
#esta funcion es casi igual para los otros datos como autor y genero
def buscar_elemento_titulo(archivo):
    nombre_elemento = input('Ingrese el nombre del titulo que desea buscar ')
    diccionario = leer_json(archivo)
    for key in diccionario['libros']:
        if nombre_elemento == key:
            print(f"""
===============================================================
{nombre_elemento} es un libro su autor es {diccionario['libros'][key]["autor"]}
su genero es {diccionario['libros'][key]["genero"]} y lo valoraste con {diccionario['libros'][key]["valoracion"]}/100 
===============================================================""")
            t.sleep(0.5)
    for key in diccionario['peliculas']:
        if nombre_elemento == key:
            print(f"""
===============================================================
{nombre_elemento} es una pelicula su autor es {diccionario['peliculas'][key]["autor"]}
su genero es {diccionario['peliculas'][key]["genero"]} y lo valoraste con {diccionario['peliculas'][key]["valoracion"]}/100 
===============================================================""")
            t.sleep(0.5)
    for key in diccionario['musica']:
        if nombre_elemento == key:
            print(f"""
===============================================================
{nombre_elemento} es una cancion su autor es {diccionario['musica'][key]["autor"]}
su genero es {diccionario['musica'][key]["genero"]} y lo valoraste con {diccionario['musica'][key]["valoracion"]}/100
===============================================================""")
            t.sleep(0.5)
    pausar_p()
#tanto para esta funcion como la de genero se usa una iteracion en el diccionario
#con .items para llegar hasta los datos que queremos llegar
def buscar_elemento_artista(archivo):
    n_archivo = input('Ingrese el nombre del artista/director o autor del cual desea buscar sus elementos ')
    diccionario = leer_json(archivo)
    for key,values in diccionario['libros'].items():
        if n_archivo == diccionario['libros'][key]['autor']:
            print(f""" 
===============================================================
{key} es un libro su autor es {diccionario['libros'][key]["autor"]}
su genero es {diccionario['libros'][key]["genero"]} y lo valoraste con {diccionario['libros'][key]["valoracion"]}/100
===============================================================""")
            t.sleep(0.5)
    for key,values in diccionario['peliculas'].items():
        if n_archivo == diccionario['peliculas'][key]['autor']:
            print(f"""
===============================================================
{key} es una pelicula su autor es {diccionario['peliculas'][key]["autor"]}
su genero es {diccionario['peliculas'][key]["genero"]} y lo valoraste con {diccionario['peliculas'][key]["valoracion"]}/100 
===============================================================""")
            t.sleep(0.5)
    for key,values in diccionario['musica'].items():
        if n_archivo == diccionario['musica'][key]['autor']:
            print(f"""
=============================================================== 
{key} es una cancion su autor es {diccionario['musica'][key]["autor"]}
su genero es {diccionario['musica'][key]["genero"]} y lo valoraste con {diccionario['musica'][key]["valoracion"]}/100 
===============================================================""")
            t.sleep(0.5)
    pausar_p()
def buscar_elemento_genero(archivo):
    n_archivo = input('Ingrese el nombre del genero del cual desea buscar sus elementos ')
    diccionario = leer_json(archivo)
    for key,values in diccionario['libros'].items():
        if n_archivo == diccionario['libros'][key]['genero']:
            print(f""" 
===============================================================
{key} es un libro su autor es {diccionario['libros'][key]["autor"]}
su genero es {diccionario['libros'][key]["genero"]} y lo valoraste con {diccionario['libros'][key]["valoracion"]}/100
===============================================================""")
            t.sleep(0.5)
    for key,values in diccionario['peliculas'].items():
        if n_archivo == diccionario['peliculas'][key]['genero']:
            print(f"""
===============================================================
{key} es una pelicula su autor es {diccionario['peliculas'][key]["autor"]}
su genero es {diccionario['peliculas'][key]["genero"]} y lo valoraste con {diccionario['peliculas'][key]["valoracion"]}/100 
===============================================================""")
            t.sleep(0.5)
    for key,values in diccionario['musica'].items():
        if n_archivo == diccionario['musica'][key]['genero']:
            print(f"""
=============================================================== 
{key} es una cancion su autor es {diccionario['musica'][key]["autor"]}
su genero es {diccionario['musica'][key]["genero"]} y lo valoraste con {diccionario['musica'][key]["valoracion"]}/100
===============================================================""")
            t.sleep(0.5)
    pausar_p()
#esta funcion pide al usuario el elemento que desea eliminar por el titulo
#revisa en cada key de categorias para saber en cual esta, luego pide 
#el nombre nuedo que le quiere poner al elemento usa las keys del diccionario y hace el cambio con .pop()
def editar_titulo(archivo):
    diccionario = leer_json(archivo)
    esta = False
    n_elemento = input('Ingrese el titulo del elemento que desea editar ')
    if n_elemento in diccionario['libros']:
        esta = True
        print(f'{n_elemento} es un libro ')
        n_nombre = input(f'Ingrese el nuevo titulo de {n_elemento} ')
        diccionario['libros'][n_nombre] = diccionario['libros'].pop(n_elemento)
        print((f"✅ {n_elemento} cambiado a {n_nombre} exitosamente"))
    if n_elemento in diccionario['peliculas']:
        esta = True
        print(f'{n_elemento} es una pelicula')
        n_nombre = input(f'Ingrese el nuevo titulo de {n_elemento} ')
        diccionario['peliculas'][n_nombre] = diccionario['peliculas'].pop(n_elemento)
        print((f"✅ {n_elemento} cambiado a {n_nombre} exitosamente"))
    if n_elemento in diccionario['musica']:
        esta = True
        print(f'{n_elemento} es una cancion ')
        n_nombre = input(f'Ingrese el nuevo titulo de {n_elemento} ')
        diccionario['musica'][n_nombre] = diccionario['musica'].pop(n_elemento)
        print((f"✅ {n_elemento} cambiado a {n_nombre} exitosamente"))
    if esta == False:
        print('el elemento no esta')
    else:
        escribir_json(archivo,diccionario)
#Tanto esta funcion como la de genero  y la de valoracion sirve casi igual que la de titulo
#pero esta entra mas profundo en el diccionario para poder editar el dato exacto
def editar_autor(archivo):
    diccionario = leer_json(archivo)
    esta = False
    n_elemento = input('Ingrese el titulo del elemento del cual desea editar el autor ')
    if n_elemento in diccionario['libros']:
        esta = True
        print(f'{n_elemento} es un libro y su autor es {diccionario['libros'][n_elemento]['autor']}')
        n_nombre = input(f'Ingrese el nombre del nuevo autor de {n_elemento} ')
        diccionario['libros'][n_elemento]['autor'] = n_nombre
        print((f"✅ {n_elemento} a cambiado su autor a {n_nombre} exitosamente"))
    if n_elemento in diccionario['peliculas']:
        esta = True
        print(f'{n_elemento} es una pelicula y su autor es {diccionario['peliculas'][n_elemento]['autor']}')
        n_nombre = input(f'Ingrese el nombre del nuevo autor de {n_elemento} ')
        diccionario['peliculas'][n_elemento]['autor'] = n_nombre
        print((f"✅ {n_elemento} a cambiado su autor a {n_nombre} exitosamente"))
    if n_elemento in diccionario['musica']:
        esta = True
        print(f'{n_elemento} es una cancion y su autor es {diccionario['musica'][n_elemento]['autor']} ')
        n_nombre = input(f'Ingrese el nuevo titulo de {n_elemento} ')
        diccionario['musica'][n_elemento]['autor'] = n_nombre
        print((f"✅ {n_elemento} a cambiado a su autor por {n_nombre} exitosamente"))
    if esta == False:
        print('el elemento no esta')
    else:
        escribir_json(archivo,diccionario)
def editar_genero(archivo):
    diccionario = leer_json(archivo)
    esta = False
    n_elemento = input('Ingrese el titulo del elemento del cual desea editar el genero ')
    if n_elemento in diccionario['libros']:
        esta = True
        print(f'{n_elemento} es un libro y su genero es {diccionario['libros'][n_elemento]['genero']}')
        n_nombre = input(f'Ingrese el nombre del nuevo genero de {n_elemento} ')
        diccionario['libros'][n_elemento]['genero'] = n_nombre
        print((f"✅ {n_elemento} a cambiado su genero a {n_nombre} exitosamente"))
    if n_elemento in diccionario['peliculas']:
        esta = True
        print(f'{n_elemento} es una pelicula y su genero es {diccionario['peliculas'][n_elemento]['genero']}')
        n_nombre = input(f'Ingrese el nombre del nuevo genero de {n_elemento} ')
        diccionario['peliculas'][n_elemento]['genero'] = n_nombre
        print((f"✅ {n_elemento} a cambiado su genero a {n_nombre} exitosamente"))
    if n_elemento in diccionario['musica']:
        esta = True
        print(f'{n_elemento} es una cancion y su genero es {diccionario['musica'][n_elemento]['genero']} ')
        n_nombre = input(f'Ingrese el nuevo genero de {n_elemento} ')
        diccionario['musica'][n_elemento]['genero'] = n_nombre
        print((f"✅ {n_elemento} a cambiado a su genero por {n_nombre} exitosamente"))
    if esta == False:
        print('el elemento no esta')
    else:
        escribir_json(archivo,diccionario)
def editar_valoracion(archivo):
    diccionario = leer_json(archivo)
    esta = False
    n_elemento = input('Ingrese el titulo del elemento del cual desea editar la valoracion ')
    if n_elemento in diccionario['libros']:
        esta = True
        print(f'{n_elemento} es un libro y su valoracion es {diccionario['libros'][n_elemento]['valoracion']}')
        n_nombre = int(input(f'Ingrese la nueva valoracion de {n_elemento} '))
        while n_nombre < 1 or n_nombre > 100:
            print('la valoracion solo es entre (1-100)')
            n_nombre = int(input(f'Ingrese la nueva valoracion de {n_elemento} '))
        diccionario['libros'][n_elemento]['valoracion'] = n_nombre
        print((f"✅ {n_elemento} a cambiado su valoracion a {n_nombre} exitosamente"))
    if n_elemento in diccionario['peliculas']:
        esta = True
        print(f'{n_elemento} es una pelicula y su valoracion es {diccionario['peliculas'][n_elemento]['valoracion']}')
        n_nombre = int(input(f'Ingrese la nueva valoracion de {n_elemento} '))
        while n_nombre < 1 or n_nombre > 100:
            print('la valoracion solo es entre (1-100)')
            n_nombre = int(input(f'Ingrese la nueva valoracion de {n_elemento} '))
        diccionario['peliculas'][n_elemento]['valoracion'] = n_nombre
        print((f"✅ {n_elemento} a cambiado su valoracion a {n_nombre} exitosamente"))
    if n_elemento in diccionario['musica']:
        esta = True
        print(f'{n_elemento} es una cancion y su valoracion es {diccionario['musica'][n_elemento]['valoracion']} ')
        n_nombre = int(input(f'Ingrese la nueva valoracion de {n_elemento} '))
        while n_nombre < 1 or n_nombre > 100:
            print('la valoracion solo es entre (1-100)')
            n_nombre = int(input(f'Ingrese la nueva valoracion de {n_elemento} '))
        diccionario['musica'][n_elemento]['valoracion'] = n_nombre
        print((f"✅ {n_elemento} a cambiado a su valoracion por {n_nombre} exitosamente"))
    if esta == False:
        print('el elemento no esta')
    else:
        escribir_json(archivo,diccionario)
#esta funcion elimina, pide en que categoria este el elemento que deseas elimiar y luego con la funcion.pop()
#elimina el elemnto que el usuario indica
def eliminar_elemento(archivo):
    diccionario = leer_json(archivo)
    tipo = validartipo('int',menus.menu_elegir_tipo )
    titulo = input('ingrese el titulo del elemento que desea eliminar ')
    match tipo:
        case 1:
            if titulo not in diccionario['libros']:
                print(f'{titulo} no existe en la categoria de libros')
            else:
                diccionario['libros'].pop(titulo)
                print((f"✅ {titulo} se ha eliminado exitosamente de la categoria de libros"))
        case 2:
            if titulo not in diccionario['peliculas']:
                print(f'{titulo} no existe en la categoria de peliculas')
            else:
                diccionario['peliculas'].pop(titulo)
                print((f"✅ {titulo} se ha eliminado exitosamente de la categoria de peliculas"))
        case 3:
            if titulo not in diccionario['musica']:
                print(f'{titulo} no existe en la categoria de musica')
            else:
                diccionario['musica'].pop(titulo)
                print((f"✅ {titulo} se ha eliminado exitosamente de la categoria de musica "))
#esta funcion usa las funciones de ver libros,ver peliculas y ver musica para mostrar todo lo que contiene
#la coleccion
def mostrar_todo(archivo):
    print('Los libros guardados son')
    ver_libros(archivo)
    print('Las peliculas guardadas son')
    ver_peliculas(archivo)
    print('La musica guardada son')
    ver_musica(archivo)