#  AI-Powered Predictive Maintenance System

An **AI-driven predictive maintenance system** that analyzes vehicle sensor data to forecast potential failures and automate maintenance scheduling.  
This project combines **machine learning, automation, and data visualization** to minimize unexpected breakdowns and improve vehicle reliability.

---

##  **Problem Statement**
Frequent unexpected vehicle breakdowns occur due to the lack of timely maintenance prediction and monitoring of critical sensor data.

---

##  **Objective**
To develop an AI-powered system that predicts vehicle failures in advance and automates maintenance scheduling.

---

##  **Workflow**

1. **Data Collection** – Gather vehicle sensor data (engine temperature, vibration, mileage, brake wear).  
2. **Data Processing** – Clean and preprocess the data for training.  
3. **Model Training** – Train a Random Forest classifier to predict vehicle failure risk.  
4. **Model Deployment** – Expose the trained model through a Flask API.  
5. **Automation (n8n)** – Automate reading CSV data, calling the API, sending alerts, and logging results.  
6. **Visualization & Reporting** – Display predictions and logs in Google Sheets or dashboards.  
7. **Maintenance Scheduling** – Automatically alert users or schedule servicing for at-risk vehicles.

---

##  **Tech Stack**

### **Machine Learning & Data**
- Python  
- Pandas  
- Scikit-learn  
- Joblib  

### **Backend**
- Flask  

### **Automation**
- n8n (for API calls, scheduling, email/Telegram alerts)  

### **Visualization**
- Google Sheets / CSV Reports  
- Google Calendar for maintenance scheduling  

### **Development**
- VS Code / Cursor  
- GitHub for version control  
- macOS Terminal (zsh)

---

## 🧰 **Project Structure**

AI AUTOMATION/
│
├── app/
│ └── api.py # Flask API for predictions
│
├── data/
│ └── vehicle_data.csv # Dataset for model training
│
├── models/
│ └── predictive_model.pkl # Trained ML model
│
├── scripts/
│ └── train_model.py # Script for model training
│
├── n8n_workflow/ # (Optional) Exported n8n workflow JSON
│
└── README.md

