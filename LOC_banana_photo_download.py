import json
import requests

def download_image(url, file_path, caption):
	full_path = file_path + caption + '.jpg'
	try:
		urllib.request.urlretrieve(url, full_path)
	except FileNotFoundError:
		pass

# open json file, extract information, write images to file
with open('LOC_Bananas_PortNOLA.json') as f_object:
	text = json.load(f_object)
	for data_dict in text:
		caption = data_dict['LOC_Call_Number']
		url = data_dict['image_URL']
		download_image(url, "Images/", caption)