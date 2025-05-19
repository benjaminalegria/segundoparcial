#Hagamos un menu de gestión de temperaturas, una de las opciones es la numero uno: registrar la temperatura del día, mostrar la temperatura más alta, mostrar la temperatura
# más baja y numero 4 se sale
# Descripción del menu
#1- permitir que el usuario ingrese la temperatura en grados celsius,se debe ingresar un n° decimal o entero dentro del siguiente rango -30 a 50° celsius, se valida 
#con manejo de excepción que el usuario no ingrese texto u otro simbolo, si el usuario ingresa valores no numericos se debe mostrar el mensaje "Debe ingresar una temperatura valida" 
#y volver a la solicitud, si el valor esta fuera del rango permitido escriba "Temperatura fuera del rango, debe estar entre -30 a 50°C", si el valor es valido "Temperatura registrada con exito"
#opción 2: Mostrar la temperatura más alta y opción 3: mostrar la temperatura más baja, si el usuario no ha registrado temperatura debe colocar "El usuario no ha registrado ninguna temperatura"
#opción 4: "Gracias por usar nuestro sistema climatico, arrivederci(Hasta pronto)"


temperaturas = []
def registrar_temperatura():
    while True:
        try:
            temperaturas = input("ingrese la temperatura en grados celsius(-30 a 50°C) : ")
            temperaturas = float (temperaturas)
             
            if -30 <= temperaturas <= 50 :
                temperaturas (temperaturas)
                print("TEMPERATURA REGISTRADA CON EXITO")
                break
            else:
                print("temperaturafuera del rango, debe estar entre -30 a 50°C")
        except ValueError:
            print("debe ingresar una temperatura valida")           
def mostrar_temperatura_maxima():
    if temperaturas:
        print(f"la temperatura mas alta registrada es {MAX(temperaturas)}°C")
    else:
        print("EL USUARIO NO A REGISTRADO NIUNA TEMPERATURA")
def menu():
    while True:
        print("menu de gestion de tremperaturas")    
        print("1 refistrar temperatura del dia ")  
        print("2 mostrar la temperatura ma alta")  
        print("3mostar la temperatura mas baja")
        print("4. salir")

        opcion = input("selecione una opcion (1-4): ")
        
        if opcion == "1":
            registrar_temperatura()
        elif opcion == "2":
            mostrar_temperatura_maxima()
        elif opcion == "3":
            mostrar_temperatura_minima()
        elif opcion == "4":
            print("Gracias por usar nuestro sistema climático, arrivederci (Hasta pronto)")
            break
        else:
            print("Opción inválida, por favor seleccione entre 1 y 4")
