a = int(input ("Esimene number : "))
b = int(input ("Teine number: "))

def minimum(a, b):
      
    if a <= b:
        return a
    else:
        return b
      
print(minimum(a, b))