import random

piedra = 1
papel = 2
tijera = 3



contador= 0

print("""    JUEGO PPT
              Estas listo?""")
nombre_jugador= str(input("Ingresa tu nombre: "))

    
while contador <3:

    jugador= int(input("""Que elemento vas a elegir?
            Ingresa:
            1 PIEDRA 🪨 - 2 PAPEL 📃 - 3 TIJERA ✂️: 
            """))
    maquina = random.randint(0,3)

    if jugador == piedra or maquina ==piedra: 
        print("PIEDRA")
    elif jugador == papel or maquina ==papel:
        print("PAPEL")
    elif jugador == tijera or maquina == tijera:
        print("TIJERA")
    else:
        print("Numero no permitido. Ingrese un numero de 1 al 3")

    condicion1= jugador == piedra and maquina == tijera
    condicion2= jugador == papel and maquina == piedra
    condicion3= jugador == tijera and maquina == papel

    if condicion1 or condicion2 or condicion3:
        print (f"GANASTE {nombre_jugador}")
    elif jugador== maquina:
        print ("EMPATE")
    else:
        print (f"PERDISTE {nombre_jugador}")

    contador += 1

print("Gracias por jugar! " \
"      Esperamos te hayas divertido! 😉")

        

