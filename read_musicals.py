"""
A job to read in each musical's metadata -- year, name, and url extension

Saves output to a file
"""
import re
import pandas as pd

from utils import io
from utils.config import Config

def extract_musical_metadata_from_html(html_text):
    """
    Given the full text of a 'letter' page from 'allmusicals.com',
    extract each musicals name + year, as well as a link to the musical's own page

    Returns a list of (name, year, musical_url) tuples
    """

    ### 1) find the releveant portion of text for each musical
    # each musical is a list item!
    list_pattern = r'<li>.*?</li>'
    text_chunk_list = re.findall(list_pattern, html_text, flags=re.DOTALL)

    ### 2) remove any that don't fit the mold 
    musical_text_list = []
    for chunk in text_chunk_list:
        if 'span' in chunk and 'href' in chunk:
            musical_text_list.append(chunk)

    
    ### 3) extract relevant fields
    musical_metadata_list = []
    for chunk in musical_text_list:

        year = re.search(r'<span class="label">(\d{4})</span>', chunk).group(1)
        url = re.search(r'href="(.*?)"', chunk).group(1)
        name = re.search(r'>(.*?) Lyrics', chunk).group(1)

        my_info = (name, year, url)
        musical_metadata_list.append(my_info)

    return musical_metadata_list

def read_musicals():
    """
    Main method
    """

    print("Reading list of musicals...")

    musical_metadata_list = []
    FIRST_LETTER_INT = 97
    LAST_LETTER_INT = FIRST_LETTER_INT + 26
    for letter_int in range(FIRST_LETTER_INT, LAST_LETTER_INT):
        letter = chr(letter_int)
        html = io.read_html_from_url(f"{Config.base_url}/{letter}.htm")

        letter_metadata_list = extract_musical_metadata_from_html(html)
        musical_metadata_list.extend(letter_metadata_list)

    musicals_df = pd.DataFrame(musical_metadata_list, columns=["musical_title", "year", "musical_url_suffix"])
    
    musicals_df.musical_title = io.replace_escaped_html_characters(musicals_df.musical_title)
    musicals_df.to_csv(Config.musical_list_path, index=False)
