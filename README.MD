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

---

## Added notes:

Source: https://www.kaggle.com/datasets/gjbroughton/start-trek-scripts by GARY BROUGHTON

9 extra notebooks included under "Code" Tab on above source

* [Text Generation-NLP-LSTM](https://www.kaggle.com/code/apoorvchaudhary/text-generation-nlp-lstm)
* [Character Identifier using Naive Bayes Variations](https://www.kaggle.com/code/eatmygoose/character-identifier-using-naive-bayes-variations)
* [Visualize Star Trek Characters Sharing Scenes](https://www.kaggle.com/code/kelly713/visualize-star-trek-characters-sharing-scenes)
* [Who has the most lines in (insert Trek here)](https://www.kaggle.com/code/levimuller/who-has-the-most-lines-in-insert-trek-here)
* [Who has the most words and lines in DS9?](https://www.kaggle.com/code/zoiaran/who-has-the-most-words-and-lines-in-ds9/data)
* [Picard - Make it So](https://www.kaggle.com/code/abaskingrootwalla/picard-make-it-so)
* [Who has the most lines in TNG?](https://www.kaggle.com/code/ucffool/who-has-the-most-lines-in-tng)
* [Who has the most lines in DS9 ?](https://www.kaggle.com/code/gjbroughton/who-has-the-most-lines-in-ds9)
* [Starter: Star Trek Scripts 931c8144-7](https://www.kaggle.com/code/kerneler/starter-star-trek-scripts-931c8144-7)

