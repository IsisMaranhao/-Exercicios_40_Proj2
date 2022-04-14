'''
Sistema de Empréstimo de Bicicletas

Vocês farão um sistema de empréstimo de bibliotecas, que envolverá duas classes principais (Cliente, Loja). O projeto deve ser entregue 
até 21/02/2022.

Cliente pode:

• Ver as bicicletas disponíveis na Loja;
• Alugar bicicletas por hora (R$5/hora);
• Alugar bicicletas por dia (R$25/dia);
• Alugar bicicletas por semana (R$100/semana)
• Aluguel para família, uma promoção que 3 ou mais empréstimos (de qualquer tipo) com 30% de desconto no valor total.

Loja pode:

• Calcular a conta quando o cliente decidir devolver a bicicleta;
• Mostrar o estoque de bicicletas;
• Receber pedidos de aluguéis por hora, diários ou semanais validando a 
possibilidade com o estoque e modo de aluguel existente.

Por questão de simplicidade vamos assumir que:

• Cada empréstimo segue apenas um modelo de cobrança (hora, dia ou semana);
• O cliente pode decidir livremente quantas bicicletas quer alugar;
• Os pedidos de aluguéis só podem ser efetuados se houver bicicletas 
suficientes disponíveis.
• Não se preocupem quanto a dinheiro em caixa das Lojas nem dos Clientes.
Ao projetar seus objetos você deve se atentar ao que cada classe será
responsável por fazer, entenda o que cada elemento pode fazer, e em seguida 
abstraia o problema para desenhar as classes e seus métodos. 
Note que nem tudo que um objeto pode fazer é necessariamente um método 
desse objeto.

Utilize a biblioteca datetime para trabalhar com tempo no seu programa.

Você provavelmente vai querer testar o funcionamento e relação dessas classes, 
para isso use um terceiro arquivo que usa pelo menos três instâncias de Cliente 
e duas de Loja e testa a integração e funcionamento das duas classes. 
Para facilitar o fluxo das chamadas use prints em cada método que funcionem 
como logs, um bom log consiste em informar de onde ele vem (classe que printou 
o log), o que ele está fazendo (qual método), com quais informações 
(os parâmetros recebidos) e o momento que ocorreu.
Faça validações, e gere erros caso alguma validação falhe (raise), note que é 
comum logarmos (neste caso, com o print) quando algum erro ocorreu em nosso 
sistema.

Bons estudos a todos!
'''

class Cliente:
    def __init__(self, nome, email, telefone, tipo_aluguel):
        self.nome = nome
        self.email = email
        self.tipo_aluguel = tipo_aluguel # "hora", "dia", "semana"
        self.telefone = telefone # 00999999999
        self.contador = 0

    def disponivel_alugar(self, loja):
        for bicicleta in loja.estoque:
            if bicicleta[1] == False:
                print(bicicleta[0], 'disponível')
            else:
                print(bicicleta[0], 'X')

