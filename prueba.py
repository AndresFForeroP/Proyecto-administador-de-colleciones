import modules.f_coleccion as fc
diccionario = fc.leer_json('registros.json')
diccionario["libros"]['ñoño'] = diccionario['libros'].pop("ñeñe")
fc.escribir_json('registros.json',diccionario)