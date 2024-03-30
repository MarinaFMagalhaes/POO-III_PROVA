class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecer_por_litro(self, litros):
        valor_a_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            print(f"Valor a pagar: R$ {valor_a_pagar:.2f}.")
        else:
            print("Não há combustível suficiente na bomba.")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"Valor do litro alterado para R$ {novo_valor:.2f}.")

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
        print(f"Tipo de combustível alterado para {novo_combustivel}.")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível alterada para {nova_quantidade} litros.")

bomba = BombaCombustivel("Gasolina", 3.0, 1000)

bomba.abastecer_por_valor(50)
bomba.abastecer_por_valor(100)
bomba.abastecer_por_litro(20)
bomba.abastecer_por_litro(50)
bomba.alterar_valor(3.5) 
bomba.alterar_combustivel("Etanol")
bomba.alterar_quantidade_combustivel(2500)  
