import requests
from bs4 import BeautifulSoup
import json


def get_text(url):
	response = requests.get(url)
	content = response.content
	parser = BeautifulSoup(content, 'html.parser')
	return parser.text


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


if __name__ == "__main__":
	print("Getting urls...")
	page_links = get_page_links()
	DS9_links = page_links[0:173]
	TOS_links = page_links[173:253]
	TAS_links = page_links[253:275]
	TNG_links = page_links[275:451]
	VOY_links = page_links[451:611]
	ENT_links = page_links[611:]

	links = [DS9_links, TOS_links, TAS_links, TNG_links, VOY_links, ENT_links]
	links_names = ['DS9', 'TOS', 'TAS', 'TNG', 'VOY', 'ENT']

	print("Getting series text...")
	all_series_scripts = {}
	for i, series in enumerate(links):
		series_name = str(links_names[i])
		print("Getting "+series_name+" episodes")
		all_series_scripts[series_name] = {}
		episode_script = {}
		all_cast = []
		for j, link in enumerate(series):
			episode = "episode "+str(j)
			text = get_text(link)
			episode_script[episode] = text
		all_series_scripts[series_name] = episode_script
	print("Serialising data...")
	with open('data/all_scripts_raw.json', 'w') as data:
		json.dump(all_series_scripts, data)
	print("Data saved.")
