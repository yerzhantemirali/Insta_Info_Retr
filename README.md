# Description of person's interest based on their instagram account

## Intro to the project
The project scrapes some person's instagram account provided by user and sends a prompt containing list of the following accounts to a local LLM to get a description about the person's interests.

## Project description
This project has a web page that asks user to input the publicly available instagram account of a perso whose interests they want to find out. This project uses selenium library to automate web browsing: specifically to log into your instagram account, search for the provided account and scrape the list of the accounts the person follows. And then this list is included in the prompt that is sent to local LLM (Llama:8b) about the possible interests of the person. The output of the LLM is then appears in the other html web page. To deal with APIs, FastAP and uvicorn were utilized. Jinja2Templates were used for templating of dynamic html pages.



## Demonstration of the project
![alt text](<markdown/Screenshot 2025-01-05 at 7.55.30 PM.png>)
![alt text](<markdown/Screenshot 2025-01-05 at 7.55.55 PM.png>)
## Steps for recreating and running this project: 
1) clone this repository
```
git clone https://github.com/yerzhantemirali/Insta_Info_Retr.git
```
2) create conda environment 
```
conda create -n insta_project python=3.8 -y
```
 ```
 conda activate insta_project
 ```
 3) install the requirements
 pip install -r requirements.txt

 4) download ollama model that you can run locally and in local_llama.py file replace "Llama3:8b" with the name of the model you downloaded:
 ```
 model = OllamaLLM(model="Llama3:8b")
 ```

5) in scraper.py file
``` 
username.send_keys('your_insta_login_here')
password.send_keys("your_insta_password_here")
```
put your instagram login and password

6) write the following in the terminal of your IDE:
```
uvicorn src.main:app --reload
``` 



## To do
Soon I am planning to create a dataset with different accounts names and with what they are all about by scraping twitter and instagram to fine tune the local LLM I am using so that the descriptions will be more accurate.


## Contacts 
If you have any questions about the project feel free to email me 
Gmail: yerzhantemirali@gmail.com
