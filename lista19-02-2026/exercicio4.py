frase = "soma = 10 + 20 ;"
tokens = frase.split()

for t in tokens:
    if t == "=": print(f"{t} -> Atribuição")
    elif t == "+": print(f"{t} -> Operador")
    elif t == ";": print(f"{t} -> Fim de instrução")
    elif t.isdigit(): print(f"{t} -> Número")
    else: print(f"{t} -> Identificador")