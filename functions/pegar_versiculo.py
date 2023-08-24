import requests
import re
from book_lists import books
from bs4 import BeautifulSoup

def pegar_versiculo(
        nome, 
        cap, 
        vers_inicio, 
        vers_fim=None
    ):
    
    if nome.lower() in books.at1:
        base_url = books.at_1[nome.lower()]
        
    elif nome.lower() in books.nt_1:
        base_url = books.nt_1[nome.lower()]
        
    elif nome.lower() in books.at_2:
        base_url = books.at_2[nome.lower()]
        
    elif nome.lower() in books.nt_2:
        base_url = books.nt_2[nome.lower()]

    url = f'{base_url}.{cap}?ed=MS'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        html = resposta.text
        soup = BeautifulSoup(html, 'html.parser')
        
        verses = []
        for vers in range(int(vers_inicio), int(vers_fim or vers_inicio) + 1):
            vers_div = soup.find('div', string=re.compile(rf'^\[{vers}\] '))
            
            if vers_div:
                verses.append(vers_div.get_text(strip=True))
        return ' '.join(verses)
