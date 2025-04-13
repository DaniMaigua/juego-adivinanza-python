

import random

numero_secreto= random.randint(0,100)
contador= 0
contador_max=5
adivinanza = False

while not adivinanza:
    if not contador < contador_max:
        print(f"""¡GAME OVER! Te quedaste sin intentos.
            El numero secreto era ✨🪄 {numero_secreto}""")

    numero= int(input("Ingrese un numero del 0 al 99: "))

    if numero == numero_secreto:
        print("Felicidades! Adivinaste el numero secreto")
    elif numero < numero_secreto:
        print("El numero es menor al numero secreto")
    else:
        print("El numero es mayor al numero secreto")
    contador +=1

    


