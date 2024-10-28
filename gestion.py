import os

productos = []

def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for line in file:
                try:
                    nombre, precio, cantidad = line.strip().split(", ")
                    productos.append({
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    })
                except ValueError:
                    print(f"Error al cargar el producto: {line.strip()}. Formato incorrecto.")

def guardar_datos():
    try:
        with open("productos.txt", "w") as file:
            for producto in productos:
                file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")
    except Exception as e:
        print(f"Error al guardar datos: {e}")

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    precio = input("Introduce el precio del producto: ")
    cantidad = input("Introduce la cantidad del producto: ")
    
    try:
        precio = float(precio)
        cantidad = int(cantidad)
        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })
        print("Producto añadido con éxito.")
    except ValueError:
        print("Error: El precio debe ser un número y la cantidad debe ser un entero.")

def ver_productos():
    if not productos:
        print("No hay produc
