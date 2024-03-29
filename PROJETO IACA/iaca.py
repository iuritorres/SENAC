###################################################################################################################
#              [ DEVS ]               #          [ PROJETO IACA ]           #          [ POPSOFTWARES ]           #
#                                     #                                     #                                     #
#           [ IURI TORRES ]           #    [ Instituição Filantrópica ]     #   [ Nossa paixão,  seu negócio ]    #
###################################################################################################################

### IMPORTAÇÕES ###

from dataclasses import replace
import os
import mysql.connector
from time import sleep

### CONEXÃO DATABASE ###

con = mysql.connector.connect(
    host='mysql-78965-0.cloudclusters.net',
    port=19072,
    database='BD_IACA',
    user='user_system',
    password='useradmin'
)

if con.is_connected():

    os.system('cls')

    db_info = con.get_server_info()
    print('Conectado ao Servdor SQL versão ',db_info)
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados ', linha)

    sleep(1)


### CODIGO ###

# Lista para definição de tipo de conta

lista_tipo_conta = []

# Timer 3 segundos

def timer3s():
        lista_timer3s = [3, 2, 1]
        for segundo in lista_timer3s:
            
            os.system('cls')

            print('\n','='*68,'\n')
            print(' Acesso ao sistema em')
            print(f' {segundo} segundos...')
            print('\n','='*68,'\n')
            sleep(1)

# Sistema De Login

