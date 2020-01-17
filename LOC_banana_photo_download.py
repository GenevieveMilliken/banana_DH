import json
import urllib.request

def download_image(url, file_path, caption):
	full_path = file_path + caption + '.jpg'
	try:
		urllib.request.urlretrieve(url, full_path)
	except TypeError:
		pass

# # open json file, extract information, write images to file
# with open('LOC_Bananas_Port_NOLA.json') as f_object:
# 	text = json.load(f_object)
# 	for data_dict in text:
# 		caption = data_dict['LOC_Call_Number']
# 		url = data_dict['image_URL']
# 		download_image(url, "Images/", caption)

# download_image('http://cdn.loc.gov/service/pnp/det/4a10000/4a17000/4a17000/4a17030v.jpg', "Images/", "test")