# **Person's Interest Detector from Instagram Account**

## **Project Overview**
This project aims to analyze a person's interests based on the Instagram accounts they follow. By providing a publicly accessible Instagram username, the project retrieves the list of accounts followed by the target user, processes this data using a locally hosted LLM (Llama:8B), and generates a detailed description of their potential interests.

### **Features**
- Automates Instagram scraping using Selenium.
- Generates personalized interest descriptions using Llama:8B LLM.
- Displays results on a dynamic web interface powered by FastAPI and Jinja2.

---


## **Example Usage**
**Screenshots of the working project:**

**Web Page to Input Instagram Username**  
![alt text](<markdown/Screenshot 2025-01-05 at 7.55.30 PM.png>)

**Generated Interest Description**  
![alt text](<markdown/Screenshot 2025-01-05 at 7.55.55 PM.png>)

---

## **Setup and Usage**

### **1. Clone the Repository**
```bash
git clone https://github.com/yerzhantemirali/Insta_Info_Retr.git
cd Insta_Info_Retr
```

### **2. Create and Activate a Poetry Environment with Dependency Installation**
- Install and initialize the package manager
```
pip install poetry
poetry init
```

- To install dependencies in the virtual environment replace ‘dependencies = [ ]’ in 'pyproject.toml' file with:
```
[tool.poetry.dependencies]
python = ">=3.12,<4.0"
selenium = "*"
requests = "*"
beautifulsoup4 = "*"
pandas = "*"
openai = "*"
fastapi = "*"
uvicorn = "*"
langchain = "*"
langchain-ollama = "*"
ollama = "*"
jinja2 = "*"
python-dotenv = "*"
python-multipart = "*"
```

- To save a virtual environment in your project folder and to install dependencies in there type: 
```
poetry config virtualenvs.in-project true
poetry install
```

- To activate the virtual environment get the path by:
```
poetry env info --path
```

If you have Mac or Linux OS follow with:
```
source <put_the_path_here>/bin/activate
```

If you have windows:
```
<put_the_path_here>\Scripts\activate
```


### **3. Set Up Your Local LLM**
- Download a suitable LLM from [Ollama](https://ollama.ai) (you should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models).

- Replace "Llama3:8b" in the local_llama.py file with the name of the model you downloaded:
```
model = OllamaLLM(model="Your_Model_Name_Here")
```
- Run the follwoing command in you terminal:
```
ollama run <put_LLM_name_you_downloaded>
```

### **4. Configure Instagram Login Credentials**
- Change the name of the file “.env.example” to just “.env” and put your Instagram login credentials:
``` 
INSTAGRAM_LOGIN=yourinstagramlogin
INSTAGRAM_PASSWORD=yourinstagrampassword
```

### **5. Run the Application**
In your terminal, execute the following command to start the server:
```
uvicorn src.main:app --reload
``` 
Access the web app at http://127.0.0.1:8000.

---

## **Future Plans**

- Dataset Creation: Scrape Instagram and Twitter to build a dataset of account names and their descriptions.

- Fine-Tuning LLM: Use the dataset to fine-tune the local LLM for more accurate and personalized descriptions.

---

## **Contacts**
Feel free to reach out for any questions or feedback about the project:
Email: yerzhantemirali@gmail.com