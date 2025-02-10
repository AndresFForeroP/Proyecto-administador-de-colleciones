import modules.f_generales as fg
import modules.menus as menus
import modules.f_coleccion as fc
import os
import json
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