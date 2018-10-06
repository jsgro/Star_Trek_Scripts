# Star-Trek-Scripts-Text

Data scraped from data from http://www.chakoteya.net/StarTrek/index.html

So I could have a play around with information retrieval techniques, nlp and basic web scraping, the dataset generated raw scripts and processed lines from all episodes of:

Star Trek The Original Series (TOS)
Star Trek The Animated Series (TAM)
Star Trek The Next Generation (TNG)
Star Trek Deep Space Nine (DS9)
Star Trek Voyager (VOY)
Star Trek Enterprise (ENT)

To run, first clone repo, open cmd in root directory:

run python scrape.py to scrape data and generate all_scripts_raw.json in data directory.

then run python process.py to process the raw text into character lines.

Structure of all_series_lines.json:

all_series_line={series_name:{episode number:{character:all_lines}}}

e.g. all_series_lines['DS9']['episode 0']['SISKO'] gets all of Sisko's lines from the pilot of DS9.