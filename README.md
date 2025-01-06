# **Person's Interest Detector from Instagram Account**

## **Project Overview**
This project aims to analyze a person's interests based on the Instagram accounts they follow. By providing a publicly accessible Instagram username, the project retrieves the list of accounts followed by the target user, processes this data using a locally hosted LLM (Llama:8B), and generates a detailed description of their potential interests.

### **Features**
- Automates Instagram scraping using Selenium.
- Generates personalized interest descriptions using Llama:8B LLM.
- Displays results on a dynamic web interface powered by FastAPI and Jinja2.

---


## **Demonstration**
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

### **2. Create and Activate a Conda Environment**
```
conda create -n insta_project python=3.8 -y
conda activate insta_project
```

### **3. Install Dependencies**
```
pip install -r requirements.txt
```

### **4. Set Up Your Local LLM**
- Download a suitable LLM from [Ollama](https://ollama.ai).

- Replace "Llama3:8b" in the local_llama.py file with the name of the model you downloaded:
```
model = OllamaLLM(model="Your_Model_Name_Here")
```

### **5. Configure Instagram Login Credentials**
- Open scraper.py and replace the placeholders with your Instagram login credentials:
``` 
username.send_keys('your_insta_login_here')
password.send_keys("your_insta_password_here")
```

### **6. Run the Application**
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