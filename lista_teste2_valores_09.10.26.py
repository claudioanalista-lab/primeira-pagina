valores = [20, 71, 100, 30]

def dobrar(valor):
    resultado = valor * 2
    return resultado

valores_novos = []
for valor in valores:
    valores_novos.append(dobrar(valor))

print(valores_novos)
