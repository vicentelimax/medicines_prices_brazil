import re

from pages.tools.data_pack_item import data_pack_item

def extract_factor(text, keywords):
    """
    Extract the first numeric value found before any of the keywords in the list.
    Context: Looks for packs of items in the text and returns the factor of the pack.
    Args:
        text (str): The input text to search.
        keywords (list): A list of keywords to look for after the numeric value.

    Returns:
        int: The first numeric value found before a keyword, or None if no match is found.
    """
    patterns = [re.compile(r'(\d+)\s*' + re.escape(keyword)) for keyword in keywords]
    for pattern in patterns:
        match = pattern.search(text)
        if match:
            return int(match.group(1))
    return 1

def add_factor_price(dataframe):
    """
    Add a columns with the factor of the pack of items calculated.
    Args:
        dataframes: The dataframe to add the new column
    Returns:
        dataframe: Dataframe plus the new column 'fator'
    """

    data = data_pack_item()
    dataframe['fator'] = dataframe['APRESENTAÇÃO'].apply(lambda x: extract_factor(x, data))

    return dataframe