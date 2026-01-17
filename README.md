# SmartHR AI  
## AI-Powered Human Resource Management System  

---

# How to Run the SmartHR-AI Project (Step-by-Step Guide)

## 1️⃣ Download and Extract the Project
- Download **SmartHR-AI-main** (ZIP file)
- Extract / unzip it to your desired location
- Open the extracted folder in **VS Code** (optional)

## 2️⃣ Important Note ⚠️
- Do **NOT** use the VS Code terminal, because it defaults to **PowerShell**
- ✅ Use **Command Prompt (CMD)** for running commands

## 3️⃣ Set Up and Activate Virtual Environment
- Open **CMD**
- Go to the folder where your `venv` exists
- Activate the virtual environment:
- venv\Scripts\activate

## 4️⃣ Navigate to the Django Project Folder
- Move inside the Django project directory:

- cd ems_main

## 5️⃣ Install Required Dependencies
- Install all required Python packages:

- pip install -r requirements.txt

## 6️⃣ Run the Django Development Server
- Start the project server:

- python manage.py runserver
## 7️⃣ Open the Project in Browser 🌐
- Open this URL in your browser:

- http://127.0.0.1:8000/
✅ Your SmartHR AI project should now be running successfully.

## 🔹 Overview  
- SmartHR AI is a web-based HR Management System enhanced with Artificial Intelligence  
- Automates employee management, resume screening, interview preparation, and HR support  
- Designed to reduce manual workload, improve hiring efficiency, and enable intelligent decision-making  

---

## 📌 Problem Overview  
- HR teams rely on manual or semi-automated processes  
- Managing employee data is time-consuming and error-prone  
- Resume screening involves hundreds or thousands of profiles  
- Repetitive HR queries reduce productivity and efficiency  
- Lack of intelligent automation delays hiring decisions  

✅ SmartHR AI solves these challenges through a centralized, AI-driven HR platform  

---

## 🚀 Key Features  

### ➤ Employee Management System  
- Add, view, filter, and delete employee records  
- Centralized and structured employee data management  

### ➤ AI Resume Ranker  
- Upload 10–15 resumes simultaneously  
- Automatically ranks resumes based on job description relevance  
- Reduces manual screening of hundreds of resumes  

### ➤ HR Assistant Chatbot  
- AI-powered chatbot using Groq API  
- Answers HR-related queries instantly  
- Suggests role-specific interview questions  

### ➤ Interview Assistance  
- Helps HR prepare consistent and relevant interview questions  
- Reduces dependency on manual preparation  

### ➤ Secure & Scalable Backend  
- Environment-based API key management  
- Modular, maintainable, and scalable architecture  

---

## 🛠 Technology Stack  
- Python – Core backend logic  
- Django – Web framework for application development  
- Django REST Framework (DRF) – API layer for AI services  
- HTML – Frontend structure  
- Bootstrap – Responsive UI design  
- Groq API – AI chatbot & language model integration  
- SQLite – Lightweight database for development  
- Git & GitHub – Version control and collaboration  
