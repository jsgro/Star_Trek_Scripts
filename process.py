import requests
from bs4 import BeautifulSoup
import re
import nltk
import json


def clean_text(script):
	script_clean = script.strip()
	script_clean = script_clean.replace("\n", "")
	script_clean = script_clean.replace("\r", " ")
	script_clean = script_clean.replace("\r\n", "")
	script_clean = re.sub("([\(\[]).*?([\)\]])", "", script_clean)
	script_clean = re.sub(r'\.([a-zA-Z])', r'. \1', script_clean) #remove missing whitespace between character lines.
	script_clean = re.sub(r'\!([a-zA-Z])', r'! \1', script_clean)
	script_clean = re.sub(r'\?([a-zA-Z])', r'? \1', script_clean)
	return script_clean


def get_cast(script_clean):
	tokens = nltk.word_tokenize(script_clean)
	cast = []
	for word in tokens:
		if re.search("\\b[A-Z]{3,}\\b", word) is not None:
			cast.append(word)
	return list(set(cast))


def get_lines(script_clean, cast):
	split_script = script_clean.split(':')
	lines_dict = dict.fromkeys(cast)
	for cast_member in cast:
		lines = []
		for i in range(len(split_script)-1):
			if cast_member in split_script[i].strip().split(" "):
				line = split_script[i+1].strip().split(" ")
				line = [word for word in line if word != '']
				for member in cast:
					if member in line:
						line.remove(member)
				line = ' '.join(line)
				lines.append(line)
		lines_dict[cast_member] = lines

	return lines_dict


def get_page_links():
	top_links = ["http://www.chakoteya.net/DS9/episodes.htm",
				 "http://www.chakoteya.net/StarTrek/episodes.htm",
				 "http://www.chakoteya.net/NextGen/episodes.htm",
				 "http://www.chakoteya.net/Voyager/episode_listing.htm",
				 "http://www.chakoteya.net/Enterprise/episodes.htm"]
	short_links = ["http://www.chakoteya.net/DS9/",
				   "http://www.chakoteya.net/StarTrek/",
				   "http://www.chakoteya.net/NextGen/",
				   "http://www.chakoteya.net/Voyager/",
				   "http://www.chakoteya.net/Enterprise/"]
	links_list = []
	names_list = []
	for i, link in enumerate(top_links):
		response = requests.get(link)
		content = response.content
		parser = BeautifulSoup(content, 'html.parser')
		urls = parser.find_all('a')
		for page in urls:
			links_list.append(short_links[i]+str(page.get('href')))
			name = page.text
			name = name.replace('\r\n',' ')
			names_list.append(name)

	links_to_remove = ['http://www.chakoteya.net/Voyager/fortyseven.htm',
						'http://www.chakoteya.net/Voyager/LineCountS1-S3.htm',
						'http://www.chakoteya.net/Voyager/LineCountS4-S7.htm',
						'http://www.chakoteya.net/Enterprise/fortyseven.htm']

	links_list = [link for link in links_list if (link.endswith('.htm')) & (link not in links_to_remove)]

	return links_list


def convert_raw_to_txt():
	with open(r'data\all_scripts_raw.json') as f:
		data = json.load(f)

	with open(r'C:\Users\gbroughton\Portfolio\NLP Web Scraper\data\scripts.txt', 'w+', encoding="utf-8") as file:
		for series in list(data.keys()):
			for ep in list(data[series].keys()):
				file.write(data[str(series)][ep])


if __name__ == "__main__":
	page_links = get_page_links()
	print("Getting raw scripts...")
	with open('data/all_scripts_raw.json', 'r') as data:
		all_scripts_raw = json.load(data)
		
	links_names = ['DS9', 'TOS', 'TAS', 'TNG', 'VOY', 'ENT']
	print("Processing lines...")
	all_series_lines={}
	for i, series in enumerate(links_names):
		print("Processing "+series+" lines...")
		series_name = str(links_names[i])
		all_series_lines[series_name] = {}
		all_lines_dict = {}
		all_cast = []
		for j, episode in enumerate(all_scripts_raw[series]):
			script = all_scripts_raw[series][episode]
			cleaned_script = clean_text(script)
			cast = get_cast(cleaned_script)
			for member in cast:
				if member not in all_cast:
					all_cast.append(member)
			lines_dict = get_lines(cleaned_script, all_cast)
			all_lines_dict[episode] = lines_dict
		all_series_lines[series] = all_lines_dict

	print("Serialising lines data...")
	
	with open('data/all_series_lines.json', 'w') as data:
		json.dump(all_series_lines, data)

	convert_raw_to_txt()

	print("Data saved.")
