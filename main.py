import modules.f_generales as fg
import modules.menus as menus
import modules.f_coleccion as fc
import os
ARCHIVO = os.path.join('data/','registros.json')
fc.inizializar_archivo(ARCHIVO)
menu_principal = 1
while menu_principal != 9:
    menu_principal = fg.validartipo('int',menus.administrar_coleccion)
    match menu_principal:
        case 1:
            menu_n_elemento = 1
            while menu_n_elemento != 9:
                menu_n_elemento = fg.validartipo('int',menus.añadir_elemento)
                match menu_n_elemento:
                    case 1:
                        fc.agregar_libro(ARCHIVO)
                    case 2:
                        fc.agregar_pelicula(ARCHIVO)
                    case 3:
                        fc.agregar_musica(ARCHIVO)
        case 2:
            menu_ver_elementos = 1
            while menu_ver_elementos != 9:
                menu_ver_elementos = fg.validartipo('int',menus.menu_ver_elementos)
                match menu_ver_elementos:
                    case 1:
                        fc.ver_libros(ARCHIVO)
                    case 2:
                        fc.ver_peliculas(ARCHIVO)
                    case 3:
                        fc.ver_musica(ARCHIVO)
        case 3:
            menu_buscar_elemento = 1
            while menu_buscar_elemento != 9:
                menu_buscar_elemento = fg.validartipo('int',menus.menu_buscar_elemento)
                match menu_buscar_elemento:
                    case 1:
                        fc.buscar_elemento_titulo(ARCHIVO)
                    case 2:
                        fc.buscar_elemento_artista(ARCHIVO)
                    case 3:
                        fc.buscar_elemento_genero(ARCHIVO)