import time
import requests
import sys
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


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
# LOGIN ONCE (IMPORTANT CHANGE)
# =========================
USERNAME = input("Login (or q): ").strip()
if USERNAME.lower() == "q":
    exit()

PASSWORD = input("Password: ").strip()


# =========================
# MAIN LOOP
# =========================
while True:
    print("\n============================")
    print("1 - LMS (wsuk)")
    print("2 - DLMS (wsi)")
    print("q - Quit")
    print("============================")

    system_choice = input("Choose system: ").strip().lower()

    if system_choice == "q":
        print("Exiting program...")
        break

    if system_choice == "1":
        BASE_URL = "https://lms.wsuk.edu.kz"
    elif system_choice == "2":
        BASE_URL = "https://dlms.wsi.ac.kr"
    else:
        print("❌ Invalid option")
        continue

    session_start_time = time.time()

    # =========================
    # COURSE SELECTION LOOP
    # =========================
    while True:
        print("\nAvailable courses:\n")
        for k, v in courses.items():
            print(f"{k} - {v}")

        COURSE_ID = input("\nEnter course code (or q): ").strip()

        if COURSE_ID.lower() == "q":
            break

        if COURSE_ID not in courses:
            print("❌ Invalid course code")
            continue

        print(f"\nSelected: {courses[COURSE_ID]}")
        confirm = input("Confirm? (y/n): ").strip().lower()

        if confirm == "y":
            break

    if COURSE_ID.lower() == "q":
        continue

    course_url = f"{BASE_URL}/courses/{COURSE_ID}"

    # =========================
    # REQUESTS LOGIN + SCRAPE
    # =========================
    try:
        session = requests.Session()

        login_page = session.get(f"{BASE_URL}/login")
        soup = BeautifulSoup(login_page.text, "html.parser")

        token_input = soup.find("input", {"name": "authenticity_token"})
        token = token_input["value"] if token_input else ""

        login_data = {
            "pseudonym_session[unique_id]": USERNAME,
            "pseudonym_session[password]": PASSWORD,
            "authenticity_token": token
        }

        session.post(f"{BASE_URL}/login/canvas", data=login_data)

        r = session.get(course_url)
        soup = BeautifulSoup(r.text, "html.parser")

        links = []
        for a in soup.find_all("a"):
            href = a.get("href")
            text = a.text.strip()

            if href and "modules/items/" in href and "{{" not in href:
                links.append((text, BASE_URL + href))

        print(f"\nTotal links found: {len(links)}")

    except Exception as e:
        print("❌ Request error:", e)
        continue

    # =========================
    # SELENIUM LOGIN
    # =========================
    try:
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")

        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_setting_values.notifications": 2
        }
        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(300)
        driver.set_script_timeout(300)
        driver.set_window_size(800, 600)

        wait = WebDriverWait(driver, 20)

        driver.get(f"{BASE_URL}/login")

        user = wait.until(EC.presence_of_element_located(
            (By.NAME, "pseudonym_session[unique_id]")
        ))
        password_field = wait.until(EC.presence_of_element_located(
            (By.NAME, "pseudonym_session[password]")
        ))

        user.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)

        print("Logging in...")
        time.sleep(5)

        driver.get(course_url)
        time.sleep(3)

        # =========================
        # PROGRESS SETTINGS
        # =========================
        total_links = len(links)
        opened_count = 0
        start_time = time.time()

        # =========================
        # OPEN LINKS
        # =========================
        batch_size = 5
        main_window = driver.current_window_handle

        for i in range(0, len(links), batch_size):
            batch = links[i:i + batch_size]

            for text, url in batch:
                opened_count += 1

                elapsed = int(time.time() - start_time)
                minutes = elapsed // 60
                seconds = elapsed % 60

                print(f"[{opened_count}/{total_links}] | {minutes}m {seconds}s | {text}")

                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(url)

                time.sleep(0.5)

            print("Batch done → sleeping...\n")
            time.sleep(5)

            for tab in driver.window_handles:
                if tab != main_window:
                    driver.switch_to.window(tab)
                    driver.close()

            driver.switch_to.window(main_window)

        print("\n✅ DONE SESSION")

        session_end_time = time.time()
        elapsed = int(session_end_time - session_start_time)

        minutes = elapsed // 60
        seconds = elapsed % 60
        print(f"\nSorry for spending your {minutes} min, {seconds} sec")
        driver.quit()

    except Exception as e:
        print("❌ Selenium error:", e)
        continue

    again = input("\nRun again? (Enter = yes / q = quit): ").strip().lower()
    if again == "q":
        print("Goodbye 👋")
        break
