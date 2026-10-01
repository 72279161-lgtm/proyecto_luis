import random

print("🎮 JUEGO: ADIVINA EL NÚMERO")
print("He pensado un número entre 1 y 100.")

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    try:
        numero = int(input("👉 Escribe tu número: "))
        intentos += 1

        if numero < numero_secreto:
            print("📈 El número es mayor.")
        elif numero > numero_secreto:
            print("📉 El número es menor.")
        else:
            print(f"🎉 ¡GANASTE! El número era {numero_secreto}.")
            print(f"🏆 Lo lograste en {intentos} intentos.")
            break

    except ValueError:
        print("❌ Escribe solamente un número.")