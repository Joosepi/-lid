import time
import random

nimi = input("Tere, mis su nimi on? ")

time.sleep(1)
print("Tere " + nimi)

täna = input("Kuidas sul täna läinud on? ")
if "hästi" in täna:
    print("Tore sama siin! ")
elif "normilt" in täna: 
    print("See polegi nii hull")
else:
    input("Oi mis juhtus? ")