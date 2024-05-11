class Banco:
    def __init__(self):
        self.saldo_inicial = 1000
        self.saldo = self.saldo_inicial
        self.depositos = []
        self.saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.depositos.append(valor)
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques < 3 and valor <= 500 and self.saldo >= valor:
            self.saques += 1
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        elif valor > 500:
            print("Erro: Limite máximo de saque diário é de R$500.")
        elif self.saques >= 3:
            print("Erro: Limite máximo de 3 saques diários atingido.")
        else:
            print("Desculpe, saldo insuficiente.")

    def extrato(self):
        print("### Extrato ###")
        print("Depósitos:")
        for deposito in self.depositos:
            print(f" - R${deposito}")
        total_depositos = sum(self.depositos)
        print(f"Total de depósitos: R${total_depositos}")
        print(f"Saldo atual: R${self.saldo}")


# Função para solicitar ação ao usuário
def menu():
    print("Escolha uma opção:")
    print("1. Consultar saldo")
    print("2. Tirar Extrato")
    print("3. Realizar saque")
    print("4. Realizar depósito")

    opcao = input("Digite o número correspondente à opção desejada: ")

    return opcao


# Teste do sistema
banco = Banco()

while True:
    escolha = menu()

    if escolha == '1':
        print(f"Seu saldo atual é: R${banco.saldo}")
    elif escolha == '2':
        banco.extrato()
    elif escolha == '3':
        valor_saque = float(input("Digite o valor que deseja sacar: R$"))
        banco.sacar(valor_saque)
    elif escolha == '4':
        valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
        banco.depositar(valor_deposito)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")