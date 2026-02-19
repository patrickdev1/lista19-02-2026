expressao = "(a + [b * c] - {d/e})"
pilha = []
pares = {')': '(', ']': '[', '}': '{'}

for char in expressao:
    if char in "([{":
        pilha.append(char)
    elif char in ")]}":
        if not pilha or pilha.pop() != pares[char]:
            print("Incorreto!")
            break
else:
    print("Correto!" if not pilha else "Incorreto!")