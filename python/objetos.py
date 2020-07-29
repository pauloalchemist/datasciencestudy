lst_num = ["Data", "Science", "Academy", "nota", 10, 10]
print(type(lst_num))

print(lst_num.count(10))

print(type(10))

print(type([]))

print(type({}))

print(type(()))

print(type("p"))

#criação de classe

class Carro(object):
    pass
#instância carro
celta = Carro()
print(type(celta))

#criando classe funcionários
class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def listFunc(self):
        print("O nome do funcionário é "+ self.nome + " com salário de R$ " + str(self.salario))

Func1 = Funcionarios("Paulo", 10000)

Func1.listFunc()

# Usando atributos
print("********** Usando atributos ***********")

print(hasattr(Func1, "nome"))

print(hasattr(Func1, 'salario'))

print(setattr(Func1, 'salario', 5000))

print(hasattr(Func1, 'salario'))

print(getattr(Func1, 'salario'))

print(delattr(Func1, 'salario'))

print(hasattr(Func1, 'salario'))
