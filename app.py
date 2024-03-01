import requests


def extrair_numeros(texto: str):
    numeros = "".join(num for num in texto if num.isdigit())
    return numeros


def busca_cep(numero_cep: str):
    cep = extrair_numeros(numero_cep)
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if resposta.status_code != 200:
        return "CEP inválido."

    else:
        dados_cep = resposta.json()
        if "erro" in dados_cep:
            return "CEP inválido."
        else:
            print(f'LOGRADOURO: {dados_cep["logradouro"].upper()}')
            print(f'BAIRRO: {dados_cep["bairro"].upper()}')
            print(f'LOCALIDADE: {dados_cep["localidade"].upper()}')
            print(f'UF: {dados_cep['uf'].upper()}')


def busca_cnpj(cnpj: str):
    resposta = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")

    if resposta.status_code != 200:
        return "CNPJ inválido."

    else:
        dados_cnpj = resposta.json()
        if dados_cnpj["status"] != "OK":
            return "CNPJ inválido."
        else:
            print(f'CNPJ: {dados_cnpj["cnpj"]}')
            print(f'RAZAO SOCIAL: {dados_cnpj["nome"].upper()}')
            if 'fantasia' in dados_cnpj and dados_cnpj["fantasia"] != "":
                print(f'NOME FANTASIA: {dados_cnpj["fantasia"].upper()}')
            cep_cnpj = extrair_numeros(dados_cnpj["cep"])
            busca_cep(cep_cnpj)
            print(f'NUMERO: {int(dados_cnpj["numero"])}')
            if 'complemento' in dados_cnpj and dados_cnpj['complemento'] != "":
                print(f'COMPLEMENTO: {dados_cnpj["complemento"].upper()}')


# main
opcoes = {1: "CEP", 2: "CNPJ"}
for k, v in opcoes.items():
    print(f"{k} para {v}")
escolha = int(input("Escolha uma opcao para consultar: "))

match escolha:
    case 1:
        busca_cep(input("Digite um CEP para consultar: "))

    case 2:
        busca_cnpj(input("Digite um CNPJ para consultar: "))
