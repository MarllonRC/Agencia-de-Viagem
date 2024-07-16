class viagem_class:
    def __init__(self, destino):
        self.destino = destino

viagem_0 = viagem_class("Florida")
viagem_1 = viagem_class("Havai")
viagem_2 = viagem_class("Tóquio")
viagem_3 = viagem_class("Egito")
viagem_4 = viagem_class("Londres")

print("Bem vindo! Viagems Space tem algumas ofertas para você!")
viajante = input("Digite seu nome para começarmos: ")
print(f"{viajante}, temos 5 destinos que combinam com você:\n"
      "[0] Florida\n"
      "[1] Havai\n"
      "[2] Tóquio\n"
      "[3] Egito\n"
      "[4] Londres")

seleção = int(input("Selecione a viagem desejada: ")) # solicitação ao usuário
lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3, viagem_4] # lista dos índices dos objetos para escolha

if seleção >= 5 or seleção < 0:
    print("Opção inválida.")
else:
    print(f"{viajante}, sua viagem para {lista_viagem[seleção].destino} está marcada.") # resultado
    print("Volte sempre")
