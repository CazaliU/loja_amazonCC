# PRODUTOS #
class produtos():  # Cria a classe produtos
    valor = None
    nome = None
    descricao = None


def cria_produtos(catalago):
    headset = produtos()
    headset.valor = float(300.00)
    headset.nome = "Headset Gamer"
    headset.descricao = 'Ótimo para jogos'
    catalago.append(headset)

    echo_dot = produtos()
    echo_dot.valor = float(200.00)
    echo_dot.nome = 'Echo Dot'
    echo_dot.descricao = '4º geração'
    catalago.append(echo_dot)

    linux = produtos()
    linux.valor = float(89.90)
    linux.nome = 'Pacote Linux'
    linux.descricao = 'Produto exclusivo'
    catalago.append(linux)

    teclado_positivo = produtos()
    teclado_positivo.valor = float(50.99)
    teclado_positivo.nome = 'Teclado Positivo'
    teclado_positivo.descricao = 'O melhor do mercado'
    catalago.append(teclado_positivo)

    iphone_onze = produtos()
    iphone_onze.valor = float(99.99)
    iphone_onze.nome = 'Iphone 11'
    iphone_onze.descricao = 'Funciona somente a bateria'
    catalago.append(iphone_onze)

    smart_tv = produtos()
    smart_tv.valor = float(999.99)
    smart_tv.nome = 'Smart TV 55"'
    smart_tv.descricao = 'Entrega Prime'
    catalago.append(smart_tv)

    whey_protein = produtos()
    whey_protein.valor = float(99.99)
    whey_protein.nome = 'Whey Protein'
    whey_protein.descricao = 'Produto mais vendido'
    catalago.append(whey_protein)

    chinelo = produtos()
    chinelo.valor = float(12.67)
    chinelo.nome = 'Chinelo'
    chinelo.descricao = 'Marca Havaianas'
    catalago.append(chinelo)

    bandeira = produtos()
    bandeira.valor = float(30.00)
    bandeira.nome = 'Bandeira do Brasil'
    bandeira.descricao = 'Tamanho G'
    catalago.append(bandeira)

    banana = produtos()
    banana.valor = float(2.99)
    banana.nome = 'Banana'
    banana.descricao = 'Catura'

    maca = produtos()
    maca.valor = float(4.89)
    maca.nome = 'Maça'
    maca.descricao = 'Fuji'
    catalago.append(maca)

    tenis = produtos()
    tenis.valor = float(200.50)
    tenis.nome = 'Tênis'
    tenis.descricao = 'Adidas'
    catalago.append(tenis)

    garrafa = produtos()
    garrafa.valor = float(5.99)
    garrafa.nome = 'Garrafa de água'
    garrafa.descricao = 'Com gás'
    catalago.append(garrafa)

    copo = produtos()
    copo.valor = float(7.99)
    copo.nome = 'Copo de vidro'
    copo.descricao = 'Transparente'
    catalago.append(copo)

    mesa = produtos()
    mesa.valor = float(200.00)
    mesa.nome = 'Mesa'
    mesa.descricao = 'Mesa de madeira'
    catalago.append(mesa)

    xicara = produtos()
    xicara.valor = float(45.99)
    xicara.nome = 'Xícara'
    xicara.descricao = 'Com estampa da Xuxa'
    catalago.append(xicara)

    bone = produtos()
    bone.valor = float(50.59)
    bone.nome = 'Boné'
    bone.descricao = 'Aba reta'
    catalago.append(bone)


def listar_produtos(catalago):
    indice = 0
    print('---------' * 4)
    for produtos in catalago:  # Roda um loop com os produtos e printa na tela
        print(f'{indice}. {produtos.nome} --> R${produtos.valor:.2f}\nObs: {produtos.descricao}\n')
        indice += 1
    print('---------' * 4)


def comprar_produtos(vetusuarios, catalago):
    verifica_senha(vetusuarios)  # verifica a senha do cliente logado

    # adiciona produtos e valores em uma lista para acessa-los mais fácil
    todos_produtos = []
    todos_valores = []
    produtos_disponiveis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for produtos in catalago:
        todos_produtos.append(produtos.nome)
    for valores in catalago:
        todos_valores.append(valores.valor)

    while vetusuarios[i].limite > 0:
        print(f'Limite disponível: {vetusuarios[i].limite:.2f}')

        escolha = int(input('Digite o número do item para acidioná-lo no carrinho.\nDigite 99 para sair do menu de compras.\nDigite 100 para pagar a conta e liberar limite.\n: '))
        if escolha == 99:
            break
        elif escolha == 100:
            print('Acessando carrinho')
            pagar_conta(vetusuarios)
            break

        if vetusuarios[i].limite > todos_valores[escolha]:
            vetusuarios[i].limite = vetusuarios[i].limite - todos_valores[escolha]
            print(f'{todos_produtos[escolha]} add ao carrinho!')
            vetusuarios[i].carrinho_cliente.append(todos_produtos[escolha])
            vetusuarios[i].carteira_cliente.append(todos_valores[escolha])
        else:
            print('Produto indisponível')


def mostrar_carrinho(vetusuarios):
    verifica_senha(vetusuarios)  # puxa a função que verifica a senha
    print('Carrinho:')
    for prod in vetusuarios[i].carrinho_cliente:  # mostra o carrinho do cliente
        print(f'Produto: {prod}')
    print(f'Valor total: R${sum(vetusuarios[i].carteira_cliente):.2f}')


