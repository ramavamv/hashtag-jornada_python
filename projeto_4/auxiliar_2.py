# listas
lista_nova = []
nomes = ["Fulano", "Beltrano"]
print(nome[0])
nomes.append("Ciclano") # adiciona informações na lista
print(nomes)

# dicionario = {"chave":valor, "chave":valor}
# uma msg do python
# posso adicioonar várias infos para cada item
idades = {"Lira": 31, "Thalia": 23, "Alon": 45}
idades["Lira"] # como pega info no dicionario
idades["Michely"] = 25 # adicionando info

# role = a função do usuário no agente
# content = conteúdo
mensagem1 = {"role": "assistant", "content": "Bora aprender Python?"}
mensagem2 = {"role": "user", "content": "Bora sim"}
mensagem3 = {"role": "assistant", "content": "Então vamos começar a aula"}

lista_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role": "user", "content": "Bora"}
lista_mensagens.append(nova_mensagem)

print(lista_mensagens)