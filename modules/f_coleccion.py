import json
import os
import modules.Estructurasdatos as es
from modules.f_generales import limpiar_p,validartipo,pausar_p
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