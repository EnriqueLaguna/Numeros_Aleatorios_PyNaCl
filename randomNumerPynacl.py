import nacl.utils
import math

if __name__ == "__main__":

    input = int(input("Numero minimo de digitos de su numero: "))
    cantidad = math.floor((2 * math.log(input, 2)) - 2)

    if(cantidad < 1):
        i = 1
    else:
        i = cantidad

    random_byteString = nacl.utils.random(i)
    print(f"Random byteString = {random_byteString}")
    randomNumber = int.from_bytes(random_byteString, "big",signed=False)
    print(f"Numero aleatorio: {randomNumber}")