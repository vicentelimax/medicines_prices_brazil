import re

from pages.tools.data_pack_item import data_pack_item

def extract_factor(text, keywords):
    patterns = [re.compile(r'(\d+)\s*' + re.escape(keyword)) for keyword in keywords]
    for pattern in patterns:
        match = pattern.search(text)
        if match:
            return int(match.group(1))
    return None

def add_factor_price(dataframe):


    data = data_pack_item()
    dataframe['fator'] = dataframe['APRESENTAÇÃO'].apply(lambda x: extract_factor(x, data))

    return dataframe