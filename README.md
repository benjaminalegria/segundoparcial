print("mama revisa estos 3 numeros")
lista = [5, 6, 7]

N_primo = 0 
N_N_Primo = 0 

def Es_primo (n): 
    if n <= 1:
        return False 
    for i in range (2, int(n / 2)+ 1):
        if n % 1 ==0:
            return False
    return True
        
#RECORDATORIO 

for 1, numero in enumerate(numero)
    print(f"{1+1} numero: {numero}", end="=>")
    if Es_primo(numero)
    print("es primo")
    N_primo +=1
else:
    print("no es primo")
    N_N_Primo +=1

#MOATRAR

print(f"/nResultado")
print(f"se ingresaron {N_primo} Numero primo")
print(f"ingreso: {N_N_Primo} numero {'S' if N_primo > 1 else}''} no primo . ]
