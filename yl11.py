a = input("Pange siia midagi: ").strip()

if len(a)>= 7:
    if (len(a) % 2) == 0:
        print("Õige")
    else:
        print("Pole õige")

print(a[len(a)//2-1:len(a)//2+2])