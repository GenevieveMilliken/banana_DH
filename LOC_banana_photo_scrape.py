# scrapes about 30 images of laborers and bananas at the Port of New Orleans from LOC Photo Collection

from bs4 import BeautifulSoup
import requests
import json 
import time

all_my_data = []

for pages in range(0,3):
	url = f"https://www.loc.gov/pictures/search/?q=New+Orleans+banana&sp={pages*1}"

	results_page = requests.get(url)
	page_html = results_page.text
	soup = BeautifulSoup(page_html, "html.parser")

	items = soup.find_all("div", attrs = {'class': 'result_item'})

	for item in items: 

		my_data = {
			"digital_object_URL" : None,
			"LOC_Call_Number": None,
			"image_URL": None, 
			"caption": None,
			"date": None,
		}

		print("--------------")

		digital_object_URL = item.find('a')
		abs_url = digital_object_URL['href']
		my_data['digital_object_URL'] = abs_url
		# print(abs_url)

		caption = digital_object_URL.text
		my_data['caption'] = caption
		# print(caption)

		object_page = requests.get(abs_url)
		object_html = object_page.text
		object_soup = BeautifulSoup(object_html, "html.parser")

		LC_Call_Number = object_soup.find("div", attrs = {'id': 'onsite'})
		LC_Call_Number = LC_Call_Number.find('li')
		LC_Call_Number = LC_Call_Number.text
		LC_Call_Number = LC_Call_Number.replace("Call Number:", "")
		LC_Call_Number = LC_Call_Number.replace("\n", "")
		LC_Call_Number = LC_Call_Number.replace("\t", "")
		my_data['LOC_Call_Number'] = LC_Call_Number
		# print(LC_Call_Number)

		try: 
			image_URL = object_soup.find_all("link", attrs = {'type': 'image/jpg'})
			image_URL = image_URL[1]
			image_URL = image_URL['href']
			image_URL = image_URL.replace("//","")
			my_data['image_URL'] = image_URL
			# print(image_URL)
		except IndexError: 
			pass 

		date = object_soup.find("meta", attrs= {'name': 'dc.date'})
		date = date['content']
		my_data['date'] = date
		# print(date)
		
		time.sleep(1)

		all_my_data.append(my_data)

with open('LOC_Bananas_Port_NOLA.json', 'w') as file_object:
	json.dump(all_my_data, file_object, indent=2)
	print("JSON file is Ready")

	




	