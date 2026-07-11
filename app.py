import streamlit as st
import joblib
import numpy as np
from datetime import date

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Flood Risk Prediction System",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------

model = joblib.load("best_flood_model.pkl")

# ---------------- CSS ----------------

st.markdown("""
<style>

.main{
    background:#F4F8FC;
}

h1{
    color:#0B3D91;
    text-align:center;
}

h2,h3{
    color:#0B3D91;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:10px;
    background:#0B3D91;
    color:white;
    font-size:18px;
    font-weight:bold;
}

.card{
background:white;
padding:20px;
border-radius:12px;
box-shadow:0px 3px 10px rgba(0,0,0,0.15);
margin-bottom:15px;
}

.footer{
text-align:center;
color:gray;
font-size:15px;
padding:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🛰️ Dashboard")

st.sidebar.markdown("---")

st.sidebar.subheader("Project")

st.sidebar.write("Flood Risk Prediction System")

st.sidebar.subheader("Model")

st.sidebar.success("Linear Regression")

st.sidebar.subheader("Dataset")

st.sidebar.info("""
Records : 1,117,957

Features : 20

Target : Flood Probability
""")

st.sidebar.subheader("Performance")

st.sidebar.write("R² : **0.8449**")

st.sidebar.write("MAE : **0.0158**")

st.sidebar.write("RMSE : **0.0201**")

st.sidebar.markdown("---")

st.sidebar.success("Developed by\n\nGahana Khandelwal")

# ---------------- HEADER ----------------

st.title(" FLOOD RISK PREDICTION SYSTEM")

st.markdown("""
<div style="background:linear-gradient(90deg,#0B3D91,#1565C0);
padding:25px;
border-radius:12px;
color:white;
text-align:center;">

<h2> Disaster Monitoring Dashboard</h2>

<p>Machine Learning Based Flood Probability Prediction</p>

</div>
""", unsafe_allow_html=True)

# STATUS CARDS

c1,c2,c3=st.columns(3)

c1.success("✔ Dataset Loaded")

c2.success("✔ Model Loaded")

c3.success("✔ Prediction Ready")

st.markdown("---")

st.subheader("Environmental Parameters")

# ---------------- INPUT PARAMETERS ----------------

left, right = st.columns(2)

with left:

    monsoon = st.slider(
        "🌧️ Monsoon Intensity",
        0,10,5,
        help="Higher rainfall increases flood probability."
    )

    topography = st.slider(
        "🏔️ Topography Drainage",
        0,10,5,
        help="Better drainage lowers flood risk."
    )

    river = st.slider(
        "🌊 River Management",
        0,10,5,
        help="Quality of river maintenance."
    )

    deforestation = st.slider(
        "🌳 Deforestation",
        0,10,5,
        help="More deforestation increases runoff."
    )

    urbanization = st.slider(
        "🏙️ Urbanization",
        0,10,5,
        help="Urban areas generally have higher flood risk."
    )

    climate = st.slider(
        "🌍 Climate Change",
        0,10,5,
        help="Represents climate change impact."
    )

    dams = st.slider(
        "🏞️ Dams Quality",
        0,10,5,
        help="Higher value = better dam quality."
    )

    siltation = st.slider(
        "🪨 Siltation",
        0,10,5,
        help="Sediment buildup in rivers."
    )

    agriculture = st.slider(
        "🌾 Agricultural Practices",
        0,10,5,
        help="Influence of farming practices."
    )

    encroachments = st.slider(
        "🏠 Encroachments",
        0,10,5,
        help="Construction on flood plains."
    )

with right:

    disaster = st.slider(
        "🚨 Disaster Preparedness",
        0,10,5,
        help="Preparedness of disaster management."
    )

    drainage = st.slider(
        "🚰 Drainage Systems",
        0,10,5,
        help="Efficiency of drainage."
    )

    coastal = st.slider(
        "🌊 Coastal Vulnerability",
        0,10,5,
        help="Flood vulnerability in coastal areas."
    )

    landslides = st.slider(
        "⛰️ Landslides",
        0,10,5,
        help="Chance of landslides."
    )

    watersheds = st.slider(
        "💧 Watersheds",
        0,10,5,
        help="Watershed management quality."
    )

    infrastructure = st.slider(
        "🏗️ Infrastructure",
        0,10,5,
        help="Condition of public infrastructure."
    )

    population = st.slider(
        "👥 Population Score",
        0,10,5,
        help="Population density indicator."
    )

    wetland = st.slider(
        "🪷 Wetland Loss",
        0,10,5,
        help="Loss of natural wetlands."
    )

    planning = st.slider(
        "📋 Inadequate Planning",
        0,10,5,
        help="Urban planning effectiveness."
    )

    political = st.slider(
        "🏛️ Political Factors",
        0,10,5,
        help="Government policy effectiveness."
    )

st.markdown("")

predict = st.button(
    " Predict Flood Probability"
)

# ---------------- PREDICTION ----------------

if predict:

    features = np.array([[
        monsoon,
        topography,
        river,
        deforestation,
        urbanization,
        climate,
        dams,
        siltation,
        agriculture,
        encroachments,
        disaster,
        drainage,
        coastal,
        landslides,
        watersheds,
        infrastructure,
        population,
        wetland,
        planning,
        political
    ]])

    prediction = model.predict(features)[0]

    st.markdown("---")

    st.header("📊 Flood Risk Assessment Dashboard")

    # ---------------- KPI CARDS ----------------

    c1, c2, c3 = st.columns(3)

    c1.metric(
        " Flood Probability",
        f"{prediction:.3f}"
    )

    c2.metric(
        " Risk %",
        f"{prediction*100:.1f}%"
    )

    c3.metric(
        " ML Model",
        "Linear Regression"
    )

    st.markdown("---")

    # ---------------- PROGRESS ----------------

    st.subheader("Flood Probability")

    st.progress(float(prediction))

    st.write(
        f"### Predicted Flood Probability : **{prediction*100:.1f}%**"
    )

    st.markdown("---")

    # ---------------- RISK LEVEL ----------------

    st.subheader("Risk Status")

    if prediction < 0.35:

        st.success("🟢 LOW FLOOD RISK")

        st.info("""
✔ Continue monitoring weather

✔ Maintain drainage systems

✔ Preserve wetlands

✔ Regular inspection of rivers
""")

    elif prediction < 0.65:

        st.warning("🟡 MODERATE FLOOD RISK")

        st.warning("""
✔ Monitor rainfall continuously

✔ Keep emergency teams ready

✔ Inspect dams

✔ Monitor river water level
""")

    else:

        st.error("🔴 HIGH FLOOD RISK")

        st.error("""
✔ Immediate flood warning

✔ Activate evacuation plan

✔ Deploy disaster response teams

✔ Monitor rivers continuously

✔ Prepare emergency shelters
""")

    st.markdown("---")

    # ---------------- TWO COLUMN DASHBOARD ----------------

    left, right = st.columns([2,1])

    with left:

        st.subheader("📋 Input Summary")

        summary = {
            "Parameter":[
                "Monsoon",
                "Topography",
                "River",
                "Deforestation",
                "Urbanization",
                "Climate Change",
                "Drainage",
                "Wetland Loss",
                "Population",
                "Political Factors"
            ],

            "Value":[
                monsoon,
                topography,
                river,
                deforestation,
                urbanization,
                climate,
                drainage,
                wetland,
                population,
                political
            ]
        }

        st.table(summary)


# ================= FOOTER =================

st.markdown("""
<div style='text-align:center;
padding:20px;
background:#0B3D91;
border-radius:10px;
color:white;'>

<h3> Flood Risk Prediction System</h3>

Machine Learning Based Decision Support Dashboard

Developed using

Python • Scikit-Learn • Streamlit

<br><br>

Developed by

<b>Gahana Khandelwal</b>

</div>
""", unsafe_allow_html=True)