import pyfiglet as py
import json as j
from typing import List, Dict

# Imprimir el nombre en grande
ascii_art = py.figlet_format("All-Mart")
print(ascii_art)
# Imprimir el eslogan debajo del nombre
print("Get it All-Mart")
Carrito: List[Dict[str, int]] = []
#Areas de la teinda 
ropa_delhombre = [    {        "Nombre": "Camisa Nike",        "Proveedor": "Nike",        "Fecha de caducidad": "N/A",        "Fecha de ingreso": "11/05/2023",        "detalles": "Camisa de algodon, tallas varias de hombre ,colores varios",        "precio": 50.00,        "unidades": 14    },    {        "Nombre": "Pans Adidas",        "Proveedor": "Adidas",        "Fecha de caducidad": "N/A",        "Fecha de ingreso": "11/05/2023",        "detalles": "Pans de algodon, tallas varias de hombre ,color Negro",        "precio": 75.00,        "unidades": 10    },    {        "Nombre": "Hoodie New Balance ",        "Proveedor": "New Balance",        "Fecha de caducidad": "N/A",        "Fecha de ingreso": "11/05/2023",        "detalles": "Hoodie con gorro , tallas varias de hombre ,colores Blanco y Negro",        "precio": 75.00,        "unidades": 12    }]
diccionario1 = {}
for item in ropa_delhombre:
    diccionario1[item["Nombre"]] = item
ropa_mujer=  [
                {
                    "Nombre": "Crop Top Nike",
                    "Proveedor": "Nike",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Camisa de algodon, tallas varias de mujer ,colores varios",
                    "precio": 50.00,
                    "unidades": 14
                },
                {
                    "Nombre": "Pans Nike",
                    "Proveedor": "Adidas",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Pans de algodon, tallas varias de mujer ,color Negro",
                    "precio": 75.00,
                    "unidades": 10
                },
                {
                    "Nombre": "Hoodie Reebok ",
                    "Proveedor": "New Balance",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Hoodie con gorro , tallas varias de mujer ,colores Blanco y Negro",
                    "precio": 75.00,
                    "unidades": 12
                }

            ]
diccionario2 = {}
for item in ropa_delhombre:
    diccionario2[item["Nombre"]] = item
calzado= [
                {
                    "Nombre": "Nike SB Dunk Orange Lobster",
                    "Proveedor": "Nike",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Zapatilla SB dunk, materiales en su mayoria y goma en la suela, tallas: 7.5, 8.5  , 9 , 10.5, 11",
                    "precio": 175.00,
                    "unidades": 5
                },
                {
                    "Nombre": "Yeezy 700 Wave Rnnr",
                    "Proveedor": "Adidas",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Zapato en su mayoria construido por tela mayada y paneles de gamuza y suela de espuma, con tecnologia boost",
                    "precio":275.00,
                    "Unidades":5
                }
            ]
diccionario3={}       
for item in calzado:
    diccionario3[item["Nombre"]] = item
Dispositivos_mobiles=[
                {
                    "Nombre": "Iphone 14 pro max",
                    "Proveedor": "Apple",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "pantalla oled 6.1 pulgadas, camara de 13 Megapixeles",
                    "precio": 1500.00,
                    "unidades": 5
                },
                {
                    "Nombre": "Samsung Note 20 Ultra",
                    "Proveedor": "Samsung",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Pantalla de 6.5 pulgadas amoled, lapiz penub ",
                    "precio": 1300,
                    "unidades": 5
                },
                {
                    "Nombre": "Huawei P40",
                    "Proveedor": "Huawei",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "pantalla de 6 pulgadas",
                    "precio": 500,
                    "unidades": 12
                }]
diccionario4={}
for item in Dispositivos_mobiles:
    diccionario4[item["Nombre"]] = item
