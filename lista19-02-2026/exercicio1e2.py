altura = int(input("Digite a altura (máx 20): "))
if altura > 20: altura = 20

print("\nTriângulo")
for i in range(1, altura + 1):
    print("* " * i)

print("\nRetângulo")
for i in range(altura):
    print("* " * altura)

print("\nDiagonal")
for i in range(altura):
    print("  " * i + "* " * (altura - i))