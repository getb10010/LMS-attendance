# 📚 LMS Auto Course Bot

A lightweight automation tool for LMS that logs in, extracts course modules, and opens them efficiently in your browser.

---

## 🎯 Purpose

This project is **only designed for LMS attendance automation**.

It helps to:

- Simplify repetitive LMS navigation
- Automatically open required course modules
- Speed up access to LMS content for attendance purposes

It does **not modify LMS data or interact with grades**.

---

## ⚙️ Features

- 🔐 Automatic LMS login
- 📚 Course selection by code
- 🔗 Scrapes all module links
- 🌐 Opens links in Chrome (5 tabs per batch)
- ⏱ Batch processing with delays for stability
- 🧹 Auto tab cleanup after each batch

---

## ⚠️ Requirements

- Python 3.9 or higher
- Google Chrome installed
- Stable internet connection

---

## 📦 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 🪟 Windows

#### 🔧 Setup

Run:

```bat
Windows - setup.bat
```

#### ▶️ Start

Run:

```bat
Windows - START.bat
```

---

### 🐧🍎 Linux / macOS

#### 🔧 Setup

```bash
chmod +x "Mac - Linux - setup.sh" "Mac - Linux - START.sh"
./Mac\ -\ Linux\ -\ setup.sh
```

#### ▶️ Start

```bash
./Mac\ -\ Linux\ -\ START.sh
```

---

## 🔑 Login

After starting the program, you will be prompted to enter:

- **Username**
- **Password**

> Login is required at the start of each session.

---

## 📚 Course Selection

Enter a course code, for example:

```
118
```

Then confirm:

```
y / n
```

---

## 🧠 How It Works

1. Logs into LMS automatically
2. Scrapes all module links from the selected course
3. Opens links in Chrome in batches of 5 tabs
4. Waits between batches for stability
5. Closes tabs after each batch

---

## ❌ Exit

To stop the program, type:

```
q
```

---

## ⚠️ Notes

- Do not close Chrome during execution
- LMS UI changes may break selectors
- Stable internet connection recommended
- Works best on the latest Chrome version

---

## 📌 Scope

| ✔️ Allowed | ❌ Not Allowed |
|---|---|
| Attendance-related LMS workflows | No data modification |
| Course module access automation | No bypassing authentication |
| Browser tab management | No unauthorized LMS actions |
