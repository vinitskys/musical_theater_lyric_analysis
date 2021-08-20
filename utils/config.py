class Config:
    
    # URLs
    base_url = 'https://www.allmusicals.com'
    
    # data paths
    data_path = 'data'
    musical_list_path = f'{data_path}/musical_metadata.csv'
    song_list_path = f'{data_path}/song_metadata.csv'
    lyrics_raw_path = f'{data_path}/lyrics_raw.csv'

    song_list_columns = ['song_title', 'musical_title', 'song_number', 'act_number', 'song_url']
    lyrics_raw_columns = ['song_title', 'musical_title', 'lyrics']