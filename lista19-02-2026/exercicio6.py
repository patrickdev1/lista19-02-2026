senha_digitada = "1-2-3"
teclas = senha_digitada.split("-")
estado = 0

for tecla in teclas:
    if estado == 0 and tecla == "1":
        estado = 1
    elif estado == 1 and tecla == "2":
        estado = 2
    elif estado == 2 and tecla == "3":
        estado = 3
    else:
        estado = 0

if estado == 3:
    print("Acesso concedido!")
else:
    print("Acesso negado.")