import json
import os

productos = []

def cargar_datos():
    """Carga los datos de productos desde un archivo si existe."""
    try:
        if os.path.exists('productos.txt'):
            with open('productos.txt', 'r') as file:
                global productos
                productos = json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print("Error al cargar los datos:", e)

def guardar_datos():
    """Guarda la lista de productos en un archivo."""
    try:
        with open('productos.txt', 'w') as file:
            json.dump(productos, file)
    except IOError as e:
        print("Error al guardar los datos:", e)

def añadir_producto():
    """Añade un nuevo producto a la lista."""
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un precio válido.")
    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, introduce una cantidad válida.")
    
    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    
    productos.append(producto)
    print(f"Producto '{nombre}' añadido con éxito.")

def ver_productos():
    """Muestra todos los productos."""
    if not productos:
        print("No hay productos en la lista.")
        return

    print("\nLista de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    print()

def actualizar_producto():
    """Actualiza un producto existente."""
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            nuevo_nombre = input("Introduce el nuevo nombre (dejar vacío para no cambiar): ")
            nuevo_precio = input("Introduce el nuevo precio (dejar vacío para no cambiar): ")
            nuevo_cantidad = input("Introduce la nueva cantidad (dejar vacío para no cambiar): ")

            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            if nuevo_precio:
                try:
                    producto['precio'] = float(nuevo_precio)
                except ValueError:
                    print("Precio no válido, no se actualizará.")
            if nuevo_cantidad:
                try:
                    producto['cantidad'] = int(nuevo_cantidad)
                except ValueError:
                    print("Cantidad no válida, no se actualizará.")

            print(f"Producto '{nombre}' actualizado con éxito.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto():
    """Elimina un producto de la lista."""
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado con éxito.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def menu():
    """Muestra el menú principal y gestiona las opciones."""
    cargar_datos()
    
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
