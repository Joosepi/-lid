import random
import time

Name = input("Tere, mis su nimi on? ")

time.sleep(1)
print("Tere " + Name)

täna = input("Kuidas sul läinud on? ")
if "hästi" in täna:
    print("Tore! ")
elif "normilt" in täna: 
    print("See pole siis nii halb")
else:
    input("Kui on hästi miks nii aga kui sul on halb miks siis ka nii? ")