import os
from dotenv import load_dotenv
import requests

load_dotenv()

"""Setup for API access and the URL endpoint"""

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_animal_data(animal_name):
	"""
	Fetches animal data from the API using the provided animal name.
	Returns a dictionary with the animal's details.
	"""

	# Set up the URL for the API request
	url = API_URL

	# Set up the parameters for the API request
	params = {"name": animal_name}

	# Set up the headers for the API request
	headers = {
		"X-Api-Key": API_KEY
	}

	try:

		response = requests.get(url, headers=headers, params=params)

		if response.status_code == 200:
			# Parse the JSON response
			animals_data = response.json()
			return animals_data
		else:
			print(f"Error: API request failed with status code  {response.status_code}")
			return []
	except Exception as e:
		print(f"Error: {e}")
		return []

