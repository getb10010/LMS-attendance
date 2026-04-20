📚 LMS Auto Course Bot

A lightweight automation tool for LMS that logs in, extracts course modules, and opens them efficiently in your browser.

🎯 Purpose

This project is only designed for LMS attendance automation.

It helps to:

simplify repetitive LMS navigation
automatically open required course modules
speed up access to LMS content for attendance purposes

It does not modify LMS data or interact with grades.

⚙️ Features
🔐 Automatic LMS login
📚 Course selection by code
🔗 Scrapes all module links
🌐 Opens links in Chrome (5 tabs per batch)
⏱ Batch processing with delays for stability
🧹 Auto tab cleanup after each batch
⚠️ Requirements
Python 3.9 or higher
Google Chrome installed
Stable internet connection
📦 Installation

Install dependencies:

pip install -r requirements.txt
🚀 How to Run
🪟 Windows
🔧 Setup
setup.bat
▶️ Start
start.bat
🐧🍎 Linux / macOS
🔧 Setup
chmod +x setup.sh start.sh
./setup.sh
▶️ Start
./start.sh
🔑 Login

After starting the program, you will be prompted to enter:

Username
Password

Login is required at the start of each session.

📚 Course Selection

Enter a course code, for example:

118

Then confirm:

y / n
🧠 How It Works
Logs into LMS automatically
Scrapes all module links from the selected course
Opens links in Chrome in batches of 5 tabs
Waits between batches for stability
Closes tabs after each batch
❌ Exit

To stop the program, type:

q
⚠️ Notes
Do not close Chrome during execution
LMS UI changes may break selectors
Stable internet connection recommended
Works best on latest Chrome version
📌 Scope

✔ Attendance-related LMS workflows
✔ Course module access automation
✔ Browser tab management

❌ No data modification
❌ No bypassing authentication
❌ No unauthorized LMS actions

If you want next upgrade, I can make your repo look insanely professional with:

🔥 GitHub badges (Python, Selenium, etc.)
📸 screenshots section
🎬 GIF demo
🚀 “1-click installer” version
🧠 fully automated workflow mode