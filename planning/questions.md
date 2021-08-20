# Questions:

#### High level
- What lyrical features impact musical quality?
- Does this change over time? (i.e. the standard for a "good musical lyric")

#### Character Counts
- How many characters sing a significant amount? -- tagging "leads"
- How many characters have their own songs?
- How many songs does the character with the most solos have?
- How many duets/trios?
- How many unique combinations of chraracters sing together?
- Do shows with more leads do better?

Vocabulary
- song / character / shows vocab size 
- unique words?
- distribution of meaningful words/pronouns/names/prepositions
    density per line/song/char

sentiment analysis?


#### Simple N-grams
- What are the N-grams that appear in the most shows?
- What are the N-grams that appear MOST in EACH show?
- What are the N-grams the appear most often, by VOLUME

#### Lyric patterns (beyond N-grams)
- Does each show have unique lyric patterns? 
- What is each character's "lyric pattern"? 
- What is each song's "lyric pattern"?
- What is the chorus' lyric pattern
- Are there song/character "lyric pattern archetypes" that appear across shows?
- Which shows/songs/characters have similar speech patterns? 
- Impact of song/char lyric pattern variety on success

#### Meaning (LDA and more!)
- What is each show about? Can we group them?
- What does each character sing about? Can we group them within a show? Between shows?
- What is each song about? Can we group them within a show? Between shows?
- What does the chorus sing about? How does this vary between shows?
- Do shows with distinct meanings do better?
- Impact of song/char meaning variety on success

---
#### Misc modifiers
All of the questions above might be affected by any of the following variables. 
Look at how the results vary as you vary the conditions below:

- Musical features (year, popularity, awards, etc...)
- Position of song in show (i.e. act, or more granular)
- Position of lyric in song (i.e. beginning/middle/end)
- Importance of character (i.e. lead or chorus)
---

---
Constructing a question:
1) Pick one of:
* Lyric Pattern
* Meaning

2) Pick one of:
* Show
* Song
* Character

3) Pick one of:
* Unique
* Similar

4) Pick one of:
* Between shows
* Within shows

How does this change with time/impact 
---
