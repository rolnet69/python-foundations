print("-----------------------------------")
print("Ejercicio 7 - Combinar diccionarios")
print("-----------------------------------")

# Diccionario 1
print("\n--- DICCIONARIO 1 ---")
d1 = {}
while True:
    c = input("Clave: ")
    if c == "": break
    v = input("Valor: ")
    if v == "": break
    
    try:
        v = int(v)
    except:
        pass
    
    # Acumular en el propio diccionario
    if c in d1:
        if isinstance(d1[c], list):
            d1[c].append(v)
        else:
            d1[c] = [d1[c], v]
    else:
        d1[c] = v
print(d1)

# Diccionario 2
print("\n--- DICCIONARIO 2 ---")
d2 = {}
while True:
    c = input("Clave: ")
    if c == "": break
    v = input("Valor: ")
    if v == "": break
    
    try:
        v = int(v)
    except:
        pass
    
    # Acumular en el propio diccionario
    if c in d2:
        if isinstance(d2[c], list):
            d2[c].append(v)
        else:
            d2[c] = [d2[c], v]
    else:
        d2[c] = v
print(d2)

# Combinar
r = {}

# Pasar D1 al resultado (siempre como lista)
for c, v in d1.items():
    if isinstance(v, list):
        r[c] = v.copy()
    else:
        r[c] = [v]

# Fusionar D2
for c, v in d2.items():
    if c in r:
        if isinstance(v, list):
            r[c].extend(v)
        else:
            r[c].append(v)
    else:
        if isinstance(v, list):
            r[c] = v.copy()
        else:
            r[c] = [v]

# Mostrar resultado
print("\n" + "="*40)
print("RESULTADO")
print("="*40)
print("D1 =", d1)
print("D2 =", d2)
print("R  =", r)
print("="*40)