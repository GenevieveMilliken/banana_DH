# WIP script 
# scrapes 34 images of laborers and bananas at the Port of New Orleans from LOC Photo Collection

from bs4 import BeautifulSoup
import requests
import json 
from time import sleep

all_my_data = []

for pages in range(0,3):
	url = f"https://www.loc.gov/pictures/search/?q=New+Orleans+banana&sp={pages*1}"

	results_page = requests.get(url)
	page_html = results_page.text
	soup = BeautifulSoup(page_html, "html.parser")

	items = soup.find_all("div", attrs = {'class': 'result_item'})

	for item in items: 

	# 	# my_data = {
	# 	# 	"digital_object_URL" : None,
	# 	# 	"image_URL": None, 
	# 	# 	"caption": None,
	# 	# 	"date": None,
	# 	# 	"LC_Call_Number": None,
	# 	# }

		print("--------------")

		digital_object_URL = item.find('a')
		abs_url = digital_object_URL['href']
		# my_data['digital_object_URL'] = abs_url
		print(abs_url)

		caption = digital_object_URL.text
		# my_data['caption'] = caption
		print(caption)

		object_page = requests.get(abs_url)
		object_html = object_page.text
		object_soup = BeautifulSoup(object_html, "html.parser")

		# image_URL = object_soup.find

	# 	# date = object_soup.find

		LC_Call_Number = object_soup.find("div", attrs = {'id': 'onsite'})
		LC_Call_Number = LC_Call_Number.find('li')
		LC_Call_Number = LC_Call_Number.text
		LC_Call_Number = LC_Call_Number.replace("Call Number:", "")
		print(LC_Call_Number)

		time.sleep(5)




	