def pagar_conta(vetusuarios):
    verifica_senha(vetusuarios)

    print(f'Valor total da compra: R${sum(vetusuarios[i].carteira_cliente):.2f}')
    op = input('Digite pagar para quitar a conta: ')
    if op == 'pagar':
        vetusuarios[i].carteira_cliente.clear()
        vetusuarios[i].carrinho_cliente.clear()
        vetusuarios[i].limite = 1000
        print(f'Agora o valor do carrinho é: R${sum(vetusuarios[i].carteira_cliente):.2f}')


# CLIENTES #
class cadastro_cliente:  # classe para cadastrar clientes
    email = None
    senha = None
    nome = None
    cpf = None
    limite = float(1000)
    carrinho_cliente = None
    carteira_cliente = None


def verifica_senha(vetusuarios):
    print()
    senha = input('Digite a sua senha de login: ')  # receba a senha de login
    print()
    for indice in range(len(vetusuarios)):  # verifica se a senha existe em vetusuarios
        if senha == vetusuarios[indice].senha:
            print(f'Bem-vindo {vetusuarios[indice].nome}\n')
            global i  # torna global o indice de vetusuarios com essa senha
            i = indice
            break
        else:
            continue


def verifica_cpf(cpf):
    # tira o . e o - do cpf inserido
    filtro_cpf = ".-"
    for i in range(0, len(filtro_cpf)):
        cpf = cpf.replace(filtro_cpf[i], "")

    if len(cpf) != 11:  # verifica se o cpf contem 11 digitos
        return False

    if cpf == cpf[::-1]:  # varifica se o cpf não tem todos os numeros iguais
        return False

    cpf_reverso = cpf[::-1]  # lê de trás pra frente
    for i in range(2, 0, -1):  # iteração que inicia em 2 e termina em 1
        cpf_enumerado = enumerate(cpf_reverso[i:],
                                  start=2)  # recebe um iterável e enumera cada posição dele, inica em 2
        dv_calculado = sum(map(lambda x: int(x[1]) * x[0],
                               cpf_enumerado)) * 10 % 11  # lambda = função anonina(não precisa ser declarada), map aplica uma operação sobre sobre cada item da lista
        if cpf_reverso[i - 1:i] != str(dv_calculado % 10):
            return False
    return True  # retorna True se estivet tudo certo


def cadastro(vetusuarios):
    cliente = cadastro_cliente()
    cliente.limite_credito = float(1000)
    cliente.carrinho_cliente = []
    cliente.carteira_cliente = []

    while True:
        cliente.nome = input('Informe o seu nome: ')
        if len(cliente.nome) > 2:
            break
        else:
            print('Digite um nome com mais de 2 caracteres!')

    while True:
        cliente.email = input('Informe o seu email: ')
        if '@' in cliente.email:
            break
        else:
            print('Digite um email válido, ex: nome@gmail.com')

    while True:
        cliente.senha = input('Digite uma senha de acesso: ')
        if len(cliente.senha) >= 6:
            break
        else:
            print('Digite uma senha com no mínimo seis dígitos!')

    cliente.cpf = input('Informe o seu cpf: ')
    if verifica_cpf(cliente.cpf) == True:
        for vetusario in vetusuarios:
            if cliente.cpf == vetusario.cpf:
                print("Esse usuário já está cadastrado!!")
                return
    else:
        print('CPF inválido!')
        return

    vetusuarios.append(cliente)
    print('Cadastro realizado com sucesso!')


def consulta_cliente(cpf, vetusuarios):
    for usuario in vetusuarios:
        if cpf == usuario.cpf:
            print(f"O nome do cliente é: {usuario.nome}")
            print(f"O email do cliente é: {usuario.email}")


# MENU #
def menu():
    vetusuarios = []  # para cadastrar novos usuarios
    catalago = []  # para criar catálago
    cria_produtos(catalago)
    while True:
        print()

        opcao = input(
            "Seja bem-vindo ao menu da Amazon, escolha uma opção para continuar:\n\n1- Cadastro\n2- Consultar cliente\n3- Mostrar catálago\n4- Comprar\n5- Mostrar carrinho\n6- Pagar conta \n0- Sair do programa\n\n:")
        if opcao == "1":
            print("Opção selecionada: Cadastro")
            cadastro(vetusuarios)
        elif opcao == "2":
            print("Opção selecionada: Consultar cliente")
            if len(vetusuarios) != 0:
                parametro_consulta = input("Insira o CPF\n:")
                consulta_cliente(parametro_consulta, vetusuarios)
            else:
                print('Cadastre um usuário primeiro!')
        elif opcao == "3":
            print("Opção selecionada: Mostrar catálago")
            listar_produtos(catalago)
        elif opcao == "4":
            print("Opção selecionada: Comprar produtos")
            if len(vetusuarios) != 0:
                comprar_produtos(vetusuarios, catalago)
            else:
                print('Cadastre um usuário primeiro!')
        elif opcao == "5":
            print("Opção selecionada: Mostrar carrinho")
            if len(vetusuarios) != 0:
                mostrar_carrinho(vetusuarios)
            else:
                print('Cadastre um usuário primeiro!')
        elif opcao == "6":
            print("Opção selecionada: Pagar conta")
            if len(vetusuarios) != 0:
                pagar_conta(vetusuarios)
            else:
                print('Cadastre um usuário primeiro')
        elif opcao == "0":
            print("Opção selecionada: Sair")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()
