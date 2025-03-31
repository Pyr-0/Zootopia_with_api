from animals_web_generator import generate_html_from_template, save_html
import data_fetcher

def main():
	try:

		animal_name = input("Enter a name of an animal: ").strip()

		if not animal_name:
			print("❌ Error: Animal name cannot be empty. Please try again.")
			return

		# Fetch animal data using the data_fetcher module
		animals_data = data_fetcher.fetch_animal_data(animal_name)

		if not animals_data:
			print(f"❌ Error: No data found for '{animal_name}'. Please check the spelling or try another animal.")


		# Generate HTML content using the template
		html_content = generate_html_from_template(animals_data, animal_name)

		# Save HTML to file
		save_html(html_content)

		print("✅ Website was successfully generated to the file animals.html.")

	except ConnectionError:
		print("❌ Error: Could not connect to the data source. Please check your internet connection.")
	except ValueError as e:
		print(f"❌ Error: Invalid input - {str(e)}")
	except FileNotFoundError:
		print("❌ Error: Could not create or write to the output file.")
	except Exception as e:
		print(f"❌ An unexpected error occurred: {str(e)}")
		print("Please try again later or contact support if the problem persists.")

if __name__ == "__main__":
	main()
