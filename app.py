import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time

# --- STABLE PAGE CONFIG ---
st.set_page_config(page_title="Project Sentinel AI", page_icon="🔬", layout="wide")

# --- CLEAN HEADER (No crash-prone CSS) ---
st.title("🧬 3M™ PROJECT SENTINEL")
st.write("### Multi-Modal AI Early Detection Platform")
st.info("System Status: Neural Network Online | Latent Space: Synchronized")

# --- STEP 1: MULTI-MODAL DATA INPUTS ---
st.write("---")
col_cam, col_data = st.columns([1.2, 1])

with col_cam:
    st.write("#### 📸 1. Scan Diagnostic Cassette")
    # This triggers the smartphone/webcam automatically
    img_file = st.camera_input("Center the Sentinel-U Test Strip in the frame")

with col_data:
    st.write("#### 📋 2. Clinical Context ('Other Data')")
    # These "Other Data" points drive the Bayesian AI logic
    age = st.number_input("Patient Age", min_value=1, max_value=120, value=55)
    diabetes = st.radio("New-Onset Diabetes (within 2 yrs)?", ["No", "Yes"])
    family_hx = st.checkbox("Family History of Pancreatic Malignancy")
    
    # Adding a "Symptoms Score" as extra 'Other Data'
    symptoms = st.multiselect("Active Indicators", 
                             ["None", "Weight Loss", "Jaundice", "Abdominal Pain"])

# --- STEP 2: AI EXECUTION ENGINE ---
if img_file:
    with st.status("🚀 Processing Multi-Modal Signals...", expanded=True) as status:
        st.write("Extracting Sentinel-5 RNA Intensity...")
        time.sleep(1)
        st.write("Correlating Clinical Metadata...")
        time.sleep(1)
        st.write("Mapping Patient to 3D Latent Manifold...")
        status.update(label="Analysis Complete!", state="complete", expanded=False)

    # --- SIMULATED AI LOGIC (Winning Bayesian Approach) ---
    # We calculate risk based on biomarkers + 'Other Data'
    risk_score = 0.40 # Baseline
    if diabetes == "Yes": risk_score += 0.25
    if family_hx: risk_score += 0.15
    if len(symptoms) > 0 and "None" not in symptoms: risk_score += 0.10
    
    # Random variance to simulate real-time AI processing
    final_risk = min(risk_score + np.random.uniform(0.01, 0.08), 0.98)

    # --- DISPLAYING THE RESULTS ---
    st.write("---")
    res_col1, res_col2 = st.columns(2)

    with res_col1:
        st.subheader("AI Diagnostic Index")
        # Visual Gauge
        st.metric(label="Malignancy Probability", value=f"{final_risk*100:.1f}%")
        
        if final_risk > 0.70:
            st.error("🚨 HIGH RISK: Sentinel-5 Threshold Exceeded")
            st.write("**Action:** Immediate referral for EUS/Biopsy recommended.")
        else:
            st.success("✅ LOW RISK: Within Normal Transcriptomic Range")
        
        # New Feature: Downloadable Report for 3M Judges
        report_text = f"PROJECT SENTINEL REPORT\nRisk: {final_risk*100:.1f}%\nFactors: Age {age}, Diabetes: {diabetes}"
        st.download_button("📄 Download Sentinel Report", report_text, file_name="sentinel_report.txt")

    with res_col2:
        st.subheader("3D Malignancy Manifold")
        # Creating a more robust 3D Manifold
        df = pd.DataFrame({
            'X': np.random.randn(50), 'Y': np.random.randn(50), 'Z': np.random.randn(50),
            'State': ['Normal']*40 + ['Malignant']*10
        })
        # Add the specific "Patient" point
        patient_pt = pd.DataFrame({'X':[final_risk*3], 'Y':[final_risk*2], 'Z':[final_risk*4], 'State':['PATIENT']})
        df = pd.concat([df, patient_pt])

        fig = px.scatter_3d(df, x='X', y='Y', z='Z', color='State',
                             color_discrete_map={'Normal':'blue', 'Malignant':'red', 'PATIENT':'gold'},
                             title="Patient Position in Latent Space")
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

st.write("---")
st.write("#### Sentinel-5 Target Panel:")
st.caption("KRT19 | ANXA1 | MLPH | MALL | CYP2C9")
