class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    @property
    def altera_cargo(self):
        novo_cargo = input('Novo cargo: ')
        self.cargo = novo_cargo
        print('Cargo atualizado para {}'.format(self.cargo))
    @property
    def altera_salario(self):
        novo_salario = float(input('Novo salário: '))
        self.salario = novo_salario
        print('Salário atualizado para R$ {}'.format(self.salario))


def registra():
    return Funcionario(
        nome = input('Nome: '),
        cargo = input('Cargo: '),
        salario = float(input('Salário: '))
    )


def menu():
    opcao = int(input('1. Novo\n2. Editar cargo\n3. Editar salário\n--> '))

    if opcao == 1:
        registra()
        print('\n')
        menu()
    if opcao == 2:
        altera_cargo() # como acessar o objeto ?
        print('\n')
        menu()
    if opcao == 3:
        altera_salario() # como acessar o objeto ?
        print('\n')
        menu()
    else:
        exit()

if __name__ == "__main__":
    menu()