Dispositivosmultimedia = [
                {
                    "Nombre": "Air pods pro",
                    "Proveedor": "Apple",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Auriculares inalambricos, blancos",
                    "precio": 250,
                    "unidades": 10
                },
                {
                    "Nombre": "Galaxy Buds Live",
                    "Proveedor": "Samsung",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Auriculares inalambricos cromados , con cancelacion de ruido activa",
                    "precio": 175,
                    "unidades": 10
                },
                {
                    "Nombre": "Parlante Sony",
                    "Proveedor": "Huawei",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Parlante SONY con luces led",
                    "precio": 230,
                    "unidades": 12
                }
            ]
diccionario5={}
for item in Dispositivosmultimedia:
    diccionario5[item["Nombre"]] = item
Electrodomesticos=[
                {
                    "Nombre": "Licuadora Oster",
                    "Proveedor": "Oster",
                    "Fecha de caducidad": "hasta que lo rompa xd",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Licuadora con vaso de vidrio 5 velocidades, y con diferentes funciones especiales",
                    "precio": 175,
                    "unidades":5
                },
                {
                    "Nombre": "Plancha Oster",
                    "Proveedor": "Oster",
                    "Fecha de caducidad": "N/A",
                    "Fecha de ingreso": "11/05/2023",
                    "detalles": "Plancha a vapor ",
                    "precio":275,
                    "Unidades":5
                }
            ]
diccionario6={}
for item in Electrodomesticos:
    diccionario6[item["Nombre"]] = item       
