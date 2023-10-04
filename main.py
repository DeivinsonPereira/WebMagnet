import requests
from bs4 import BeautifulSoup
def coletar_precos(produto):
    # Fazer uma requisição HTTP para a página do produto
    url = f"https://www.atacadao.com.br/{produto}"
    response = requests.get(url)

    # Parsear a página HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Extrair o preço do produto
    preco = soup.find("span", {"class": "product-box__price--number"}).text

    # Extrair o nome do produto
    nome = soup.find({"h1"}).text

    return preco, nome

if __name__ == "__main__":
    # Coletar preços de produtos
    produtos = ["file-de-peito-de-frango-com-sassami-congelado-adoro-por-kg/",
                "carvao-campeao-saco-4kg/"]
    precos, nomes = [], []

    # Imprimir os preços coletados
    for produto in produtos:
        preco_coletado, nome_coletado = coletar_precos(produto)
        precos.append(preco_coletado)
        nomes.append(nome_coletado)

        # Imprimir os preços e nomes coletados
    print(precos)
    print(nomes)
