# 📚 LMS Auto Course Bot

This bot:
- logs into LMS automatically
- lets you choose a course
- collects all module links
- opens them in browser tabs (5 at a time)

---

## ⚠️ Requirements

- Python 3.9+
- Google Chrome installed
- Internet connection

---

## 📦 Install dependencies

Run:

pip install -r requirements.txt

---

## 🚀 Run

python main.py

---

## 🔑 Login

Login and password will be asked after start.

---

## 📚 Course selection

Enter course code like:

118

Then confirm with:
y / n

---

## 🧠 What it does

- Scrapes course links
- Opens them in Chrome
- 5 tabs at a time
- waits 10 seconds
- closes tabs

---

## ❌ Exit

Type:
exit

---

## ⚠️ Notes

- Do not close Chrome during execution
- LMS UI changes may break selectors
