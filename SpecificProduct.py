import requests
from bs4 import BeautifulSoup


def collect_prices(specific_product):

    # Make an HTTP request to the product page
    url = f"https://www.atacadao.com.br/{specific_product}"
    response = requests.get(url)

    # Parse the HTML page
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the product price
    price = soup.find("span", {"class": "product-box__price--number"}).text

    # Extract the product name
    name = soup.find({"h1"}).text

    return price, name


if __name__ == "__main__":

    # Collect product prices
    products = ["file-de-peito-de-frango-com-sassami-congelado-adoro-por-kg/",
                "carvao-campeao-saco-4kg/"]
    prices, names = [], []

    # To print the collected prices
    for product in products:
        preco_coletado, nome_coletado = collect_prices(product)
        prices.append(preco_coletado)
        names.append(nome_coletado)

    # To print the collected prices and names
    print(names)
    print(prices)
