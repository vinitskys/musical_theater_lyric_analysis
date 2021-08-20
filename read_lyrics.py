"""
Reading the lyrics for a song.
Does NOT parse them or ANYTHING, just reads the entire text chunk and saves it
"""

import pandas as pd
import re

from utils import io
from utils.config import Config

def read_lyrics_for_single_song(song_title, musical_title, song_url):
    """
    Returns df with lyrics -- columns match `Config.lyrics_raw_columns`
    """
    
    html = io.read_html_from_url(song_url)
    try:
        lyrics_chunk = re.search(r'<div id="page">.*?h2>\s*<br>\s*(.*?)<span class="muted">', html, flags=re.DOTALL).group(1)
        
        # must match Config.lyrics_raw_columns -- ['song_title', 'musical_title', 'lyrics']
        data = [(song_title, musical_title, lyrics_chunk)]
        df = pd.DataFrame(data=data, columns=Config.lyrics_raw_columns)
    except:
        raise Exception(f"Failed to read '{song_title}'' from '{musical_title}'")
    
    return df

def read_lyrics_for_all_songs():
    print(f"Reading song lyrics for all songs...")

    song_df = pd.read_csv(Config.song_list_path)

    all_lyrics_df = pd.DataFrame(columns=Config.lyrics_raw_columns)
    # iterative over MUSICAL for better logging
    for musical_title in song_df.musical_title.unique():
        print(f"| Reading song lyrics for musical '{musical_title}")
        musical_df = song_df[song_df.musical_title == musical_title]
        for index, row in musical_df.iterrows():
            my_lyrics = read_lyrics_for_single_song(
                song_title=row['song_title'],
                musical_title=row['musical_title'],
                song_url=row['song_url']
            )
            all_lyrics_df = all_lyrics_df.append(my_lyrics)

    all_lyrics_df.lyrics = io.replace_escaped_html_characters(all_lyrics_df.lyrics)
    all_lyrics_df.lyrics = io.remove_newlines(all_lyrics_df.lyrics)

    all_lyrics_df.to_csv(Config.lyrics_raw_path, index=False)