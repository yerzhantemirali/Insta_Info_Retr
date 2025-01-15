import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_prompt(keyword: str) -> str:
    """
    Automate the web browing to collect data and to return a text (prompt).

    This function takes string type account name and automates browing to collect data about the
    account to return a prompt asing about the description of the person.

    Args:
        keyword (str): The incoming account name.

    Returns:
        str: prompt containing list of followings of the account that asks for descrpition based on it.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")

    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))
    )

    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))
    )

    load_dotenv()

    insta_login = os.getenv("INSTAGRAM_LOGIN")
    insta_password = os.getenv("INSTAGRAM_PASSWORD")

    username.clear()
    username.send_keys(insta_login)

    password.clear()
    password.send_keys(insta_password)

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )

    button.click()

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "svg[aria-label='Search']")
        )
    )

    search_button.click()

    searchbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[aria-label='Search input']")
        )
    )

    searchbox.clear()

    searchbox.send_keys(keyword)

    if keyword.startswith("@"):
        keyword = keyword[1:]

    first_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[text()='{keyword}']"))
    )

    first_result.click()

    following_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '/following/')]")
        )
    )

    following_button.click()
    time.sleep(2)
    all_hrefs = []
    scrollable_div = driver.find_element(
        By.XPATH, "//div[contains(@class, 'x1ccrb07')]"
    )

    last_height = driver.execute_script(
        "return arguments[0].scrollHeight", scrollable_div
    )

    while True:
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight",
            scrollable_div,
        )

        time.sleep(2.5)

        new_height = driver.execute_script(
            "return arguments[0].scrollHeight", scrollable_div
        )
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(0.5)
    links = scrollable_div.find_elements(By.XPATH, ".//a[@href]")
    for link in links:
        href = link.get_attribute("href")
        if href not in all_hrefs:
            all_hrefs.append(href)

    driver.find_element(By.CSS_SELECTOR, "button[class='_abl-']").click()

    followers_button = driver.find_element(
        By.XPATH, "//a[contains(@href, '/followers/')]"
    )

    followers_button.click()

    time.sleep(2)

    all_hrefs_followers = []
    scrollable_div = driver.find_element(
        By.XPATH, "//div[contains(@class, 'x1ccrb07')]"
    )

    last_height = driver.execute_script(
        "return arguments[0].scrollHeight", scrollable_div
    )

    while True:
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight",
            scrollable_div,
        )

        time.sleep(2.5)

        new_height = driver.execute_script(
            "return arguments[0].scrollHeight", scrollable_div
        )
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(0.5)
    links = scrollable_div.find_elements(By.XPATH, ".//a[@href]")

    for link in links:
        href = link.get_attribute("href")
        if href not in all_hrefs_followers:
            all_hrefs_followers.append(href)

    interests = [
        element for element in all_hrefs if element not in all_hrefs_followers
    ]

    output = ""

    for i in interests:
        output += str(i[26:-1])
        output += " "

    prompt = "give description for the interests of a person who follows accounts like: "
    prompt += output

    return prompt