def sistema_login():
    print('\n','='*28,'[ LOGIN ]','='*28,'\n')
    print(' 0 - Login')
    print(' 1 - Registrar')
    print('\n','='*68,'\n')

    id_login = int(input(' Digite um número que corresponda a função que deseja executar: '))

    while True:
        
        if id_login == 0: # LOGIN

            print('\n','='*28,'[ LOGIN ]','='*28,'\n')
            user_login = str(input(' Digite o seu e-mail ou CPF: '))
            password_login = str(input(' Digite sua senha: '))
            print('\n','='*68,'\n')

            verificacao = "SELECT EMAIL FROM FUNCIONARIOS WHERE EMAIL ='{}'".format(user_login)
            cursor.execute(verificacao)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                verificacao_campo_funcionarios = 'conta_doador'

            if len(resultado) != 0:
                verificacao_campo_funcionarios = 'EMAIL'

            verificacao = "SELECT CPF FROM FUNCIONARIOS WHERE CPF ='{}'".format(user_login)
            cursor.execute(verificacao)
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                verificacao_campo_funcionarios = 'CPF'

            if verificacao_campo_funcionarios != 'conta_doador':

                verificacao = "SELECT SENHA FROM FUNCIONARIOS WHERE {} ='{}'".format(verificacao_campo_funcionarios, user_login)
                cursor.execute(verificacao)
                resultado_funcionarios = cursor.fetchall()

                if password_login in resultado_funcionarios[0]:

                    break

                else:
                    print(' Você digitou um usuário ou senha inválido, tente novamente.')

            elif verificacao_campo_funcionarios == 'conta_doador':

                verificacao = "SELECT EMAIL FROM DOADORES WHERE EMAIL ='{}'".format(user_login)
                cursor.execute(verificacao)
                resultado = cursor.fetchall()

                if len(resultado) != 0:
                    verificacao_campo_doador = 'EMAIL'

                verificacao = "SELECT CPF FROM DOADORES WHERE CPF ='{}'".format(user_login)
                cursor.execute(verificacao)
                resultado = cursor.fetchall()

                if len(resultado) != 0:
                    verificacao_campo_doador = 'CPF'

                verificacao = "SELECT SENHA FROM DOADORES WHERE {} = '{}'".format(verificacao_campo_doador, user_login)
                cursor.execute(verificacao)
                resultado_doadores = cursor.fetchall()

                if password_login in resultado_doadores[0]:

                    break

                else:
                    print(' Você digitou um usuário ou senha inválido, tente novamente.')

        elif id_login == 1: # REGISTRO

            # Declara o tipo de conta

            os.system('cls')

            tabela_login = str(input(' Qual o tipo de conta que você deseja registrar (FUNCIONARIO/DOADOR): ')).upper()

            if tabela_login == 'FUNCIONARIO':
                tabela_consulta = 'FUNCIONARIOS'
            elif tabela_login == 'DOADOR':
                tabela_consulta = 'DOADORES'

                # Se for tipo doador
            
                if tabela_consulta == 'DOADORES':

                    nome_consulta = str(input(' Digite o nome completo para o novo cadastro: ')).upper()
                    CPF_consulta = int(input(' Digite o CPF (somente números): '))
                    email_consulta = str(input(' Digite o e-mail: '))
                    num_telefone_consulta = int(input(' Digite o número de telefone (DDD + número sem o 9): '))
                    dataNasc_consulta = str(input(' Digite a data de nascimento no formato AAAA-MM-DD (inclua os "-"): '))
                    sexo_consulta = str(input(' Digite o sexo (M/F): '))
                    nomePai_consulta = str(input(' Digite o nome completo do Pai: ')).upper()
                    nomeMae_consulta = str(input(' Digite o nome completo da Mae: ')).upper()
                    senha_consulta = str(input('Digite sua senha: '))

                    def funcao_insertinto():
                        comando = f"""INSERT INTO DOADORES (NOME, CPF, EMAIL, NUMERO, DATA_NASC, SEXO, NOME_PAI, NOME_MAE, SENHA)

                    VALUES
                            ('{nome_consulta}', {CPF_consulta}, '{email_consulta}', {num_telefone_consulta}, '{dataNasc_consulta}', '{sexo_consulta}', '{nomePai_consulta}', '{nomeMae_consulta}', '{senha_consulta}');"""

                        cursor.execute(comando)
                        con.commit()

                    funcao_insertinto()
                    print(' O Registro foi efetivado com sucesso!')

                    break

                # Se for tipo funcionário

                elif tabela_consulta == 'FUNCIONARIOS':

                    nome_consulta = str(input(' Digite o nome completo para o novo cadastro: ')).upper()
                    CPF_consulta = int(input(' Digite o CPF (somente números): '))
                    email_consulta = str(input(' Digite o e-mail: '))
                    num_telefone_consulta = int(input(' Digite o número de telefone (DDD + número sem o 9): '))
                    num_camisa_consulta = str(input(' Digite o tamanho da sua camisa (P/M/PP/MM etc.): '))
                    dataNasc_consulta = str(input(' Digite a data de nascimento no formato AAAA-MM-DD (inclua os "-"): '))
                    sexo_consulta = str(input(' Digite o sexo (M/F): '))
                    nomePai_consulta = str(input(' Digite o nome completo do Pai: ')).upper()
                    nomeMae_consulta = str(input(' Digite o nome completo da Mae: ')).upper()
                    senha_consulta = str(input('Digite sua senha: '))

                    def funcao_insertinto():
                        comando = f"""INSERT INTO FUNCIONARIOS (NOME, CPF, EMAIL, NUMERO, N_CAMISA, DATA_NASC, SEXO, NOME_PAI, NOME_MAE, SENHA)

                    VALUES
                            ('{nome_consulta}', {CPF_consulta}, '{email_consulta}', {num_telefone_consulta}, '{num_camisa_consulta}', '{dataNasc_consulta}', '{sexo_consulta}', '{nomePai_consulta}', '{nomeMae_consulta}', '{senha_consulta}');"""

                        cursor.execute(comando)
                        con.commit()

                    funcao_insertinto()
                    print(' O Registro foi efetivado com sucesso!')

                    break

        else:
            print(' Você não digitou um número válido, tente novamente!')

    if verificacao_campo_funcionarios == 'EMAIL':
        lista_tipo_conta.append('conta_funcionario')
    elif verificacao_campo_funcionarios == 'CPF':
        lista_tipo_conta.append('conta_funcionario')
    elif verificacao_campo_funcionarios == 'conta_doador':
        lista_tipo_conta.append('conta_doador')


# Menu de Funções do Sistema

