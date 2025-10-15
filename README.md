# 🧠 Quizzler App

**Quizzler** is a simple quiz application built with **Python 3.12**.  
Each time you run the app, it randomly selects **10 questions** from a random category.  
Each question has **two possible answers: True or False**.

---

## 🎯 How It Works

- When the app starts, it fetches 10 random questions from the [Open Trivia Database API](https://opentdb.com/).
- Each correct answer increases your **score by 1**.
- After answering all 10 questions, the app displays a message showing **how many questions you got right**.

---

## 🧩 Technologies Used

- **Python 3.12**
- **Requests 2.32.5**
- **Open Trivia Database API**

---

## 🚀 Features

- Random question selection each run  
- Simple True/False interface  
- Automatic scoring system  
- Displays final result after completion  

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/SonDA-22011995/quizzler.git
   cd quizzler

2. Install dependencies:
    ```bash
    pip install requests==2.32.5
3. Run the app:
    ```bash
    python main.py
