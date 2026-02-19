A = [1, 2, 3]
B = [2, 3, 4]

uniao = A.copy()
for x in B:
    if x not in uniao:
        uniao.append(x)

intersecao = []
for x in A:
    if x in B:
        intersecao.append(x)

print(f"União: {uniao}")
print(f"Interseção: {intersecao}")