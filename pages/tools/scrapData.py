import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_data_url_from_anvisa():
    """Get the URL of the Excel file from the ANVISA website
    return: 
        bs4 link object: str
    """
    url = "https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos"
    # Ignora a verificação SSL
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the link with "xls_conformidade_site" in href
    link = soup.find('a', href=lambda href: href and "xls_conformidade_site" in href)
    if link:
        return link['href']
    else:
        raise Exception("Excel file link not found")
    


