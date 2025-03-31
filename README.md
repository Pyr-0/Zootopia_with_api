# 🦊 My Zootopia API

A **simple and fun Python application** that fetches animal information from [API Ninjas Animals API](https://api-ninjas.com/api/animals) and generates a simple, responsive HTML webpage to display the data. 

---

## 🌍 Project Overview
This project lets users **search for animals by name**, fetches their details from an external API, and presents the data in a visually appealing way. The generated HTML includes **taxonomy, locations, and characteristics** of the requested animals.

---

## ✨ Features
✅ Fetch **real-time animal data** from API Ninjas  
✅ Accept **user input** for animal searches  
✅ Generate a **responsive HTML webpage** dynamically  
✅ Handle cases where animals **are not found gracefully**  
✅ Clean and **modular code structure** for easy understanding  

---
### 📂 Current Project Structure
```
zootopia_api/
├── 🐍 animals_web_generator.py → Main script that generates the webpage
├── 🌐 data_fetcher.py → Module that interacts with the API
├── 🔑 .env → Configuration file for storing the API key securely
├── 📋 requirements.txt → List of dependencies for easy setup
└── 📝 README.md → Project documentation
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```sh
git clone https://github.com/yourusername/My_Zootopia_API.git
cd My_Zootopia_API
```

### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Configure API Key
Create a `.env` file in the project directory and add:
```sh
API_KEY=your_api_ninjas_key_here
```

---

## 🦁 Usage
Run the program from the terminal:
```sh
python main.py
```
💡 **When prompted, enter an animal name** (e.g., "Fox", "Elephant", "Tiger").

The program will generate an HTML file named `animals.html`. Open it in any web browser to view the results!

### Example Run:
```sh
$ python main.py
Enter a name of an animal: Fox
✅ Website successfully generated: animals.html
```

---

## 🔍 How It Works
1️⃣ **User inputs an animal name**  
2️⃣ `data_fetcher.py` **requests data** from API Ninjas  
3️⃣ The data is **processed and formatted** into HTML  
4️⃣ The **HTML file is saved** and ready to be viewed  

---

## ⚠️ Error Handling
🛑 **API request failure** → Displays an error message  
🛑 **Animal not found** → Website still generates with a friendly message  
🛑 **Missing/Invalid API key** → Provides clear instructions  

---

## 📦 Dependencies
- **requests** → For making API calls  
- **python-dotenv** → For loading environment variables  

Install all dependencies with:
```sh
pip install -r requirements.txt
```

---

## 🔮 Future Improvements
🚀 Search by **multiple criteria** (e.g., habitat, classification)  
🚀 **Include animal images** dynamically  
🚀 Add **pagination** for larger datasets  
🚀 Upgrade to a **full web application** with a front-end UI  

---

## 📜 Credits
🐾 **Animal data provided by API Ninjas**  
🌟 Inspired by the **original My_Zootopia project**  

📌 **Contributions & feedback are welcome!** Feel free to fork the repo and submit a pull request. 🚀