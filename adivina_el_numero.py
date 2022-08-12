import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_alegido = int(input("elige un numero del 1 al 100: "))
    while numero_alegido != numero_aleatorio:
        if numero_alegido < numero_aleatorio:
            print("Busca un numero mas alto")
        else:
            print("Busca un numero mas bajo")
        numero_alegido = int(input("Elige otro numero: "))
    print("GANASTE")


if __name__ == '__main__':
    run()