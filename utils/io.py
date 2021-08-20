import requests

def read_html_from_url(url):
    """
    reads a URL, returning the html as a string
    """
    r = requests.get(url)
    return r.text

def replace_escaped_html_characters(col):
    """
    cleans a column (series) by replacing html escape sequences
    """

    col = col.str.replace('&#039;', "\'")
    col = col.str.replace("&amp;", "&")

    return col
