# Requires "requests" to be installed (see python-requests.org)
import requests

def rm_bg(img_path):

	response = requests.post(
		'https://api.remove.bg/v1.0/removebg',
		files={'image_file': img_path},
		data={'size': 'auto'},
		headers={'X-Api-Key': 'tgGDqPuRPVDrz8zVuoPd4nFn'},
	)
	if response.status_code == requests.codes.ok:
		with open('no-bg.png', 'wb') as out:
			out.write(response.content)
			return out
	else:
		print("Error:", response.status_code, response.text)