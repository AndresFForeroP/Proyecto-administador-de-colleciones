import json
import os
import modules.Estructurasdatos as es
from modules.f_generales import limpiar_p,validartipo,pausar_p
import modules.menus as menus
import time as t
def leer_json(archivo):
    try:
        with open(archivo, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def actualizar_json(archivo,msg):
    diccionario = leer_json(archivo)
    diccionario.update(msg)
    escribir_json(archivo,diccionario)
def escribir_json(archivo,msg):
    with open(archivo,'w',encoding="utf-8") as file:
        json.dump(msg,file,indent=4,ensure_ascii=False)
def inizializar_archivo(archivo):
    if not os.path.isfile(archivo):
        escribir_json(archivo,es.estructura_inicializacion)
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
def mostrar_todo(archivo):
    print('Los libros guardados son')
    ver_libros(archivo)
    print('Las peliculas guardadas son')
    ver_peliculas(archivo)
    print('La musica guardada son')
    ver_musica(archivo)