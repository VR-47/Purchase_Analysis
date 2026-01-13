# 🏭 BHEL Purchase & Procurement Analysis  
### *(PSU Case Study)*

---

## 📌 Overview

This project presents an **end-to-end procurement and purchase analysis** for a **BHEL-like Public Sector Undertaking (PSU)**.  
It is designed to closely mirror **real ERP-based procurement systems** used in PSUs and focuses on generating  
**management-level insights** rather than only technical outputs.

---

## 🎯 Project Objectives

- Simulate a realistic **PSU procurement workflow**
- Design an **ERP-style normalized database**
- Use **SQL** for data ingestion and joins
- Perform **Python-based data analysis and visualization**
- Derive **actionable insights for management decision-making**

---

## 🧠 Business Context

In PSUs such as **BHEL**, procurement follows a strict hierarchical approval flow:

Section → Department → Division → Plant → Vendor → Purchase Order → Payment


- Sections raise purchase demands  
- Higher levels ensure approval and control  
- Vendors supply materials  
- Payments are processed after successful delivery  

This structured flow ensures:
- Accountability  
- Budget control  
- Audit and compliance readiness  

---

## 🗂 Dataset Design

The database is modeled using an **ERP-style normalized schema**.

### 🔹 Master Tables
- `plant_master`
- `division_master`
- `department_master`
- `section_master`
- `vendor_master`
- `material_master`

### 🔹 Transaction Tables
- `purchase_orders`
- `purchase_payments`

### 📌 Why Normalization?
- Avoids data redundancy  
- Maintains data consistency  
- Reflects real-world enterprise ERP systems  

> For analysis, all tables are joined during ingestion to form a **single analytical dataset**.

---

## ⚙️ Tech Stack

| Layer          | Technology        |
|---------------|------------------|
| Database       | MySQL            |
| Language       | Python           |
| Analysis       | pandas           |
| Visualization  | matplotlib       |
| Environment    | Jupyter Notebook |

---

## 🔄 Project Workflow

### 1️⃣ Data Generation
- Realistic **PSU-style procurement data**

### 2️⃣ Data Storage
- Normalized tables stored in **MySQL**

### 3️⃣ Data Ingestion
- SQL joins handled via a **separate Python script**
- Final output returned as a **single pandas DataFrame**

### 4️⃣ Data Validation
- Missing value checks  
- Consistency validation  

### 5️⃣ Feature Engineering
- Time-based attributes (Year, Month)

### 6️⃣ Exploratory Data Analysis (EDA)
- Procurement spend analysis  
- Vendor dependency analysis  
- Delivery delays  
- Payment delays  
- Priority misuse  

### 7️⃣ KPI & Insight Generation
- Management-focused metrics  
- Business recommendations  

---

## 📊 Key Analyses Performed

- Procurement spend by plant  
- Top vendor dependency analysis  
- Vendor delivery performance  
- Payment delay assessment  
- Priority order usage evaluation  

Each analysis follows a structured approach:

> **Business Question → Analysis → Visualization → Interpretation**

---

## 📈 Key Insights

- Procurement spend is concentrated among **limited plants and vendors**
- Certain vendors show **consistent delivery delays**
- Payment delays may negatively impact **vendor relationships**
- High-priority orders indicate **planning inefficiencies**

---

## 🧩 Management Recommendations

- Diversify vendor base to reduce dependency risk  
- Enforce SLA compliance for delayed vendors  
- Improve demand forecasting and planning  
- Streamline payment approval processes  

---

## 📁 Repository Structure
├── data
├── db_ingestion.py # SQL joins and data loading
├── Purchase_Analysis.ipynb # Main analysis notebook
├── README.md


---

## ⚠️ Assumptions & Limitations

- Dataset is **simulated**, but designed based on real PSU workflows  
- Vendor behavior assumed consistent over time  
- Focus is on **operational insights**, not legal or regulatory compliance  

---

## 🚀 Future Enhancements

- Vendor performance scoring system  
- Predictive delay analysis  
- Inventory and production data integration  
- Interactive dashboards (Power BI / Tableau)

---

## 👤 Author

**Vanshika Rana**  
B.Tech – Computer Science  
Procurement & Data Analytics Project  

---

## ⭐ Why This Project is Valuable

This project demonstrates:

- Strong understanding of **PSU procurement systems**
- Effective integration of **SQL + Python**
- Emphasis on **business insights and decision-making**
- Industry-aligned **data modeling and analysis**
