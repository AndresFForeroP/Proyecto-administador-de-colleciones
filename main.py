import modules.f_generales as fg
import modules.menus as menus
import modules.f_coleccion as fc
import os
#Se especifica la ubicacion y el nombre del archivo que se va a usar durante todo el programa
ARCHIVO = os.path.join('data/','registros.json')
#se inicializa el archivo
fc.inizializar_archivo(ARCHIVO)
menu_principal = 1
while menu_principal != 9:
    #estas validaciones se usan durante todo el codigo para validar que el usuario solo ingrese el tipo de dato que quiero
    #y en cada menu se usa un match para seleccionar las opciones
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
            fc.mostrar_todo(ARCHIVO)
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
        case 4:
            menu_editar_elemento = 1
            while menu_editar_elemento != 9:
                menu_editar_elemento = fg.validartipo('int',menus.menu_editar_elemento)
                match menu_editar_elemento:
                    case 1:
                        fc.editar_titulo(ARCHIVO)
                    case 2:
                        fc.editar_autor(ARCHIVO)
                    case 3:
                        fc.editar_genero(ARCHIVO)
                    case 4:
                        fc.editar_valoracion(ARCHIVO)
        case 5:
            fc.eliminar_elemento(ARCHIVO)
        case 6:
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
print('SALISTE DEL PROGRAMA')