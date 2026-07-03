# 🎓 Student Placement Predictor

A machine learning web app that predicts whether a student is likely to be placed, based on academic performance, skills, and internship experience — with a live probability score and a clean Streamlit interface.
![Uploading InvincibleConquestGIF.gif…]()


![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🚀 Demo

🔗 **[Live App](#)** *(https://student-placement-predictor-vuww2bvzmxznsaeyhshqxd.streamlit.app/)*

---

## 📸 Screenshots

<p align="center">
  <img src="images/screenshot-form.png" alt="Input form" width="800"/>
  <br/><em>Input form — academic details and skills</em>
</p>

<p align="center">
  <img src="images/screenshot-result.png" alt="Prediction result" width="800"/>
  <br/><em>Prediction output with placement probability</em>
</p>

---

## ✨ Features

- 🎯 Predicts placement outcome (Placed / Not Placed) from student data
- 📊 Returns a probability/confidence score, not just a label
- 🖥️ Interactive, form-based Streamlit interface — no code needed to use it
- ⚙️ Trained and compared across multiple ML models
- 🎨 Clean, modern, responsive UI
- 💾 Model and scaler persisted with Joblib for fast inference

---

## 🛠 Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data | Pandas, NumPy |
| ML | Scikit-Learn |
| Web App | Streamlit |
| Model Persistence | Joblib |

---

## 📂 Project Structure

```
Student-Placement-Predictor/
├── app.py                     # Streamlit application entry point
├── README.md
├── requirements.txt
├── data/                      # Raw / processed datasets
├── images/                    # Screenshots & app assets
├── model/
│   ├── placement_model.pkl    # Trained ML model
│   └── scaler.pkl             # Fitted feature scaler
└── notebooks/                 # EDA & model training notebooks
```

---

## 📊 Machine Learning Workflow

1. **Data Cleaning** — handling missing values, duplicates, and outliers
2. **Exploratory Data Analysis** — understanding feature distributions and correlations with placement outcome
3. **Feature Engineering** — deriving/encoding relevant features (CGPA, skills, internships, etc.)
4. **Feature Scaling** — standardizing numerical features
5. **Model Training** — Logistic Regression, Decision Tree, Random Forest
6. **Model Evaluation** — accuracy, precision, recall, F1-score, confusion matrix
7. **Deployment** — best-performing model served via Streamlit

---

## ▶ Installation

```bash
# Clone the repository
git clone https://github.com/nigerdivij/STUDENT-PLACEMENT-PREDICTOR.git
cd STUDENT-PLACEMENT-PREDICTOR

# (Optional but recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 🧠 Usage

1. Launch the app with `streamlit run app.py`
2. Enter student details in the form — CGPA, skills, internships, projects, etc.
3. Click **Predict**
4. View the predicted placement outcome along with the model's confidence score

---

## 📈 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 90.24% |
| Decision Tree | 100% |
| Random Forest | 100% |

*Final model selected: **Random Forest**, saved as `model/placement_model.pkl` (with `model/scaler.pkl` for feature scaling).*

> ⚠️ Note: Decision Tree and Random Forest both hit 100% accuracy on the test split, which is a strong signal of overfitting rather than a truly perfect classifier. If you're extending this project, consider cross-validation, hyperparameter tuning (e.g. `max_depth`, `min_samples_leaf`), and checking for data leakage between train/test splits.

**Features used:** `IQ`, `Prev_Sem_Result`, `CGPA`, `Academic_Performance`, `Extra_Curricular_Score`, `Communication_Skills`, `Projects_Completed`, `Internship_Experience`

---

## 🔮 Future Improvements

- [ ] Add SHAP/feature-importance explainability to predictions
- [ ] Support batch predictions via CSV upload
- [ ] Add model comparison dashboard within the app
- [ ] Deploy with Docker for easier reproducibility
- [ ] Expand dataset with more diverse placement records

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, open an issue, or submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Divij Kulkarni**

[![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/nigerdivij)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/divij-kulkarni-7041a9402/)

---

⭐ If you found this project useful, consider giving it a star — it helps a lot!
