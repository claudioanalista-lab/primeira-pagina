#notas = [7.0, 1.5, 10.0, 8.5, 3.0, 5.5, 3.9, 4.5]

# contador = 0
# limite = len(notas) -1

# while contador <= limite:
#    print (f"Sua nota é: {notas[contador]}")
#    contador += 1

#--------------------------------------------
# notas = [7.0, 1.5, 10.0, 8.5, 3.0, 5.5, 3.9, 4.5]

# for x in notas:
#     print(f"Sua nota é: {x}")
#--------------------------------------------
    
    
    
# Lista inicial de notas
notas = [7.0, 1.5, 10.0, 8.5, 3.0, 5.5, 3.9, 4.5]

print("--- 1. ADICIONANDO UM ELEMENTO ---")
notas.append(9.0)  # Adiciona 9.0 no final
notas.insert(0, 6.0)  # Adiciona 6.0 na posição (índice) 0
print("Após adicionar:", notas)

print("\n--- 2. MODIFICANDO UM ELEMENTO ---")
notas[1] = 8.0  # Altera o elemento do índice 1 para 8.0
print("Após modificar o índice 1:", notas)

print("\n--- 3. EXCLUINDO UM ELEMENTO ---")
notas.pop()  # Remove o último elemento
notas.remove(1.5)  # Remove a primeira ocorrência do valor 1.5
del notas[0]  # Remove o elemento do índice 0
print("Após excluir elementos:", notas)

print("\n--- EXIBINDO AS NOTAS FINAIS COM O LOOP FOR ---")
for x in notas:
  print(f"Sua nota é: {x}")
