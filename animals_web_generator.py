import os
from datetime import datetime

def generate_animal_card(animal):
	"""
	Generate HTML for a single animal card.
	"""
	# Get the animal name
	name = animal.get('name', 'Unknown')
		
	# Start the animal card
	html = f'''
	<li class="cards__item">
		<h2 class="card__title">{name}</h2>
		
		<div class="card__text">
			<h3 class="section-heading">Taxonomy</h3>
			<ul class="animal-details">
	'''

	# Add taxonomy section
	taxonomy = animal.get('taxonomy', {})
	for key, value in taxonomy.items():
		if value:  # Only include non-empty values
			html += f'''
				<li class="detail-item"><strong>{key.capitalize()}:</strong> {value}</li>
			'''

	html += '''
			</ul>
	'''

	# Add locations section
	locations = animal.get('locations', [])
	if locations:
		html += '''
			<h3 class="section-heading">Locations</h3>
			<ul class="locations-list">
		'''
		for location in locations:
			html += f'''
				<li>{location}</li>
			'''
		html += '''
			</ul>
		'''

	# Add characteristics section
	html += '''
			<h3 class="section-heading">Characteristics</h3>
			<ul class="animal-details">
	'''

	characteristics = animal.get('characteristics', {})
	for key, value in characteristics.items():
		if value:  # Only include non-empty values
			html += f'''
				<li class="detail-item"><strong>{key.capitalize().replace('_', ' ')}:</strong> {value}</li>
			'''
	html += '''
			</ul>
		</div>
	</li>
	'''
	return html

def generate_animals_content(animals_data, animal_name):
	"""
	Generate HTML content for all animals or error message if none found.
	"""
	if not animals_data:
		return f'''
		<div class="error-message">
			<h2>No results found</h2>
			<p>The animal "{animal_name}" doesn't exist in our database or no information was found.</p>
			<p>Please try another animal name.</p>
		</div>
		'''
	# Start the cards list
	html = '<ul class="cards">'
	# Generate HTML for each animal
	for animal in animals_data:
		html += generate_animal_card(animal)
	# Close the cards list
	html += '</ul>'
	return html

def generate_html_from_template(animals_data, animal_name):
	"""	Generate HTML from template file and dynamic data."""

	# Generate the animals content
	animals_content = generate_animals_content(animals_data, animal_name)

	# Read the template file
	template_path = os.path.join('templates', 'animals_template.html')
	try:
		with open(template_path, 'r', encoding='utf-8') as file:
			template = file.read()
	except FileNotFoundError:
		print(f"Error: Template file not found at {template_path}")
		return f"<html><body><h1>Error</h1><p>Template file not found. Please make sure {template_path} exists.</p></body></html>"

	# Replace placeholders with actual content
	html_content = template.replace('{{ANIMAL_NAME}}', animal_name)
	html_content = html_content.replace('{{ANIMALS_CONTENT}}', animals_content)
		
	return html_content

def save_html(html_content, filename="animals.html"):
	"""Save HTML content to a file.	"""
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(html_content)
