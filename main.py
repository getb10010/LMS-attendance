import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =========================
# COURSES MAP
# =========================
courses = {
    "130": "calculus",
    "112": "kazakh language",
    "131": "Freshmen Capstone project",
    "129": "Introduction to Database",
    "140": "Linear Algebra",
    "139": "Moral Ethic and Social Responsibility",
    "118": "Python I"
}


# =========================
# INPUT LOGIN
# =========================
USERNAME = input("Login: ")
PASSWORD = input("Password: ")


# =========================
# SELECT COURSE (SAFE LOOP)
# =========================
while True:
    print("\nAvailable courses:\n")

    for k, v in courses.items():
        print(f"{k} - {v}")

    COURSE_ID = input("\nEnter course code (or 'exit'): ").strip()

    if COURSE_ID.lower() == "exit":
        print("Exiting...")
        exit()

    if COURSE_ID not in courses:
        print("❌ Invalid course code, try again.")
        continue

    # confirmation
    print(f"\nYou selected: {COURSE_ID} - {courses[COURSE_ID]}")
    confirm = input("Confirm? (y/n): ").strip().lower()

    if confirm == "y":
        break
    else:
        print("Selection cancelled, try again...")


course_url = f"https://lms.wsuk.edu.kz/courses/{COURSE_ID}"


# =========================
# 1. REQUESTS SCRAP LINKS
# =========================
session = requests.Session()

login_page = session.get("https://lms.wsuk.edu.kz/login")

soup = BeautifulSoup(login_page.text, "html.parser")
token_input = soup.find("input", {"name": "authenticity_token"})
token = token_input["value"] if token_input else ""

login_data = {
    "pseudonym_session[unique_id]": USERNAME,
    "pseudonym_session[password]": PASSWORD,
    "authenticity_token": token
}

session.post("https://lms.wsuk.edu.kz/login/canvas", data=login_data)

r = session.get(course_url)

soup = BeautifulSoup(r.text, "html.parser")
base = "https://lms.wsuk.edu.kz"

links = []

for a in soup.find_all("a"):
    href = a.get("href")
    text = a.text.strip()

    if href and "modules/items/" in href and "{{" not in href:
        links.append((text, base + href))

print(f"\nTotal links: {len(links)}")


# =========================
# 2. SELENIUM LOGIN
# =========================
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.get("https://lms.wsuk.edu.kz/login")

user = wait.until(EC.presence_of_element_located(
    (By.NAME, "pseudonym_session[unique_id]")
))

password = wait.until(EC.presence_of_element_located(
    (By.NAME, "pseudonym_session[password]")
))

user.send_keys(USERNAME)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

print("\nLogging in...")
time.sleep(5)


# =========================
# OPEN COURSE
# =========================
driver.get(course_url)
time.sleep(3)


# =========================
# OPEN LINKS IN BATCHES
# =========================
batch_size = 5
main_window = driver.current_window_handle

for i in range(0, len(links), batch_size):
    batch = links[i:i + batch_size]

    for text, url in batch:
        print("Opening:", text)
        driver.execute_script(f"window.open('{url}', '_blank');")

    time.sleep(3)

    print("Batch done → sleeping 10 sec...\n")
    time.sleep(10)

    # close only extra tabs
    for tab in driver.window_handles:
        if tab != main_window:
            driver.switch_to.window(tab)
            driver.close()

    driver.switch_to.window(main_window)

print("\nDONE")