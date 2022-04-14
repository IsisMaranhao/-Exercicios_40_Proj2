# Objetivo:
# Poder criar usuários (classe Usuario)
# Poder armazenar uma coleção de usuários (classe BancoDeUsuarios)

# Imprimir tabela de usuarios:
#      Paulo | paulo@email.com
#    Matheus | matheus@email.com
# ...
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def visualiza_loja(self, loja):
        for bicicleta in loja.estoque:
            print(bicicleta[0])



class Loja:

    def __init__(self,):
        self.estoque = [
            ['123', 'azul', False, None], # identificador, cor, está alugada, quem alugou
            ['456', 'vermelha', False, None]
        ]

    def adicionar_bicicleta(self, identificador, cor):
        self.estoque.append([identificador, cor, False, None])

    def alugar_bicicleta(self, cliente, identificador):
        for bicicleta in self.estoque:
            if bicicleta[0] == identificador and bicicleta[2] == False:
                bicicleta[2] = True
                bicicleta[3] = cliente.email

    def devolver_bicicleta(self, cliente):
        quantidade = 0

        for bicicleta in self.estoque:
            if bicicleta[3] == cliente.email:
                bicicleta[2] = False
                bicicleta[3] = None
                quantidade = quantidade + 1
                
        print(quantidade)

        # Lógica de valor a ser pago...
        # ...
        # return valor  
        # ou  
        # print(valor)

loja1 = Loja()

loja1.adicionar_bicicleta('789', 'amarela')

print(loja1.estoque)
print()

cliente1 = Cliente('Paulo', 'paulo@email.com')
cliente2 = Cliente('Matheus', 'matheus@email.com')


loja1.alugar_bicicleta(cliente1, '789')
loja1.alugar_bicicleta(cliente2, '123')

print(loja1.estoque)
print()

valor_a_ser_pago = loja1.devolver_bicicleta(cliente1)

print(loja1.estoque)
print()

cliente1.visualiza_loja(loja1)