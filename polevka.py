from bs4 import BeautifulSoup as bs
import json
import requests

file = "recept.json"
url = "https://souhrada.github.io/bsoup-exam/"


def main():

    # chybí vytvoření proměnné, např. soup pro uložení kódu níže
    bs(
        response.content, "html.parser"
    )  # <--- Úkol: popiš krátce, co tohle dělá = nacte content na strance

    response = requests.get(
        url
    )  # vytvoření response musí být před tím, než jej použijete

    list = bs.find_all("h2")

    ingredients = list[
        0, 1, 2, 3
    ]  # takto nelze pracovat s listem, proč raději nepoužijete ve for loopu range(4)?

    for i in ingredients:
        print(i)

    # chybí witf open a syntax jsonu
    json.dump(ingredients, file, indent=4)


if __name__ == "__main__":
    main()
