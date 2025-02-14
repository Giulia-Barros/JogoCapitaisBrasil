import random

def obter_dicionario_estados():
    return {
        "Rio Grande do Sul": "Porto Alegre",
        "Santa Catarina": "Florianópolis",
        "Paraná": "Curitiba",
        "São Paulo": "São Paulo",
        "Minas Gerais": "Belo Horizonte",
        "Rio de Janeiro": "Rio de Janeiro",
        "Espírito Santo": "Vitória",
        "Goiás": "Goiânia",
        "Mato Grosso do Sul": "Campo Grande",
        "Mato Grosso": "Cuiabá",
        "Amazonas": "Manaus",
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
        "Sergipe": "Aracaju"
    }

def sortear_estado(dicionario_estados):
    return random.choice(list(dicionario_estados.keys()))

def jogo():
    dicionario_estados = obter_dicionario_estados()
    estado = sortear_estado(dicionario_estados)
    resposta = input(f'Qual é a capital do Estado {estado}? ').strip()
    
    if resposta.lower() == dicionario_estados[estado].lower():
        print("Acertou!")
    else:
        print(f"Errou! A capital correta de {estado} é {dicionario_estados[estado]}.")

def jogarNovamente():
    while True:
        jogo()
        repetir = input('Mais uma rodada? (S-Sim ou N-Não): ').strip().lower()
        
        if repetir != 's':
            break

jogarNovamente()
