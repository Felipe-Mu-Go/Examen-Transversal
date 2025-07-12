productos = {"8475HD":["HP", 15.6, "8GB", "DD", "IT", "Intel Core i5", "Nvidia GTX1050"],
            "2175HD":["Lenovo", 14, "4GB", "SSD", "512GB", "Intel COre i5", "Nvidia GTX1050"]}

stock = {"8475HD": [387990, 10], 
         "2175HD": [327990,4]}

def stock_marca(marca):
    contador = 0
    for clave, valor in productos.items():
        if marca.lower() in valor[0].lower():
            contador = contador + 1
            dato = stock[clave]
            print(f"El stock es: {dato[1]}")
    if contador == 0:
        print("Marca no encontrada")


def busquedaPrecio():
    contador = 0
    while True:
        try:
            monto_minimo = int(input("Ingrese monto minimo de busqueda: "))
            monto_maximo = int(input("Ingrese monto maximo de busqueda: "))
            break
        except ValueError:
            print("Ingrese caracter válido")
    for clave, valor in stock.items():
        if monto_minimo <= valor[0] <= monto_maximo:
            contador = contador + 1
            dato = productos[clave]
            print(f"Los Equipos entre losprecios consultados son: Marca {dato[0]} Modelo: {clave}")
    if contador == 0:
        print("No existen productos por ese precio")


def actualizarPrecio():
    codigo = str(input("Ingrese código de producto actualizar: ")).lower()
    encontrado = False
    for clave, valor in stock.items():
        if codigo == clave.lower():
            encontrado = True
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if nuevo_precio != 0:
                stock[clave][0] = nuevo_precio
                print("Precio cambiado con éxito")
            else:
                print("No se realiza cambio de precio")
    if encontrado == False:
        print("Producto no encontrado")

while True:
    print("*** MENU PRINCIPAL ***")
    print("1.- Stock Marca")
    print("2.- Busqueda por precio")
    print("3.- Actualizar Precio")
    print("4.- Salir")
    try:
        opcion = int(input("Elija una opción: "))
        if  opcion == 1:
            nombre_marca = input("Nombre de la Marca a buscar: ")
            stock_marca(nombre_marca)
        elif opcion == 2:
            busquedaPrecio()
        elif opcion == 3:
            actualizarPrecio()
        elif opcion == 4:
            print("Saliendo del programa, gracias")
            break
        else:
            print("Ingrese una opcion válida")
    except ValueError:
        print("Ingrese un caracter Válido")
