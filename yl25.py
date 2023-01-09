päevik = {
"eesnimi": "Martin Joosep",
"perenimi": "Reiljan",
"sünniaasta": "2005",
"elukoht": "Albu",
"lemmik magustoit": "Im the biggest bird"
}

print(päevik.get("elukoht"))
print(päevik["elukoht"])

päevik.update({"lemmik magustoit": "watermelon" })

print(päevik.keys())

print(päevik.values())

if 'isikukood' in päevik :
    print("On isikukood")
else:
    print("Pole isikukoodi")

print(len(päevik))

päevik.update({"pikkus": len(päevik)})

päevik.pop("sünniaasta")

del päevik