Vestimenta= [ropa_delhombre,ropa_mujer,calzado]
Electronica=[Dispositivos_mobiles,Electrodomesticos,Dispositivosmultimedia]
Areas = [Vestimenta,Electronica]
def programa_Admin():
        while True:
            print("\nBienvenido a la zona de almacenamiento de la tienda.")
            print("¿Qué acción desea realizar?")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Ver productos en la tienda")
            print("4.Salir")
            accion = int(input("Ingrese la opción deseada: "))
            if accion == 1:
                print("En que area desea agregar el producto?")
                opcionesarea= {"1. Vestimenta", "2. Electronica", "3. Salir"}
                for i in opcionesarea:
                    print(i)
                opcion_area_elegida = input("Ingrese la opción deseada: ")
                while True:
                    if opcion_area_elegida == "1":
                        print("¿En que categoria desea agregar el producto?")
                        opcioncategoriav = ("1. Ropa del hombre", "2. Ropa del mujer", "3. Calzado", "4. Salir")
                        for i in opcioncategoriav:
                            print(i)
                        opcion_categoria_elegida = input("Ingrese la opción deseada: ")
                        if opcion_categoria_elegida == "1":
                            print("Menu de ropa del hombre")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_caducidad = input("Ingrese la fecha de caducidad (en formato dd/mm/aaaa): ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de caducidad": fecha_caducidad, "Fecha de ingreso": fecha_ingreso, "Detalles del articulo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            ropa_delhombre.append(producto)
                            print("Producto agregado exitosamente.")
                            
                        elif opcion_categoria_elegida == "2":
                            print("Menu de ropa de mujer")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_caducidad = input("Ingrese la fecha de caducidad (en formato dd/mm/aaaa): ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de caducidad": fecha_caducidad, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            ropa_mujer.append(producto)
                            print("Producto agregado exitosamente.")
                        elif opcion_categoria_elegida == "3":
                            print("Menu de calzado")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_caducidad = input("Ingrese la fecha de caducidad (en formato dd/mm/aaaa): ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de caducidad": fecha_caducidad, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            calzado.append(producto)
                            print("Producto agregado exitosamente.")
                        elif opcion_categoria_elegida == "4":
                            return
                        else:
                            print("Opcion invalida")
                    elif opcion_area_elegida == "2":
                        print("Menu de electronica")
                        print("Elija en que categoria desea agregar el producto")
                        opcioneselectro = ("1.Dispositivos mobiles", "2.Electrodomesticos", "3.Dispositivos multimedia", "4. Salir")
                        for i in opcioneselectro:
                            print(i)
                        input("Ingrese la opción deseada: ")
                        if opcioneselectro == "1":
                            print("Menu de dispositivos mobiles")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_caducidad = input("Ingrese la fecha de caducidad (en formato dd/mm/aaaa): ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de caducidad": fecha_caducidad, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            Dispositivos_mobiles.append(producto)
                            print("Producto agregado exitosamente.")
                        elif opcioneselectro == "2":
                            print("Menu de electrodomesticos")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_caducidad = input("Ingrese la fecha de caducidad (en formato dd/mm/aaaa): ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de caducidad": fecha_caducidad, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            Electrodomesticos.append(producto)
                            print("Producto agregado exitosamente.")
                        elif opcioneselectro == "3":
                            print("Menu de dispositivos multimedia")
                            nombre = input("Ingrese el nombre del producto: ")
                            proveedor = input("Ingrese el nombre del proveedor: ")
                            fecha_caducidad = input("Ingrese la fecha de caducidad (en formato dd/mm/aaaa): ")
                            fecha_ingreso = input("Ingrese la fecha de ingreso a la tienda (en formato dd/mm/aaaa): ")
                            detalles = input("Ingrese detalles del artículo: ")
                            precio = float(input("Ingrese el precio del producto: "))
                            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
                            producto = {"Nombre": nombre, "Proveedor": proveedor, "Fecha de caducidad": fecha_caducidad, "Fecha de ingreso": fecha_ingreso, "Detalles del artículo": detalles, "Precio": precio, "Unidades disponibles": unidades}
                            Dispositivosmultimedia.append(producto)
                            print("Producto agregado exitosamente.")       
                        else:
                            print("Opcion invalida")
                    break
            elif accion == 2:
                print("en que area desea ingresar?")
                opcionborrar= ("1. Vestimenta", "2. Electronica", "3.Salir")
                for i in opcionborrar:
                    print(i)
                while True:
                    opcion_area_elegida = input("Ingrese la opción deseada: ")
                    while True:
                            if opcion_area_elegida == "1":
                                print("¿En que categoria desea eliminar el producto?")
                                opcioncategoriav = {"1. Ropa del hombre", "2. Ropa del mujer", "3. Calzado"}
                                for i in opcioncategoriav:
                                    print(i)
                                opcion_categoria_elegida = input("Ingrese la opción deseada: ")
                                if opcion_categoria_elegida == "1":
                                    print("Menu de ropa del hombre")
                                    for i in ropa_delhombre:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del ropa_delhombre[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(ropa_delhombre, indent=4))
                                    break
                                elif opcion_categoria_elegida == "2":
                                    print("Menu de ropa de mujer")
                                    for i in ropa_mujer:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del ropa_mujer[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(ropa_mujer, indent=4))
                                    break
                                elif opcion_categoria_elegida =="3":
                                    print("Menu de calzado ")
                                    for i in calzado:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del calzado[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(calzado, indent=4))
                                    break
                                else:
                                    print("Opcion invalida")
                            elif opcion_area_elegida == "2":
                                print("Menu de electronica")
                                print("Elija en que categoria desea agregar el producto")
                                opcioneselectro = ("1.Dispositivos mobiles", "2.Electrodomesticos", "3.Dispositivos multimedia", "4. Salir")
                                for i in opcioneselectro:
                                    print(i)
                                input("Ingrese la opción deseada: ")
                                if opcioneselectro == "1":
                                    print("Menu de dispositivos mobiles")
                                    for i in Dispositivos_mobiles:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del Dispositivos_mobiles[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(Dispositivos_mobiles, indent=4))
                                    break
                                elif opcioneselectro == "2":
                                    print("Menu de dispositivos mobiles")
                                    for i in Electrodomesticos:
                                        print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del Electrodomesticos[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(Electrodomesticos, indent=4))
                                    break
                                elif opcioneselectro == "3":
                                    print("Menu de dispositivos mobiles")
                                    for i in Dispositivosmultimedia:
                                            print(j.dumps(i, indent=4))
                                    eleccion = int(input("Elige una opcion de los disponibles este es el orden (0,1,2,3...) "))
                                    del Dispositivosmultimedia[eleccion]
                                    print("Producto eliminado exitosamente. La nueva lista de articulos disponibles\n")  
                                    print(j.dumps(Dispositivosmultimedia, indent=4))
                                    break
                                else: print("Opcion invalida")
                                break
                            else: print("Opcion invalida")
            elif accion == 3:
                print("Que accion desea realizar")
                while True:
                    opcionesmostrartienda= ["1.mostrar todos los productos", "2. Mostrar productos de un area en especifico", "3. Mostrar productos de una categoria especifica", "4. Salir"]
                    for i in opcionesmostrartienda:
                        print(i)
                    eleccion=input("Ingrese la opción deseada: ")
                    if eleccion == "1":
                        print("Mostrando todos los productos")
                        print(j.dumps(Areas, indent=4))
                    elif eleccion == "2":
                        print("Area que desea visualizar")
                        categorias = {"1. Vestimenta", "2.Electronica"}
                        for i in categorias:
                            print(i)
                        eleccion = input("Ingrese la opción deseada: ")
                        if eleccion == "1":
                            print("Mostrando todos los productos de la categoria Vestimenta")
                            print(j.dumps(Vestimenta, indent=4))
                            break
                        elif eleccion == "2":
                            print("Mostrando todos los productos de la categoria Electronica")
                            print(j.dumps(Electronica, indent=4))
                            break
                        else: print("Opcion invalida")
                    elif eleccion == "3":
                        print("Mostrando productos por categoria")
                        while True:
                            categoria = {"1. Ropa de hombre", "2.Ropa de  mujer ","3.Calzado ", "4.Dispositivos mobiles", "5.Electrodomesticos", "6.Dispositivos multimedia", "7. Salir"}
                            for i in categoria:
                                print(i)
                            eleccion = input("Ingrese la opción deseada: ")
                            if eleccion == "1":
                                print("Mostrando todos los productos de la categoria Ropa de hombre")
                                print(j.dumps(ropa_delhombre, indent=4))
                                break
                            elif eleccion =="2":
                                print("Mostrando todos los productos de la categoria Ropa de mujer")
                                print(j.dumps(ropa_mujer, indent=4))
                                break
                            elif eleccion =="3":
                                print("Mostrando todos los productos de la categoria Calzado")
                                print(j.dumps(calzado, indent=4))
                                break
                            elif eleccion =="4":
                                print("Mostrando todos los productos de la categoria Dispositivos mobiles")
                                print(j.dumps(Dispositivos_mobiles, indent=4))
                                break
                            elif eleccion =="5":
                                print("Mostrando todos los productos de la categoria Electrodomesticos")
                                print(j.dumps(Electrodomesticos, indent=4))
                                break
                            elif eleccion =="6":
                                print("Mostrando todos los productos de la categoria Dispositivos multimedia")
                                print(j.dumps(Dispositivosmultimedia, indent=4))
                                break
                            elif eleccion =="7":
                                return
                            
                            else: print("Opcion invalida")
                        return
                    elif eleccion == "4":
                        return  
                    else: print("Opcion invalida")     
            elif accion == 4:
                return

            else: print("Opcion invalida")
def programaGerente():
    print("Que accion desea realizar")
    while True:
        opcionesmostrartienda= ["1.mostrar todos los productos", "2. Mostrar productos de un area en especifico", "3. Mostrar productos de una categoria especifica", "4. Salir"]
        for i in opcionesmostrartienda:
            print(i)
        eleccion=input("Ingrese la opción deseada: ")
        if eleccion == "1":
            print("Mostrando todos los productos")
            print(j.dumps(Areas, indent=4))
        elif eleccion == "2":
            print("Area que desea visualizar")
            categorias = {"1. Vestimenta", "2.Electronica"}
            for i in categorias:
                print(i)
            eleccion = input("Ingrese la opción deseada: ")
            if eleccion == "1":
                print("Mostrando todos los productos de la categoria Vestimenta")
                print(j.dumps(Vestimenta, indent=4))
                break
            elif eleccion == "2":
                print("Mostrando todos los productos de la categoria Electronica")
                print(j.dumps(Electronica, indent=4))
                break
            else: print("Opcion invalida")
        elif eleccion == "3":
            print("Mostrando productos por categoria")
            while True:
                categoria = {"1. Ropa de hombre", "2.Ropa de  mujer ","3.Calzado ", "4.Dispositivos mobiles", "5.Electrodomesticos", "6.Dispositivos multimedia", "7. Salir"}
                for i in categoria:
                    print(i)
                eleccion = input("Ingrese la opción deseada: ")
                if eleccion == "1":
                    print("Mostrando todos los productos de la categoria Ropa de hombre")
                    print(j.dumps(ropa_delhombre, indent=4))
                    break
                elif eleccion =="2":
                    print("Mostrando todos los productos de la categoria Ropa de mujer")
                    print(j.dumps(ropa_mujer, indent=4))
                    break
                elif eleccion =="3":
                    print("Mostrando todos los productos de la categoria Calzado")
                    print(j.dumps(calzado, indent=4))
                    break
                elif eleccion =="4":
                    print("Mostrando todos los productos de la categoria Dispositivos mobiles")
                    print(j.dumps(Dispositivos_mobiles, indent=4))
                    break
                elif eleccion =="5":
                    print("Mostrando todos los productos de la categoria Electrodomesticos")
                    print(j.dumps(Electrodomesticos, indent=4))
                    break
                elif eleccion =="6":
                    print("Mostrando todos los productos de la categoria Dispositivos multimedia")
                    print(j.dumps(Dispositivosmultimedia, indent=4))
                    break
                elif eleccion =="7":
                    return
                                
                else: print("Opcion invalida")
            return
        elif eleccion == "4":
            menu_principal()
        else: print("Opcion invalida")
def programa_vendedor():
    print("Que accion desea realizar")
    while True:
        opcionesventa: List[str] = ["1.Agregar producto al carrito", "2.Eliminar producto del carrito", "3.Finalizar compra", "4.Salir"]
        for i in opcionesventa:
            print(i)
        eleccion: str = input("Ingrese la opción deseada: ")
        if eleccion == "1":
            print("A que area desea ingresar ? ")
            areas= ["1. Vestimenta", "2.Electronica", "3. Salir"]
            for i in areas:
                print(i)
            eleccion = input("Ingrese la opción deseada: ")
            if eleccion == "1":
                categorias={"1. Ropa de hombre", "2.Ropa de  mujer ","3.Calzado ", "4.Salir"}
                for i in categorias:
                    print(i)
                eleccion = input("Ingrese la opción deseada: ")
                if eleccion == "1":
                    print("Inventario Ropa de hombres")
                    productos = list(diccionario1.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario1[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            Carrito.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "2":
                    print("Inventario Ropa de Mujer ")
                    productos = list(diccionario2.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario2[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            Carrito.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "3":
                    print("Inventario calzado")
                    productos = list(diccionario3.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario3[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            Carrito.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "4":
                    return 
            elif eleccion == "2":
                categorias2={"1. Dispositivos mobiles", "2.Electrodomesticos", "3.Dispositivos multimedia", "4.Salir"}
                for i in categorias2:
                    print(i)
                eleccion = input("Ingrese la opción deseada: ")
                if eleccion == "1":
                    print("Inventario Dispositivos mobiles")
                    productos = list(diccionario2.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario2[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            Carrito.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "2":
                    print("Inventario Electrodomesticos")
                    productos = list(diccionario5.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario5[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))
                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            Carrito.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "3":
                    print("Menu Dispositivos multimedia")
                    productos = list(diccionario6.keys())
                    for i, producto in enumerate(productos):
                        precio:float = diccionario6[producto]
                        item = {
                            "Nombre": producto,
                            "precio":precio
                        }
                        print(j.dumps(f"{i+1}. {producto} - ${precio}", indent=4))

                    while True:
                            indice = int(input("Ingrese el número de índice del producto que desea agregar al carrito (o 0 para salir): "))
                            if indice == 0:
                                break
                            producto = productos[indice-1]
                            precio = diccionario1[producto]["precio"]
                            item = {
                                "Nombre": producto,
                                "precio": precio
                            }
                            Carrito.append(item)
                            print(f"{producto} ha sido agregado al carrito.")
                            print()
                elif eleccion == "4":
                    return
            elif eleccion == "3":
                return
        elif eleccion == "2":
            print("Borrar Articulos del Carrito")
            while True:
                print(j.dumps([item for item in Carrito], indent=4))
                eleccion_producto = input("¿Qué item deseas eliminar del carrito? (Ingresa 'q' para salir): ")
                if eleccion_producto.lower() == 'q':
                    break
                try:
                    eleccion_producto = int(eleccion_producto) - 1
                    eliminado = Carrito[eleccion_producto]
                    del Carrito[eleccion_producto]
                    print(f"El item {eliminado} ha sido eliminado del carrito.")
                except (ValueError, IndexError):
                    print("Entrada inválida. Ingresa un número de la lista o 'q' para salir.")
        elif eleccion == "3":
            ascii_art = py.figlet_format("Ticket")
            print(ascii_art)
            total = 0
            for i, item in enumerate(Carrito):
                precio = item["precio"]
                total += precio
                print(f"{i+1}. {item['Nombre']} - ${precio:.2f}")
            print(f"Total: ${total:.2f}")
            break
def menu_principal():
        while True:
            opciones = ["1. Administrador", "2. Gerente", "3. Empleado", "4. Salir"]
            print("Bienvenido al programa, ¿En qué nivel de acceso desea ingresar?")
            for i in opciones:
                print(i)
            inicio = input()
            if inicio == "1":
                while True:
                    print("Elija una opción\n")
                    opciones1 = ["1. Iniciar sesión", "2. Volver al menú"]
                    for i in opciones1:
                        print(i)
                    selector = input("Ingrese una opción: ")    
                    if selector == "1":
                        while True:
                            user_ = "admin"
                            pwd_ = "JLRD"
                            print('Introducir datos de administrador o escriba "s" para volver al menú')
                            print('Nombre de Usuario:')
                            user = input()
                            if user == "s":
                                menu_principal()
                            print('Contraseña:')
                            pwd = input()
                            if user == user_ and pwd == pwd_:
                                ascii_art = py.figlet_format("On-Line")
                                print(ascii_art)
                                print("Bienvenido administrador, ¿qué desea hacer hoy?")
                                programa_Admin()
                                break
                            else:
                                print("Usuario o contraseña incorrecto")
                        break
                    elif selector == "2":
                        menu_principal()
                    else:
                        print("Dato ingresado no aceptado, inténtelo otra vez")
            elif inicio == "2":
                while True:
                    print("Ingrese datos gerenciales")
                    gerente = "Carlos"
                    contragerente = "562"
                    gerent = input("Ingrese usuario: ")
                    if gerent == "s":
                        menu_principal()
                    contra = input("Ingrese contraseña: ")
                    if gerent == gerente and contra == contragerente:
                        ascii_art = py.figlet_format("On-Line")
                        print(ascii_art)
                        programaGerente()
                        break
                    else:
                        print("Datos erróneos")
            elif inicio == "3":
                print("Bienvenido Empleado")
                class user:
                    def __init__(self, nom, pwd):
                        self.nom = nom
                        self.pwd = pwd

                u1 = user("xavier", "123")
                u2 = user("Jeremy", "456")
                u3 = user("fatima", "789")
                u4 = user("Rene",   "780")
                trabajadores = [u1, u2, u3,u4]

                n = input("Ingrese su usuario o escriba s para volver al menú principal: ")
                if n == "s":
                    menu_principal()
                p = input("Ingrese contraseña: ")
                if p == "s":
                    menu_principal()
                k = 0
                for i in range(len(trabajadores)):
                    if trabajadores[i].nom == n and trabajadores[i].pwd == p:
                        ascii_art = py.figlet_format("On-Line")
                        print(ascii_art)
                        print(trabajadores[i].nom, "- Bienvenido al programa")
                        k = 1
                        programa_vendedor()
                        break

                if k == 0:
                    print("Intente nuevamente")
            elif inicio == "4":
                break
            else:
                print("Dato ingresado no aceptado, inténtelo otra vez")

menu_principal()
