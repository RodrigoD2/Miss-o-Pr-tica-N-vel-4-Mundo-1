class Calculadora:
    def __init__(self, valorA=0, valorB=0, operacao=''):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self):
        operacoes_validas = ['+', '-', '*', '/']
        return self.__operacao in operacoes_validas
    
    def calcular(self):
        if not self.validarOperacao():
            print(f"Operação inválida: {self.__operacao}. As operações válidas são +, - , *, /. ")
            exit()

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Não é possível dividir o valor por 0.")
                exit()
            return self.__valorA / self.__valorB

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"{self.__valorA} {self.__operacao} {self.__valorB} = {resultado}")
    def entradaDados(self):
        self.__valorA = float(input("Digite o valor A: "))
        self.__operacao = input("Digite a operação matemática: ")
        self.__valorB = float(input("Digite o valor B: "))
        if not self.validarOperacao():
            print(f"Operação inválida: {self.__operacao}. As operações válidas são +, -, *, e /.")
            exit()