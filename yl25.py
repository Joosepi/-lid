päevik = {
"eesnimi": "Martin Joosep",
"perenimi": "Reiljan",
"sünniaasta": "2005",
"Asukoht": "Kureaare",
"lemmik magustoit": "Hesburger"
}

print(päevik.get("Asukoht"))
print(päevik["Asukoht"])

päevik.update({"lemmik magustoit": "melon" })

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