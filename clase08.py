def ingresa_usuario(): 
    while True:
        user = input("ingrea usuario")
        if user not in d:
            break
        else:
            print("usuario entregado ya existe")
    while True:
        sex = input("ingrese sexo") 
        if sex == "m"or sex == "f":
            break
        else:
            print("ingrese sexo, selecsione M o F")
    while True:
        NUM =0 
        letra = 0
        passw = input("ingresa su contraseña:") 
        if len (passw) >=8:
            if " " not in passw:
                for c in passw:
                    if c in "0123456789":
                        NUM +=1 
                    if c in "abdc":
                        letra +=1
                if NUM > 0 and letra > 0:
                    print("contraseña valida")
                    d[user] =   {passw, sex}   
                    print("usuario ingresado correctamente") 




                    