def funcoes_sistema():
    print('\n','='*27,'[ CONSULTA ]','='*27,'\n')
    print(' 0 - Finalizar Consultas')
    print(' 1 - Checar registros de uma tabela.')
    print(' 2 - Inserir um registro em uma tabela.')
    print(' 3 - Atualizar uma informação de uma tabela.')
    print(' 4 - Deletar um registro de uma tabela.')
    print('\n','='*68,'\n')

# ACESSO

sistema_login()

# INÍCIO DA CONSULTA

timer3s()
os.system('cls')

while True:

    funcoes_sistema()
    id_exec_funcao_sistema = int(input(' Digite um número que corresponda a função que deseja executar: '))
    print('\n','='*68,'\n')


    # FUNÇÃO SELECT

    if id_exec_funcao_sistema == 1:
        print(' TABELAS: DOACOES, DOADORES, FUNCIONARIOS')
        tabela_consulta = str(input(' Digite o nome da tabela que deseja consultar: ')).upper()

        def funcao_select():
            comando = f'SELECT * FROM {tabela_consulta}'
            cursor.execute(comando)
            resultado = cursor.fetchall()

            if tabela_consulta == 'DOACOES':

                for registro in resultado:
                    posicao_registro = resultado.index(registro)
                    conteudo_registro = resultado[posicao_registro]

                    comando = f'SELECT NOME FROM DOADORES WHERE ID = {conteudo_registro[0]}'
                    cursor.execute(comando)
                    resultado_nome_doador = cursor.fetchall()

                    nome_doador = resultado_nome_doador

                    print(f'\n', ('='*27), f'[{posicao_registro + 1}° registro]', ('='*27))
                    print(f' ID do Doador: {conteudo_registro[0]}')
                    print(f' Nome do Doador: {nome_doador}' .replace("[('", "") .replace("',)]", ''))
                    print(f' Data da Doação: {conteudo_registro[1]}')
                    print(f' Tipo de Doação: {conteudo_registro[2]}')
                    print(f' Meio de Pagamento: {conteudo_registro[3]}')


            elif tabela_consulta == 'DOADORES':

                for registro in resultado:
                    posicao_registro = resultado.index(registro)
                    conteudo_registro = resultado[posicao_registro]

                    if conteudo_registro[6] == 'M':
                        sexo = 'Masculino'

                    elif conteudo_registro[6] == 'F':
                        sexo = 'Feminino'

                    print(f'\n', ('='*27), f'[{posicao_registro + 1}° registro]', ('='*27))
                    print(f' ID: {conteudo_registro[0]}')
                    print(f' Nome Completo: {conteudo_registro[1]}')
                    print(f' CPF: {conteudo_registro[2]}')
                    print(f' E-mail: {conteudo_registro[3]}')
                    print(f' Telefone: {conteudo_registro[4]}')
                    print(f' Data de Nascimento: {conteudo_registro[5]}')
                    print(f' Sexo: {sexo}')
                    print(f' Nome do Pai: {conteudo_registro[7]}')
                    print(f' Nome da Mãe: {conteudo_registro[8]}')

            elif tabela_consulta == 'FUNCIONARIOS':

                for registro in resultado:
                    posicao_registro = resultado.index(registro)
                    conteudo_registro = resultado[posicao_registro]

                    if conteudo_registro[7] == 'M':
                        sexo = 'Masculino'

                    elif conteudo_registro[7] == 'F':
                        sexo = 'Feminino'

                    print(f'\n', ('='*27), f'[{posicao_registro + 1}° registro]', ('='*27))
                    print(f' ID: {conteudo_registro[0]}')
                    print(f' Nome Completo: {conteudo_registro[1]}')
                    print(f' CPF: {conteudo_registro[2]}')
                    print(f' E-mail: {conteudo_registro[3]}')
                    print(f' Telefone: {conteudo_registro[4]}')
                    print(f' Tamanho da camisa: {conteudo_registro[5]}')
                    print(f' Data de Nascimento: {conteudo_registro[6]}')
                    print(f' Sexo: {sexo}')
                    print(f' Nome do Pai: {conteudo_registro[8]}')
                    print(f' Nome da Mãe: {conteudo_registro[9]}')

        funcao_select()

    # FUNÇÃO INSERT INTO

    elif id_exec_funcao_sistema == 2:

        if 'conta_doador' == lista_tipo_conta[0]:
            print(' Você não tem acesso a essa funcionalidade, por favor digite outro número.')

        else:

            print(' TABELAS: DOACOES, DOADORES, FUNCIONARIOS')
            tabela_consulta = str(input(' Digite o nome da tabela que deseja inserir um registro: ')).upper()

            if tabela_consulta == 'DOACOES':

                print('\n [REGISTRO]:')

                id_doador_consulta = int(input(' Digite o ID do doador: '))

                print(f'\n [REGISTRO]: \n ID: {id_doador_consulta}')

                data_doacao_consulta = str(input(' Digite a data atual no formato AAAA-MM-DD (inclua os "-"): '))

                print(f'\n [REGISTRO]: \n ID: {id_doador_consulta} \n DATA DA DOAÇÃO: {data_doacao_consulta}')

                tipo_consulta = str(input(' Digite o tipo de doação (ROUPA/ALIMENTO/DINHEIRO/HIGIENE): ')).upper()

                print(f'\n [REGISTRO]: \n ID: {id_doador_consulta} \n DATA DA DOAÇÃO: {data_doacao_consulta} \n TIPO DE DOAÇÃO: {tipo_consulta}')

                forma_pagamento_consulta = str(input(' Digite a forma de pagamento (DÉBITO/CRÉDITO/BOLETO/PIX/TRANSFERÊNCIA/DOAÇÃO): ')).upper()

                print(f'\n [REGISTRO]: \n ID: {id_doador_consulta} \n DATA DA DOAÇÃO: {data_doacao_consulta} \n TIPO DE DOAÇÃO: {tipo_consulta} \n FORMA DE PAGAMENTO: {forma_pagamento_consulta}')

                def funcao_insertinto():
                    comando = f"""INSERT INTO DOACOES (ID_DOADOR, DATA_DOACAO, TIPO, FORMA_PAGAMENTO)

                VALUES
                        ({id_doador_consulta}, '{data_doacao_consulta}', '{tipo_consulta}', '{forma_pagamento_consulta}');"""

                    cursor.execute(comando)
                    con.commit()

                confirmacao = str(input(' Você realmente deseja inserir esse registro? (SIM/NAO): ')).upper()

                if confirmacao == 'SIM':

                    funcao_insertinto()

                elif confirmacao == 'NAO':

                    print(' A solicitação foi cancelada!')


            elif tabela_consulta == 'DOADORES':

                nome_consulta = str(input(' Digite o nome completo para o novo cadastro: ')).upper()
                CPF_consulta = int(input(' Digite o CPF (somente números): '))
                email_consulta = str(input(' Digite o e-mail: '))
                num_telefone_consulta = int(input(' Digite o número de telefone (DDD + número sem o 9): '))
                dataNasc_consulta = str(input(' Digite a data de nascimento no formato AAAA-MM-DD (inclua os "-"): '))
                sexo_consulta = str(input(' Digite o sexo (M/F): '))
                nomePai_consulta = str(input(' Digite o nome completo do Pai: ')).upper()
                nomeMae_consulta = str(input(' Digite o nome completo da Mae: ')).upper()
                senha_consulta = str(input('Digite sua senha: '))

                def funcao_insertinto():
                    comando = f"""INSERT INTO DOADORES (NOME, CPF, EMAIL, NUMERO, DATA_NASC, SEXO, NOME_PAI, NOME_MAE, SENHA)

                VALUES
                        ('{nome_consulta}', {CPF_consulta}, '{email_consulta}', {num_telefone_consulta}, '{dataNasc_consulta}', '{sexo_consulta}', '{nomePai_consulta}', '{nomeMae_consulta}', '{senha_consulta}');"""

                    cursor.execute(comando)
                    con.commit()

                funcao_insertinto()

            elif tabela_consulta == 'FUNCIONARIOS':

                nome_consulta = str(input(' Digite o nome completo para o novo cadastro: ')).upper()
                CPF_consulta = int(input(' Digite o CPF (somente números): '))
                email_consulta = str(input(' Digite o e-mail: '))
                num_telefone_consulta = int(input(' Digite o número de telefone (DDD + número sem o 9): '))
                num_camisa_consulta = str(input(' Digite o tamanho da sua camisa (P/M/PP/MM etc.): '))
                dataNasc_consulta = str(input(' Digite a data de nascimento no formato AAAA-MM-DD (inclua os "-"): '))
                sexo_consulta = str(input(' Digite o sexo (M/F): '))
                nomePai_consulta = str(input(' Digite o nome completo do Pai: ')).upper()
                nomeMae_consulta = str(input(' Digite o nome completo da Mae: ')).upper()
                senha_consulta = str(input('Digite sua senha: '))

                def funcao_insertinto():
                    comando = f"""INSERT INTO FUNCIONARIOS (NOME, CPF, EMAIL, NUMERO, N_CAMISA, DATA_NASC, SEXO, NOME_PAI, NOME_MAE, SENHA)

                VALUES
                        ('{nome_consulta}', {CPF_consulta}, '{email_consulta}', {num_telefone_consulta}, '{num_camisa_consulta}', '{dataNasc_consulta}', '{sexo_consulta}', '{nomePai_consulta}', '{nomeMae_consulta}', '{senha_consulta}');"""

                    cursor.execute(comando)
                    con.commit()

                funcao_insertinto()

    # FUNÇÃO UPDATE

    elif id_exec_funcao_sistema == 3:

        if 'conta_doador' == lista_tipo_conta[0]:
            print(' Você não tem acesso a essa funcionalidade, por favor digite outro número.')

        else:

            print(' TABELAS: DOACOES, DOADORES, FUNCIONARIOS')
            tabela_consulta = str(input(' Digite o nome da tabela que deseja alterar um registro: ')).upper()

            campo_consulta = str(input(' Digite o campo a ser alterado: '))
            novaInfo_consulta = input(' Digite a nova informação do registro: ')

            campoCondicao_consulta = str(input(' Digite o campo condicional: '))
            valorCondicao_consulta = input(' Digite o valor condicional do campo definido acima: ')

            def funcao_update():
                comando = f'UPDATE {tabela_consulta} SET {campo_consulta} = "{novaInfo_consulta}" WHERE {campoCondicao_consulta} = "{valorCondicao_consulta}";'
                cursor.execute(comando)
                con.commit()

            funcao_update()

    # FUNÇÃO DELETE

    elif id_exec_funcao_sistema == 4:

        if 'conta_doador' == lista_tipo_conta[0]:
            print(' Você não tem acesso a essa funcionalidade, por favor digite outro número.')

        else:

            print(' TABELAS: DOACOES, DOADORES, FUNCIONARIOS')
            tabela_consulta = str(input(' Digite o nome da tabela que deseja deletar um registro: ')).upper()

            campoCondicao_consulta = str(input(' Digite o campo condicional: '))
            valorCondicao_consulta = input(' Digite o valor condicional do campo definido acima: ')

            def funcao_delete():

                comando = f'DELETE FROM {tabela_consulta} WHERE {campoCondicao_consulta} = "{valorCondicao_consulta}"'
                cursor.execute(comando)
                con.commit()

            confirmacao = str(input(' Você realmente deseja deletar esse registro? (SIM/NAO): ')).upper()

            if confirmacao == 'SIM':

                funcao_delete()

            elif confirmacao == 'NAO':

                print(' A solicitação foi cancelada!')

    elif id_exec_funcao_sistema == 0:

        break

    else:
        print(' Você não digitou um número válido, tente novamente!')

### FINALIZAR CONEXÃO COM O DATABASE ###

if con.is_connected():
    cursor.close()
    con.close()
    print(' A conexão ao MySQL foi encerrada!')
