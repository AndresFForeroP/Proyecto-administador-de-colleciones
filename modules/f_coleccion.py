import json
import os
import modules.Estructurasdatos as es
from modules.f_generales import limpiar_p,validartipo,pausar_p
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
            print('el equipo ya esta registrado')
        else:
            break
    autor = input(f'Ingrese el autor de {nombre_libro} ')
    genero = input(f'Ingrese el genero de {nombre_libro} ')
    valoracion = validartipo('int',f'Ingrese la valoracion de {nombre_libro} ')
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
    valoracion = validartipo('int',f'Ingrese la valoracion de {nombre_pelicula} ')
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
        nombre_musica = input('Ingrese el nombre de la pelicula que desea agregar ')
        if nombre_musica in diccionario['libros']:
            print('el equipo ya esta registrado')
        else:
            break
    autor = input(f'Ingrese el autor de {nombre_musica} ')
    genero = input(f'Ingrese el genero de {nombre_musica} ')
    valoracion = validartipo('int',f'Ingrese la valoracion de {nombre_musica} ')
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
su genero es {diccionario['libros'][libro]["genero"]} y lo valoraste con {diccionario['libros'][libro]["valoracion"]}
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
su genero es {diccionario['peliculas'][libro]["genero"]} y lo valoraste con {diccionario['peliculas'][libro]["valoracion"]}
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
su genero es {diccionario['musica'][libro]["genero"]} y lo valoraste con {diccionario['musica'][libro]["valoracion"]}
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
su genero es {diccionario['libros'][key]["genero"]} y lo valoraste con {diccionario['libros'][key]["valoracion"]} 
===============================================================""")
            t.sleep(0.5)
    for key in diccionario['peliculas']:
        if nombre_elemento == key:
            print(f"""
===============================================================
{nombre_elemento} es una pelicula su autor es {diccionario['peliculas'][key]["autor"]}
su genero es {diccionario['peliculas'][key]["genero"]} y lo valoraste con {diccionario['peliculas'][key]["valoracion"]} 
===============================================================""")
            t.sleep(0.5)
    for key in diccionario['musica']:
        if nombre_elemento == key:
            print(f"""
===============================================================
{nombre_elemento} es una cancion su autor es {diccionario['musica'][key]["autor"]}
su genero es {diccionario['musica'][key]["genero"]} y lo valoraste con {diccionario['musica'][key]["valoracion"]} 
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
su genero es {diccionario['libros'][key]["genero"]} y lo valoraste con {diccionario['libros'][key]["valoracion"]}
===============================================================""")
            t.sleep(0.5)
    for key,values in diccionario['peliculas'].items():
        if n_archivo == diccionario['peliculas'][key]['autor']:
            print(f"""
===============================================================
{key} es una pelicula su autor es {diccionario['peliculas'][key]["autor"]}
su genero es {diccionario['peliculas'][key]["genero"]} y lo valoraste con {diccionario['peliculas'][key]["valoracion"]} 
===============================================================""")
            t.sleep(0.5)
    for key,values in diccionario['musica'].items():
        if n_archivo == diccionario['musica'][key]['autor']:
            print(f"""
=============================================================== 
{key} es una cancion su autor es {diccionario['musica'][key]["autor"]}
su genero es {diccionario['musica'][key]["genero"]} y lo valoraste con {diccionario['musica'][key]["valoracion"]} 
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
su genero es {diccionario['libros'][key]["genero"]} y lo valoraste con {diccionario['libros'][key]["valoracion"]}
===============================================================""")
            t.sleep(0.5)
    for key,values in diccionario['peliculas'].items():
        if n_archivo == diccionario['peliculas'][key]['genero']:
            print(f"""
===============================================================
{key} es una pelicula su autor es {diccionario['peliculas'][key]["autor"]}
su genero es {diccionario['peliculas'][key]["genero"]} y lo valoraste con {diccionario['peliculas'][key]["valoracion"]} 
===============================================================""")
            t.sleep(0.5)
    for key,values in diccionario['musica'].items():
        if n_archivo == diccionario['musica'][key]['genero']:
            print(f"""
=============================================================== 
{key} es una cancion su autor es {diccionario['musica'][key]["autor"]}
su genero es {diccionario['musica'][key]["genero"]} y lo valoraste con {diccionario['musica'][key]["valoracion"]} 
===============================================================""")
            t.sleep(0.5)
    pausar_p()