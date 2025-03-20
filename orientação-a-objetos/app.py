import os

# Lista de restaurantes com nome e estado (ativo ou inativo)
lista_de_restaurantes = [{'nome': 'sushi', 'ativo': True}, {'nome': 'peixe', 'ativo': False}]

def exibir_nome_do_programa():
    '''
    Exibe o nome do programa com uma arte no terminal.
    
    Inputs:
    - Nenhum
    
    Outputs:
    - Exibe o nome do programa em um formato estilizado no terminal.
    '''
    print("""  
    ██████╗░██╗███████╗███████╗░█████╗░  ██████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗████████╗  
    ██╔══██╗██║╚════██║╚════██║██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝╚══██╔══╝  
    ██████╔╝██║░░███╔═╝░░███╔═╝███████║  ██████╔╝██║░░░░░███████║██╔██╗██║█████╗░░░░░██║░░░  
    ██╔═══╝░██║██╔══╝░░██╔══╝░░██╔══██║  ██╔═══╝░██║░░░░░██╔══██║██║╚████║██╔══╝░░░░░██║░░░  
    ██║░░░░░██║███████╗███████╗██║░░██║  ██║░░░░░███████╗██║░░██║██║░╚███║███████╗░░░██║░░░  
    ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░  
    """)

def exibir_opcoes():
    '''
    Exibe o menu principal do programa.
    
    Inputs:
    - Nenhum
    
    Outputs:
    - Exibe as opções do menu principal no terminal.
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''
    Exibe uma mensagem de finalização do aplicativo.
    
    Inputs:
    - Nenhum
    
    Outputs:
    - Exibe uma mensagem de "App Finalizado" no terminal.
    '''
    exibir_subtitulos('App Finalizado')

def voltar_ao_menu_principal():
    '''
    Retorna ao menu principal após o usuário pressionar uma tecla.
    
    Inputs:
    - Nenhum
    
    Outputs:
    - Retorna ao menu principal ao pressionar qualquer tecla.
    '''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    '''
    Exibe uma mensagem de alerta quando o usuário escolhe uma opção inválida.
    
    Inputs:
    - Nenhum
    
    Outputs:
    - Exibe uma mensagem "Opção Inválida" e retorna ao menu principal.
    '''
    print('\nOpção Inválida')
    voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    '''
    Exibe um subtítulo no terminal e limpa a tela.
    
    Inputs:
    - texto: A string a ser exibida como subtítulo.
    
    Outputs:
    - Limpa a tela e exibe o texto passado como subtítulo no terminal.
    '''
    os.system('cls')
    print(texto, '\n')

def cadastrar_novo_restaurante():
    '''
    Função responsável por cadastrar um novo restaurante na lista.
    
    Inputs:
    - Nenhum. O nome do restaurante é solicitado ao usuário via input.
    
    Outputs:
    - Exibe uma mensagem de sucesso ao cadastrar um novo restaurante.
    '''
    exibir_subtitulos('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    lista_de_restaurantes.append({'nome': nome_do_restaurante, 'ativo': False})
    print(f'\nO Restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Exibe a lista de restaurantes cadastrados e seu estado (ativo ou inativo).
    
    Inputs:
    - Nenhum
    
    Outputs:
    - Exibe o nome de todos os restaurantes e seu estado (Ativado/Desativado) no terminal.
    '''
    exibir_subtitulos('Restaurantes Cadastrados')
    for restaurante in lista_de_restaurantes:
        nome_restaurante = restaurante['nome']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{nome_restaurante} | ativo = {ativo}')
    voltar_ao_menu_principal()

def alternando_estado_booleano():
    '''
    Altera o estado de um restaurante entre "ativo" e "inativo".
    
    Inputs:
    - Nenhum. O nome do restaurante é solicitado ao usuário via input.
    
    Outputs:
    - Exibe uma mensagem confirmando se o restaurante foi ativado ou desativado com sucesso.
    '''
    exibir_subtitulos(f'Alternando Estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante: ')
    restaurante_encontrado = False
    
    for restaurante in lista_de_restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\n{nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'\nO Restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('\nRestaurante não encontrado! Volte ao menu principal e o cadastre primeiro!')    
    voltar_ao_menu_principal()

def escolher_opcao():
    '''
    Solicita ao usuário a escolha de uma opção no menu e executa a opção selecionada.
    
    Inputs:
    - Nenhum
    
    Outputs:
    - Executa a função associada à opção escolhida ou exibe uma mensagem de erro se a entrada for inválida.
    '''
    while True:
        opcao = input('Escolha uma opção: ')
        if opcao.isdigit():  # Verifica se a entrada é um número
            opcao_escolhida = int(opcao)
            break
        else:
            opcao_invalida()
    
    try:
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternando_estado_booleano()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    '''
    Função principal do aplicativo. Exibe o nome do programa e o menu, e chama a função para escolher a opção.
    
    Inputs:
    - Nenhum
    
    Outputs:
    - Exibe o nome do programa e o menu, e chama a função para escolher a opção.
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
