# 🏥 Smart Healthcare Management System

> An AI-powered Flask web application for early-stage disease prediction and holistic health guidance.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Tech Stack](#tech-stack)
5. [Getting Started](#getting-started)
6. [Training the Model](#training-the-model)
7. [Running the App](#running-the-app)
8. [Dataset Guide](#dataset-guide)
9. [Architecture](#architecture)
10. [Disclaimer](#disclaimer)

---

## Overview

The Smart Healthcare Management System lets users enter symptoms through an interactive UI and receive an instant, comprehensive health report powered by a **Support Vector Classifier (SVC)** trained on a curated dataset of **41 diseases** and **132 symptoms**.

The report includes:

- Predicted disease name and confidence score
- Plain-language disease description
- Precautionary measures
- Common medications
- Recommended diet plan
- Workout suggestions

---

## Features

| Feature                | Description                                    |
| ---------------------- | ---------------------------------------------- |
| Symptom chip selector  | Search + click-to-select UI with live counter  |
| SVC prediction         | Multi-class classifier with probability output |
| Full health report     | 5 auxiliary datasets merged per prediction     |
| Health blog            | Educational articles section                   |
| Developer profile      | Showcase page                                  |
| Print-friendly report  | CSS print styles included                      |
| Blueprint architecture | Modular Flask routes                           |

---

## Project Structure

```
healthcare_system/
├── app.py                    # Application factory & entry point
├── config.py                 # Configuration classes (Dev / Prod / Test)
├── requirements.txt
├── .env.example
├── .gitignore
│
├── routes/
│   ├── __init__.py
│   ├── main_routes.py        # Home, About, Developer, Contact
│   ├── prediction_routes.py  # Symptom input & result
│   └── blog_routes.py        # Blog list & detail
│
├── utils/
│   ├── __init__.py
│   ├── prediction_service.py # ML inference + dataset lookups
│   ├── validators.py         # Input validation helpers
│   └── logger.py             # Centralised logging setup
│
├── models/
│   ├── __init__.py
│   ├── model_trainer.py      # Train & serialise the SVC model
│   ├── svc_model.pkl         # (generated — git-ignored)
│   └── label_encoder.pkl     # (generated — git-ignored)
│
├── data/
│   ├── Training.csv          # Symptom-disease training data
│   ├── symtoms_df.csv
│   ├── precautions_df.csv
│   ├── medications.csv
│   ├── diets.csv
│   ├── workout_df.csv
│   └── description.csv
│
├── templates/
│   ├── base.html             # Master layout (navbar + footer)
│   ├── index.html            # Landing page
│   ├── symptom_input.html    # Symptom checker form
│   ├── result.html           # Health report
│   ├── about.html
│   ├── developer.html
│   ├── blog_list.html
│   ├── blog_detail.html
│   └── contact.html
│
└── static/
    ├── css/
    │   ├── main.css           # Global design tokens + shared styles
    │   ├── symptom_input.css  # Chip selector styles
    │   └── result.css         # Report card styles
    └── js/
        ├── main.js            # Navbar scroll, global utilities
        └── symptom_input.js   # Chip interaction logic
```

---

## Tech Stack

| Layer             | Technology                   |
| ----------------- | ---------------------------- |
| Language          | Python 3.11                  |
| Web Framework     | Flask 3.0                    |
| ML Library        | Scikit-learn (SVC)           |
| Data Processing   | Pandas, NumPy                |
| Model Persistence | joblib                       |
| Frontend          | Bootstrap 5, Bootstrap Icons |
| Fonts             | DM Serif Display + DM Sans   |

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/healthcare-system.git
cd healthcare-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

```bash
cp .env.example .env
# Edit .env and set a strong SECRET_KEY
```

### 5. Add your datasets

Place the following CSV files in the `data/` directory:

- `Training.csv`
- `symtoms_df.csv`
- `precautions_df.csv`
- `medications.csv`
- `diets.csv`
- `workout_df.csv`
- `description.csv`

---

## Training the Model

Run this **once** (or whenever the dataset changes):

```bash
python models/model_trainer.py
```

This will:

1. Load and preprocess `data/Training.csv`
2. Train an SVC with RBF kernel
3. Print accuracy and cross-validation scores
4. Save `models/svc_model.pkl` and `models/label_encoder.pkl`

---

## Running the App

### Development

```bash
flask run
# or
python app.py
```

Open http://localhost:5000

### Production (Gunicorn)

```bash
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
```

---

## Dataset Guide

| File                 | Required Columns                           |
| -------------------- | ------------------------------------------ |
| `Training.csv`       | symptom columns + `prognosis`              |
| `description.csv`    | `Disease`, `Description`                   |
| `precautions_df.csv` | `Disease`, `Precaution_1` … `Precaution_4` |
| `medications.csv`    | `Disease`, `Medication_1` …                |
| `diets.csv`          | `Disease`, `Diet_1` …                      |
| `workout_df.csv`     | `Disease`, `workout`                       |

---

## Architecture

```
User Browser
    │
    ▼
Flask Routes (Blueprints)
    │
    ├── main_routes.py      → Static pages
    ├── prediction_routes.py → POST /predict/result
    │       │
    │       ▼
    │   validators.py       → Validate + sanitise input
    │       │
    │       ▼
    │   prediction_service.py → Feature vector → SVC → HealthReport
    │       │
    │       ├── svc_model.pkl
    │       ├── label_encoder.pkl
    │       └── CSV datasets (description, precautions, meds, diet, workout)
    │
    └── blog_routes.py      → Blog pages
```

---

## Disclaimer

> This system is developed for **educational and research purposes** as part of a B.Tech final-year project.  
> It is **not** a certified medical device and should **not** replace the advice of a qualified healthcare professional.  
> Always consult a licensed physician for clinical diagnosis and treatment.
