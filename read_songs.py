"""
Using the list of musicals + metadata we have, read the list of each musical's songs + metadata
"""

import re
import pandas as pd

from utils import io
from utils.config import Config

def read_songs_from_single_musical_url(musical_title, musical_url):
    """
    Queries 'url' to get a dataframe of song info, with columns `Config.song_list_columns`
    """
    print(f"| Reading song metadata for musical '{musical_title}'")

    html = io.read_html_from_url(musical_url)

    # trim out any excess things that might get in the way
    lyrics_section = re.search(pattern=r'<section class="lyrics-list">(.*?)</section>', 
                               string=html, 
                               flags=re.DOTALL
                        ).group(1)

    # list containing each song's RE chunk
    song_chunk_list = re.findall(pattern=r'<li>(.*?)</li>',
                                 string=lyrics_section,
                                 flags=re.DOTALL)

    song_number = 1
    act_num = 0
    song_metadata_list = []
    for song_chunk in song_chunk_list:
        
        # check if it's an act break title
        # some musical have act titles -- i.e "Act 1: breaking and entering"
        act_num_regex = re.search(r'<span class="grey">\s*Act\s+(\d)(.*)?</span>', song_chunk)
        if act_num_regex:
            act_num = act_num_regex.group(1)
            continue
        
        # song that's missing lyrics (these DO HAVE links)
        add_lyrics_button_html = '<img src="/images/img/add.gif" border="0" align="absmiddle" alt="add">'
        if add_lyrics_button_html in song_chunk:
            song_number += 1
            continue

        # Any other thing is who cares
        if 'href' not in song_chunk:
            continue

        try:

            song_url = re.search(pattern=r'<a href="(.*?)">', string=song_chunk).group(1)
            song_title = re.search(pattern=r'>(.*?)</a>', string=song_chunk).group(1)

            # ['song_title', 'musical_title', 'song_number', 'act_number', 'song_url']
            my_metadata = (song_title, musical_title, song_number, act_num, song_url)
            song_metadata_list.append(my_metadata)
            
            song_number += 1
        except:
            print(song_chunk)
            raise Exception("OOPS")

    songs_df = pd.DataFrame(data=song_metadata_list, columns=Config.song_list_columns)
    return songs_df

def read_songs_from_all_musicals():
    """
    Main entrypoint. Read every song name+metadata from every musical, saving as csv
    """
    print("Reading list of songs from each musical...")


    musicals_df = pd.read_csv(Config.musical_list_path)
    
    all_songs_df = pd.DataFrame(columns=Config.song_list_columns)
    for index, row in musicals_df.iterrows():

        musical_title = row['musical_title']
        musical_url_suffix = row['musical_url_suffix']
        musical_url = f'{Config.base_url}{musical_url_suffix}'

        my_songs_df = read_songs_from_single_musical_url(musical_title=musical_title, musical_url=musical_url)

        all_songs_df = all_songs_df.append(my_songs_df)

    all_songs_df.song_title = io.replace_escaped_html_characters(all_songs_df.song_title)
    all_songs_df.to_csv(Config.song_list_path, index=False)