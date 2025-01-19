import requests
from bs4 import BeautifulSoup

def get_data_url_from_anvisa():
    url = "https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the link with "xls_conformidade_site" in href
    link = soup.find('a', href=lambda href: href and "xls_conformidade_site" in href)
    if link:
        return link['href']
    else:
        raise Exception("Excel file link not found")


