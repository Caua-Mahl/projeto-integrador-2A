from datetime import datetime
import uuid

# função verifica se existe o arquivo txt.
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# função cria arquivo txt.
def criaArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        linhas(f'erro ao criar arquivo {nome}')


# função de leitura de arquivo txt .
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        linhas('erro ao ler arquivo')
    else:
        print('PESSOAS CADASTRADAS ACADEMIA DO JÃO')
        print(a.read())
    finally:
        a.close()

# função de validação de peso.
def valida_peso(nome):
    nome['peso'] = float(input('Peso em KG. Peso :'))
    while int(nome['peso']) not in range(20, 300):
        linhas('ops, digite um peso válido.')
        nome['peso'] = float(input('Peso em KG. Peso :'))

#função de validação do sexo.
def valida_sexo(nome):
    while True:
        genero = input('digite 1 para sexo masculino ou 2 para sexo feminino.')
        if genero == '1':
            nome['sexo'] = 'M'
            break
        elif genero == '2':
            nome['sexo'] = 'F'
            break
        else:
            linhas('digite uma opção válida.')
            continue


# função de validação da altura.
def valida_altura(nome):
    nome['altura'] = float(input('Altura em metros. Altura :'))
    while int(nome['altura']) not in range(1, 3):
        linhas('ops, digite uma altura válida')
        nome['altura'] = float(input('Altura em metros. Altura :'))


# função valida nome com .split para definir o espaço no nome como separador e não bugar o isalpha.
def valida_nome(nome):
    nome['nome'] = str(input('Nome: '))
    while all(n.isalpha() for n in nome['nome'].split(" ")) == False:
        print('-=' * 30)
        nome['nome'] = str(input('\t ops, digite nome válido. Nome: '))


# função validação do nascimento onde só aceita se for numerico e entre 1900 e 2022.
def valida_nascimento(nome):
    nasc = input('Ano de Nasc: ')
    while True:
        if nasc.isnumeric() and 1900 < int(nasc) < 2022:
            nome['idade'] = datetime.now().year - int(nasc)
            break
        else:
            linhas('ops, digite um ano de nascimento  válido.')
            nasc = input(' Ano de Nasc: ')


# função validação do plano.
def valida_plano(nome):
    while True:
        nome['plano'] = input('escolha seu plano: \n livre = 100,00 reais,acesso ilimitado \n semanal = 70,00 reais, acesso até 3 vezes por semana \n diário = 10,00 reais, acesso 1 vez por semana')
        if nome['plano'] in ('livre', 'semanal', 'diario', 'diário'):
            break
        else:
            linhas('ops, digite um plano válido')


# função cadastra no arquivo txt.
def cadastraArquivo(arq, nome):
    try:
        a = open(arq, 'at')
    except:
        linhas('erro ao cadastrar no arquivo')
    else:
        a.write(f'{nome} \n')
        #a.write(f"{nome['nome']} {nome['idade']} {nome['id']} {nome['sexo']} {nome['peso']} {nome['altura']} {nome['idade']} {nome['plano']} {nome['imc']} {nome['bf']}")
        a.close()

#função de linhas.
def linhas(msg):
    print('=-' * 30)
    print(msg)
    print('=-' * 30)