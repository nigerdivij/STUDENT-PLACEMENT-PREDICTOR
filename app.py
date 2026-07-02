import streamlit as st
import numpy as np
import joblib

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Student Placement Predictor",
    page_icon="🎓",
    layout="wide"
)

# -------------------- LOAD MODEL --------------------
model = joblib.load("model/placement_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#0f172a,#1e293b);
    color:white;
}

h1,h2,h3,h4{
    color:white;
}

.block-container{
    padding-top:2rem;
}

div[data-testid="stMetric"]{
    background:#1f2937;
    padding:15px;
    border-radius:15px;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:15px;
    background:#2563eb;
    color:white;
    font-size:20px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background:#1d4ed8;
}

[data-testid="stSidebar"]{
    background:#111827;
}

</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.title("🎓 Placement Predictor")

    st.write("---")

    st.write("""
### About

This application predicts whether a student is likely to be placed based on academic performance and skills.

**Model**
- Random Forest

**Built Using**
- Python
- Scikit-Learn
- Streamlit
""")

# -------------------- TITLE --------------------

st.title("🎓 Student Placement Predictor")

st.write("Predict whether a student is likely to get placed.")

st.write("---")

# -------------------- INPUTS --------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📚 Academic Details")

    iq = st.number_input("IQ", 50.0,200.0,100.0)

    prev_sem = st.number_input("Previous Semester Result",0.0,100.0,70.0)

    cgpa = st.number_input("CGPA",0.0,10.0,7.0)

    academic = st.number_input("Academic Performance",0.0,10.0,7.0)

with col2:

    st.subheader("💼 Skills")

    extra = st.number_input("Extra Curricular Score",0.0,10.0,5.0)

    communication = st.number_input("Communication Skills",0.0,10.0,7.0)

    projects = st.number_input("Projects Completed",0.0,20.0,2.0)

    internship = st.selectbox(
        "Internship Experience",
        ["No","Yes"]
    )

internship = 1 if internship=="Yes" else 0

st.write("")

# -------------------- BUTTON --------------------

if st.button("🚀 Predict Placement"):

    data = np.array([[

        iq,
        prev_sem,
        cgpa,
        academic,
        extra,
        communication,
        projects,
        internship

    ]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    probability = model.predict_proba(data)[0][1]

    st.write("---")

    col1,col2 = st.columns(2)

    with col1:

        if prediction[0]==1:

            st.success("🎉 Likely to be Placed")

        else:

            st.error("❌ Unlikely to be Placed")

    with col2:

        st.metric(
            "Placement Probability",
            f"{probability*100:.2f}%"
        )

    st.progress(float(probability))

    if probability>0.80:

        st.info("Excellent placement chances.")

    elif probability>0.60:

        st.warning("Good chances. Improving communication and projects can help further.")

    else:

        st.error("Placement chances are currently low. Focus on CGPA, projects, and internships.")