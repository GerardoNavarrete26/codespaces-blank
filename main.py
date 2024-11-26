contador = 0
suma = 0
nombre = input("Escribe tu nombre :")
apellido = input("Escribe tu apellido :")
nombrecompleto = nombre + " " + apellido
print(f"Hola, {nombrecompleto}. Como estas ?") 

def suma_numeros():
    
    cantidad = int(input("¿Cuántos números deseas sumar? "))
    total = 0 
    
    for i in range(cantidad):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        total += numero 
    
    print(f"La suma total es: {total}")

suma_numeros()
