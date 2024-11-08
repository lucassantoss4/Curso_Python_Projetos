class Evento:
    def __init__(self, capacidade_inicial=3):
        self.capacidade_inicial = capacidade_inicial
        self.lugares_ocupados = 0
        self.lugares_disponiveis = self.capacidade_inicial

    def cancelar(self):
        if self.lugares_ocupados > 0:
            self.lugares_ocupados -= 1
            self.lugares_disponiveis += 1
            return "Reserva cancelada com sucesso!"
        else:
            return "Não existem reservas para cancelar!"

    def reservar(self):
        if self.lugares_disponiveis > 0:
            self.lugares_ocupados += 1
            self.lugares_disponiveis -= 1
            return "Lugar reservado com sucesso!"
        else:
            return "Não existem mais lugares disponíveis para reserva!"

    def exibir_lugares_disponiveis(self):
        return f"Lugares disponíveis: {self.lugares_disponiveis}"


# Criando a instância do evento
evento = Evento()

# Loop de interação com o usuário
while True:
    opcao = int(input("Selecione uma Opção:\n1 - Exibir lugares\n2 - Reservar Lugar\n3 - Cancelar Reserva\n0 - Sair\n"))


    # lugar_diponivel = evento.exibir_lugares_disponiveis()

    if evento.lugares_disponiveis == 0:
        print("Não existem mais lugares disponíveis para reserva. Encerrando o programa.")
        break

    if opcao == 0 :
        break
    elif opcao == 1:
        print(evento.exibir_lugares_disponiveis())
    elif opcao == 2:
        print(evento.reservar())
    elif opcao == 3:
        print(evento.cancelar())
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
