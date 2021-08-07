from bs4 import BeautifulSoup
import requests

# objeto site recebe o conteudo da requisaão http do site
site = requests.get('https://www.climatempo.com.br/').content

# o objeto soup baixa o site - o html
soup = BeautifulSoup(site, 'html.parser')

# transforma html em string e o print vai exibir o html
print(soup.prettify())

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

#print(temperatura.string)
print(soup.title.string)