class Loja:
    def __init__(self, bicicletas):

        self.estoque = bicicletas

    def adicionar_bicicleta_estoque(self, id):
        self.estoque.append([id, False, None])

    def alugar_bicicleta(self, cliente, id):
        for bicicleta in self.estoque:
            if bicicleta[0] == id and bicicleta[1] == False:
                bicicleta[1] = True
                bicicleta[2] = cliente.email

    def devolver_bicicleta(self, cliente):
        quantidade = 0
        
        for bicicleta in self.estoque:
            if bicicleta[2] == cliente.email:
                bicicleta[1] = False
                bicicleta[2] = None
                quantidade += 1

        cliente.contador = quantidade

    def ver_estoque(self):
        print('************ ESTOQUE ************')
        for x in range(len(loja.estoque)):
            if loja.estoque[x][1] == False:
                print(f' BICICLETA: {loja.estoque[x][0]}')
            elif loja.estoque[x][1] == True:
                print(f' BICICLETA: {loja.estoque[x][0]} está alugada para {loja.estoque[x][2]}')
        print('*********************************')

    def calcular_conta(self, cliente):
        parametro = cliente.tipo_aluguel
        valor = cliente.contador

        if (parametro == 'hora'): # Alugar bicicletas por hora (R$5/hora); Aluguel para família, uma promoção que 3 ou mais empréstimos com 30% de desconto no valor total.
            if valor < 3:
                pagamento = valor * 5
                print(f' NOME:{cliente.nome} \n TOTAL DE BICICLETAS: {valor} \n PLANO: Por {parametro} ')
                print('---------------------------------')
                print(f' VALOR A PAGAR: R$ {pagamento} \n')
            else:
                pagamento = (valor * 5) - (0.3 * valor * 5)
                print(f' NOME:{cliente.nome} \n TOTAL DE BICICLETAS: {valor} \n PLANO: Por {parametro} ')
                print('---------------------------------')
                print(f' VALOR A PAGAR: R$ {pagamento} \n')

        if (parametro == 'dia'): # Alugar bicicletas por dia (R$25/dia); Aluguel para família, uma promoção que 3 ou mais empréstimos com 30% de desconto no valor total.
            
            if valor < 3:
                pagamento = valor * 25
                print(f' NOME:{cliente.nome} \n TOTAL DE BICICLETAS: {valor} \n PLANO: Por {parametro} ')
                print('---------------------------------')
                print(f' VALOR A PAGAR: R$ {pagamento} \n')

            else:
                pagamento = (valor * 25) - (0.3 * valor * 25)
                print(f' NOME:{cliente.nome} \n TOTAL DE BICICLETAS: {valor} \n PLANO: Por {parametro} ')
                print('---------------------------------')
                print(f' VALOR A PAGAR: R$ {pagamento} \n')

        if (parametro == 'semana'): # Alugar bicicletas por semana (R$100/semana) Aluguel para família, uma promoção que 3 ou mais empréstimos com 30% de desconto no valor total.

            if valor < 3: 
                pagamento = valor * 100
                print(f' NOME:{cliente.nome} \n TOTAL DE BICICLETAS: {valor} \n PLANO: Por {parametro} ')
                print('---------------------------------')
                print(f' VALOR A PAGAR: R$ {pagamento} \n')
            else:
                pagamento = (valor * 100) - (0.3 * valor * 100)
                print(f' NOME:{cliente.nome} \n TOTAL DE BICICLETAS: {valor} \n PLANO: Por {parametro} ')
                print('---------------------------------')
                print(f' VALOR A PAGAR: R$ {pagamento} \n')




# CRIANDO ESTOQUE DA LOJA DE BICICLETAS:
estoque_loja = [
        ['bike_01', False, None], # identificador, está alugada ou não, quem alugou
        ['bike_02', False, None],
        ['bike_03', False, None],
        ['bike_04', False, None], 
        ['bike_05', False, None],
        ['bike_06', False, None],
        ['bike_07', False, None],
        ['bike_08', False, None], 
        ['bike_09', False, None],
        ['bike_10', False, None],
        ['bike_11', False, None],
        ['bike_12', False, None], 
        ['bike_13', False, None],
        ['bike_14', False, None],
        ['bike_15', False, None],
        ['bike_16', False, None], 
        ['bike_17', False, None],
        ['bike_18', False, None],
        ['bike_19', False, None],
        ['bike_20', False, None]
        ]

loja = Loja(estoque_loja)

# ADICIONANDO A BIKE 21 AO SISTEMA:
loja.adicionar_bicicleta_estoque('bike_21')

# VERIFICANDO A INCLUSÃO DA BICICLETA 21 AO ESTOQUE:
loja.ver_estoque()

#CADASTRANDO CLIENTES:
#Cadastrando primeiro cliente - Classe Cliente
cliente01 = Cliente('Isis', 'isis@email.com', 21999999999 ,'hora')

