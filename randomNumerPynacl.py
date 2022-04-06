import nacl.utils
import math

if __name__ == "__main__":

    num_bytes = int(input("Numero de bytes para su numero: "))

    random_byteString = nacl.utils.random(num_bytes)
    print(f"Random byteString = {random_byteString}")
    randomNumber = int.from_bytes(random_byteString, "big",signed=False)
    print(f"Numero aleatorio: {randomNumber}")