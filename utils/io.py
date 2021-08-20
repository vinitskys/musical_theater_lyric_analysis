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
    col = col.str.replace('&quot;', "\"")
    col = col.str.replace("&amp;", "&")

    # also trim whitespace here too haha
    col = col.str.strip()

    return col

def remove_newlines(col):
    """
    Newlines (\r or \n) mess up the CSV file.
    But we have <br> to denote the newlines in the html! So we're good
    """

    col = col.str.replace('\r', '')
    col = col.str.replace('\n', '')

    return col