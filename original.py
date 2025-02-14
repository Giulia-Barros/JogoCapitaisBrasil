import random

def sortearEstados():
    dicionarioEstados = {"Rio Grande do Sul": "Porto Alegre",
                         "Santa Catarina": "Florianópolis",
                         "Paraná": "Curitiba",
                         "São Paulo": "São Paulo",
                         "Minas Gerais": "Belo Horizonte",
                         "Rio de Janeiro": "Rio de Janeiro",
                         "Espírito Santo": "Vitória",
                         "Goias": "Goiânia",
                         "Mato Grosso do Sul": "Campo Grande",
                         "Mato Grosso": "Cuiabá",
                         "Amazona": "Manaus",
                         "Rondônia": "Porto Velho",
                         "Acre": "Rio Branco",
                         "Roraima": "Boa Vista",
                         "Amapá": "Macapá",
                         "Pará": "Belém",
                         "Tocantins": "Palmas",
                         "Maranhão": "São Luís",
                         "Bahia": "Salvador",
                         "Piauí": "Teresina",
                         "Ceará": "Fortaleza",
                         "Rio Grande do Norte": "Natal",
                         "Paraíba": "João Pessoa",
                         "Pernambuco": "Recife",
                         "Alagoas": "Maceió",
                         "Sergipe": "Aracaju"} 

    
    # sortear = random.choice(list(dicionarioEstados.keys()))
    # print(sortear)
    return random.choice(list(dicionarioEstados.keys()))
    
def jogo():
    estado = sortearEstados()
    resposta = input(f'Qual é a capital do Estado {estado}? ')
    return resposta

def validacao(d, resposta):
    keys = []
    for key, val in d.items():
        if val == resposta:
            keys.append(key)
    return keys  
 
res = jogo()
est = sortearEstados()  
   

keys = validacao(est, res)

if est == keys:
    print('Acertou')
else:
    print('Errou')

def jogarNovamente():
    
    novoJogo = jogo()
    repetir = input('Mais um rodada? \n A Resposta deve ser Sim ou Não ')

    if repetir == 'Sim'.lower():
        for i in novoJogo:
           return novoJogo()
   break



#jogo()
