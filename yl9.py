a = float(input("esimene külg: "))
b = float(input("teine külg: "))
c = float(input("alus külg: "))

if a == b == c:
    print("võrdkülgne")
elif (a <= 0) or (b <= 0) or (c <= 0):
    print("pole saadav")
elif a == b:
    print("võrdhaarne")
else:
    print("erikülgne")