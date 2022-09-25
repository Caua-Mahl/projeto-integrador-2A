import pandas as pd
import interface as it

# cria o dicionário.
dados = dict()
dados['nome'] = True
dados['idade'] = True
dados['id'] = True
dados['sexo'] = True
dados['peso'] = True
dados['altura'] = True
dados['plano'] = True
dados['imc'] = True
dados['bf'] = True
#nomeia o arquivo txt.
arquivo = 'Cadastros_Academia_do_Jão'
if not it.arquivoExiste(arquivo):
    it.criaArquivo(arquivo)
# processo
while True:
    it.linhas('BEM VINDO AO SISTEMA DA ACADEMIA DO JÃO')
    escolha = input('ESCOLHA UMA DAS OPÇÕES:\n 1- cadastrar cliente \n 2- checar lista de cadastros \n 3- sair do programa')
    if escolha == '1':
        while True:
            it.valida_nome(dados)
            it.linhas('Nome válido')
            it.valida_nascimento(dados)
            it.linhas('ano de nascimento válido')
            dados['id'] = it.uuid.uuid1()
            it.valida_sexo(dados)
            while True:
                try:
                    it.valida_peso(dados)
                    break
                except ValueError:
                    it.linhas('ops, digite um peso válido')
            it.linhas('peso válido')
            # altura.
            while True:
                try:
                    it.valida_altura(dados)
                    break
                except ValueError:
                    it.linhas('ops, digite uma altura válida')
            it.linhas('altura válida')
            it.valida_plano(dados)
            it.linhas('plano válido')
            it.linhas('CADASTRO REALIZADO COM SUCESSO')
            dados['imc'] = round((dados['peso']) / ((dados['altura']) ** 2), 2)
            if dados['sexo'] in 'Mm':
                dados['bf'] = round((1.20 * (dados['imc']) + (0.23 * (dados['idade'])) - (10.8 * 1) - 5.4), 2)
            else:
                dados['bf'] = round((1.20 * (dados['imc']) + (0.23 * (dados['idade'])) - (10.8 * 0) - 5.4), 2)
            dados_df = pd.DataFrame([dados])
            print(dados_df)
            it.cadastraArquivo(arquivo, dados)
            dados = dict()
            recomecar = input('Deseja cadastrar mais alguém? [S/N]')
            while recomecar not in 'SsNn':
                it.linhas('opção inválida')
                recomecar = input('Deseja cadastrar mais alguém? [S/N]')
            if recomecar in 'nN':
                break
    elif escolha == '2':
        it.lerArquivo(arquivo)
    elif escolha == '3':
        it.linhas('SAINDO DO SISTEMA, TCHAU.')
        break
    else:
        it.linhas('\t digite uma opção válida')