#Cadastrando segundo cliente - Classe Cliente
cliente02 = Cliente('Junior', 'junior@email.com', 11999999999 ,'hora')

#Cadastrando terceiro cliente - Classe Cliente
cliente03 = Cliente('Isabella', 'isabella@email.com', 41999999999 ,'dia')

#Cadastro quarto cliete - Classe Cliente
cliente04 = Cliente('Davi', 'davi@gmail.com', 20999999999 ,'dia')

#Cadastro quarto cliete - Classe Cliente
cliente05 = Cliente('Mayara', 'Mayara@gmail.com', 19999999999 ,'semana')

#Cadastro quarto cliete - Classe Cliente
cliente06 = Cliente('Renan', 'Renan@gmail.com', 29999999999 ,'semana')

# VERIFICANDO O ESTOQUE:
loja.ver_estoque()

#ACESSANDO O ESTOQUE COMO CLIENTE E ALUGANDO BICICLETAS:
print('ESOQUE DA LOJA VISTO PELO CLIENTE 01:')
cliente01.disponivel_alugar(loja)
print()

loja.alugar_bicicleta(cliente01, 'bike_01')
loja.alugar_bicicleta(cliente01, 'bike_02')

print('ESOQUE DA LOJA VISTO PELO CLIENTE 02:')
cliente02.disponivel_alugar(loja)
print()

loja.alugar_bicicleta(cliente02, 'bike_03')
loja.alugar_bicicleta(cliente02, 'bike_04')
loja.alugar_bicicleta(cliente02, 'bike_05')

print('ESOQUE DA LOJA VISTO PELO CLIENTE 03:')
cliente03.disponivel_alugar(loja)
print()

loja.alugar_bicicleta(cliente03, 'bike_10')

print('ESOQUE DA LOJA VISTO PELO CLIENTE 04:')
cliente04.disponivel_alugar(loja)
print()

loja.alugar_bicicleta(cliente04, 'bike_11')
loja.alugar_bicicleta(cliente04, 'bike_12')
loja.alugar_bicicleta(cliente04, 'bike_13')

print('ESOQUE DA LOJA VISTO PELO CLIENTE 05:')
cliente05.disponivel_alugar(loja)
print()

loja.alugar_bicicleta(cliente05, 'bike_16')
loja.alugar_bicicleta(cliente05, 'bike_17')

print('ESOQUE DA LOJA VISTO PELO CLIENTE 06:')
cliente06.disponivel_alugar(loja)
print()

loja.alugar_bicicleta(cliente06, 'bike_19')
loja.alugar_bicicleta(cliente06, 'bike_20')
loja.alugar_bicicleta(cliente06, 'bike_21')

# VISUALIZANDO O ESTOQUE DEPOIS DE ALUGAR:
print('ESOQUE DA LOJA VISTO PELO SISTEMA:')
print(loja.estoque)
print()

# OU 
print('ESOQUE DA LOJA VISTO PELO SISTEMA:')
for x in range(len(loja.estoque)):
    print(loja.estoque[x])
print()

# DEVOLUÇÕES DAS BICILETAS:
loja.devolver_bicicleta(cliente01)
loja.devolver_bicicleta(cliente02)
loja.devolver_bicicleta(cliente03)
loja.devolver_bicicleta(cliente04)
loja.devolver_bicicleta(cliente05)
loja.devolver_bicicleta(cliente06)

# VISUALIZANDO O ESTOQUE DEPOIS DAS DEVOLUÇÕES:
print('ESOQUE DA LOJA VISTO PELO SISTEMA:')
for x in range(len(loja.estoque)):
    print(loja.estoque[x])
print()

# CALCULANDO O VALOR DE CADA ALUGUEL
loja.calcular_conta(cliente01)
loja.calcular_conta(cliente02)
loja.calcular_conta(cliente03)
loja.calcular_conta(cliente04)
loja.calcular_conta(cliente05)
loja.calcular_conta(cliente06)

print()