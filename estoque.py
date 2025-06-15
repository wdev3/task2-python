class estoque:
    def __init__(self, quantidade = 0):
        self.quantidade = quantidade

    def adicionar(self, adicao):
        self.quantidade += adicao

    def remover(self, remocao):
        if remocao <= self.quantidade:
            print ("Estoque removido")
            self.quantidade -= (remocao)
        else:
            print("Nao foi possivel remover essa quantidade")

    def mostrar(self):
        print (F"Estoque atual: {self.quantidade}")

def menu():
    print ("1 - adicionar produto ao estoque")
    print ("2 - remover produto do estoque")
    print ("3 - mostrar estoque atual")
    print ("4 - sair")



add = estoque(0)

menu()
try:
 while True:
  pergunta = int(input(""))
  if pergunta == 1:
    print ("Digite o valor que deseja adiconar ao estoque: ")
    pergunta_adicionar_estoque = int(input("\n"))
    add.adicionar (pergunta_adicionar_estoque)
    print (f"O valor {pergunta_adicionar_estoque} foi adicionado ao estoque")
    menu()

  if pergunta == 2:
    print("Digite o valor que deseja remover do estoque: ")
    pergunta_remover_estoque = int(input("\n"))
    add.remover(pergunta_remover_estoque)
    print (f"O valor foi {pergunta_remover_estoque} foi removido do estoque")
    menu()

  if pergunta == 3:
    add.mostrar()
    menu()

  if pergunta == 4:
    print ("Programa encerrado...")
    break
  else:
    print ("Digite apenas numeros de 1 a 4")
    menu()
except ValueError:
   print("Digite apenas numeros inteiros!")