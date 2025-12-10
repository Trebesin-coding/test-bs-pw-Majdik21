from bs4 import BeautifulSoup as bs
import json
import requests

file= 'recept.json'
url = 'https://souhrada.github.io/bsoup-exam/'

def main():

    bs(response.content, "html.parser") #<--- Úkol: popiš krátce, co tohle dělá = nacte content na strance
    
    response = requests.get(url)

    list = bs.find_all('h2')

    ingredients = list[0,1,2,3]

    for i in ingredients:
        print(i)

    json.dump(ingredients, file, indent =4 )

    
    
    



if __name__ == "__main__":
    main()


