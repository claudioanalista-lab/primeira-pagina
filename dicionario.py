clientes = [
   {"nome":"Ana","cel":"1187872233", "empresa":"FIAT"},
   {"nome":"Pedro","cel":"119972233", "empresa":"INTEL"},
   {"nome":"Maria","cel":"1187874433", "empresa":"SEBRAE"},
   {"nome":"Felipe","cel":"11808072233", "empresa":"FIAT"},
]


# Pesquisa de um cliente pela empresa
empresa_digitada = input ("Digite o nome da empresa: ")
for cliente in clientes:
   if cliente["empresa"] == empresa_digitada:
       print (cliente)
      
# Cadastrar um novo cliente
print ("---- Cadastrando um novo CLIENTE ----")
nome = input ("Digite o nome do Cliente: ")
celular = input ("Digite o numero de celular do Cliente: ")
empresa = input ("Digite a empresa do Cliente: ")
novo_cliente = {
   "nome": nome,
   "cel": celular,
   "empresa": empresa
}
clientes.append(novo_cliente)
print (clientes)
      
# Remover um Cliente
print ("----> Removendo um Cliente pelo Nome <----")

nome_cliente = input ("Digite o nome do Cliente para remover: ")
for cliente in clientes:
    if cliente[nome] == novo_cliente:
       clientes.remove (cliente)
       break
 
print(clientes)    


