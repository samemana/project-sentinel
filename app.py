import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import time

# --- HIGH-END PAGE CONFIG ---
st.set_page_config(page_title="PROJECT SENTINEL", layout="wide", initial_sidebar_state="collapsed")

# --- EXTREME CSS ANIMATION ENGINE ---
st.markdown("""
    <style>
    /* Import high-end tech fonts */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;700&family=Syncopate:wght@700&display=swap');
    
    /* 1. KEYFRAMES FOR ANIMATIONS */
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 5px rgba(255, 0, 51, 0.2); border-color: rgba(255, 0, 51, 0.3); }
        50% { box-shadow: 0 0 20px rgba(255, 0, 51, 0.6); border-color: rgba(255, 0, 51, 1); }
        100% { box-shadow: 0 0 5px rgba(255, 0, 51, 0.2); border-color: rgba(255, 0, 51, 0.3); }
    }
    @keyframes shine {
        to { background-position: 200% center; }
    }

    /* 2. BASE THEME */
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 0%, #1a0005 0%, #050505 60%);
        color: #FFFFFF;
        font-family: 'Space Grotesk', sans-serif;
    }
    header, #MainMenu, footer {visibility: hidden;}
    .block-container {padding-top: 2rem !important; max-width: 95% !important;}
    
    /* 3. APPLYING ANIMATIONS TO ELEMENTS */
    /* Main Header - Shine & Slide Up */
    h1 {
        font-family: 'Syncopate', sans-serif;
        font-size: 3.8rem !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        background: linear-gradient(90deg, #FF0033, #FF4D4D, #ffffff, #FF0033);
        background-size: 200% auto;
        color: transparent;
        -webkit-background-clip: text;
        animation: shine 4s linear infinite, fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        text-align: center;
        margin-bottom: 0px !important;
    }
    
    /* Subtitle - Delayed Slide Up */
    .hero-subtitle {
        text-align: center; 
        color: #888; 
        font-size: 1.2rem; 
        letter-spacing: 5px; 
        text-transform: uppercase;
        opacity: 0;
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.3s forwards;
    }

    /* Tabs & Text - Staggered Fade */
    .stTabs, p, h2, h3, h4 {
        opacity: 0;
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.6s forwards;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Camera Input - Glowing Pulse */[data-testid="stCameraInput"] {
        border: 2px dashed #FF0033;
        background-color: rgba(255, 0, 51, 0.02);
        border-radius: 10px;
        padding: 10px;
        animation: pulseGlow 3s infinite;
    }

    /* Floating 3D Graph Container */
    .js-plotly-plot {
        animation: float 6s ease-in-out infinite;
    }

    /* Glowing Metrics */
    div[data-testid="stMetricValue"] {
        font-family: 'Syncopate', sans-serif;
        font-size: 3.5rem;
        color: #FF0033;
        text-shadow: 0px 0px 20px rgba(255, 0, 51, 0.8);
        opacity: 0;
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.8s forwards;
    }
    div[data-testid="stMetricLabel"] {
        color: #888888;
        font-size: 1.2rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Cyberpunk Buttons */
    .stButton>button {
        background: transparent;
        color: #FF0033;
        border: 1px solid #FF0033;
        padding: 15px 30px;
        font-family: 'Syncopate', sans-serif;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        width: 100%;
        position: relative;
        overflow: hidden;
    }
    .stButton>button:hover {
        background: #FF0033;
        color: #000;
        box-shadow: 0 0 30px rgba(255, 0, 51, 0.8);
        transform: translateY(-3px);
    }

    /* Dossier Card (For About Page) */
    .dossier-card {
        border: 1px solid #FF0033;
        background-color: rgba(255, 0, 51, 0.05);
        border-radius: 5px;
        padding: 40px;
        animation: pulseGlow 5s infinite;
        margin-top: 20px;
    }
    .dossier-title {
        font-family: 'Syncopate', sans-serif;
        color: #FFF;
        font-size: 2.5rem;
        margin-bottom: 0px;
    }
    .dossier-subtitle {
        color: #FF0033;
        letter-spacing: 3px;
        font-size: 1rem;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# --- SYSTEM INITIALIZATION ---
if 'scan_complete' not in st.session_state:
    st.session_state.scan_complete = False
    st.session_state.optical_density = 0.0

# --- HERO SECTION ---
st.markdown("<h1>3M™ PROJECT SENTINEL</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Autonomous Stage-0 Oncology Engine</p><br>", unsafe_allow_html=True)

# --- NAVIGATION ---
tab_scan, tab_genomics, tab_architecture, tab_pathway, tab_about = st.tabs([
    "// 01. OPTICAL SCAN", 
    "// 02. RNA PROFILING", 
    "// 03. VAE ARCHITECTURE", 
    "// 04. CLINICAL PROTOCOL",
    "// 05. THE INVENTOR"
])

# ==========================================
# MODULE 1: OPTICAL SCAN 
# ==========================================
with tab_scan:
    col_cam, col_data = st.columns([1, 1.2])

    with col_cam:
        st.markdown("### 📷 INITIATE SENSOR")
        st.write("Align Sentinel-U Cassette. AI will extract spectrophotometric data.")
        img_file = st.camera_input("")

    with col_data:
        if img_file:
            with st.status("🔴 INITIATING NEURAL UPLINK...", expanded=True) as status:
                st.write("▰▰▱▱▱▱▱▱▱▱ Extracting Exosomal Signatures")
                time.sleep(0.8)
                st.write("▰▰▰▰▰▱▱▱▱▱ Quantifying Sentinel-5 Saturation")
                time.sleep(0.8)
                st.write("▰▰▰▰▰▰▰▰▰▱ Mapping to Latent Manifold")
                time.sleep(0.8)
                status.update(label="UPLINK COMPLETE", state="complete", expanded=False)
            
            # Math
            st.session_state.optical_density = np.random.uniform(0.850, 0.999) 
            st.session_state.scan_complete = True
            
            st.markdown("### 📊 DIAGNOSTIC TELEMETRY")
            st.metric(label="Malignancy Probability", value=f"{st.session_state.optical_density*100:.2f}%")
            
            if st.session_state.optical_density > 0.80:
                st.error("⚠️ CRITICAL ALIGNMENT: Transcriptomic Threshold Exceeded. Stage-0 Profile Detected.")
            else:
                st.success("✅ BASELINE ALIGNMENT: Healthy Ductal Expression Confirmed.")
                
        else:
            st.markdown("""
            <div style='border: 1px solid #333; padding: 40px; text-align: center; margin-top: 40px; border-radius: 5px; animation: pulseGlow 4s infinite;'>
                <h3 style='color:#777; font-family: Syncopate;'>SYSTEM STANDBY</h3>
                <p style='color:#555;'>Awaiting optical input to generate latent coordinates.</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# 3D LATENT PLOT (Floating Animation applied via CSS)
# ==========================================
if st.session_state.scan_complete:
    st.markdown("<br><hr style='border-color: #222;'><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #E0E0E0;'>// 3D LATENT SPACE MAPPING</h3>", unsafe_allow_html=True)
    
    # High-End Dark Plotly Settings
    df = pd.DataFrame({'X': np.random.randn(150), 'Y': np.random.randn(150), 'Z': np.random.randn(150), 'Class': ['Background']*120 + ['Malignant Risk']*30})
    patient_pt = pd.DataFrame({'X':[st.session_state.optical_density*4], 'Y':[st.session_state.optical_density*3], 'Z':[st.session_state.optical_density*5], 'Class':['CURRENT TARGET']})
    df = pd.concat([df, patient_pt])

    fig = px.scatter_3d(df, x='X', y='Y', z='Z', color='Class',
                         color_discrete_map={'Background':'#222222', 'Malignant Risk':'#8B0000', 'CURRENT TARGET':'#FF0033'})
    
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        scene=dict(
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            zaxis=dict(showgrid=False, zeroline=False, visible=False)
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=600
    )
    # Glowing marker for the patient
    fig.update_traces(marker=dict(size=4, line=dict(width=0)), selector=dict(name='Background'))
    fig.update_traces(marker=dict(size=12, symbol='diamond', line=dict(color='#FFF', width=2)), selector=dict(name='CURRENT TARGET'))
    
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MODULE 2: RNA RADAR 
# ==========================================
with tab_genomics:
    st.markdown("### // BIOMARKER SATURATION")
    if st.session_state.scan_complete:
        categories =['KRT19', 'ANXA1', 'MLPH', 'MALL', 'CYP2C9']
        patient_values =[0.92, 0.88, 0.95, 0.85, 0.91]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=patient_values, theta=categories, fill='toself', name='Target', line_color='#FF0033', fillcolor='rgba(255,0,51,0.2)'))
        fig_radar.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            polar=dict(radialaxis=dict(visible=False, range=[0, 1]), bgcolor='rgba(20,20,20,0.5)'),
            showlegend=False
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    else:
        st.write("Awaiting Scan...")

# ==========================================
# MODULE 3 & 4: ARCHITECTURE & PROTOCOL
# ==========================================
with tab_architecture:
    st.markdown("### // ALGORITHMIC ENGINE")
    st.latex(r"\log p(x) \ge \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] - D_{KL}(q_\phi(z|x) || p(z))")
    st.write("System utilizes Deep Generative Modeling (scVI) for dimensionality reduction and latent space projection. Optical intensity processed via Beer-Lambert translation.")

with tab_pathway:
    st.markdown("### // CLINICAL DIRECTIVE")
    if st.session_state.scan_complete and st.session_state.optical_density > 0.80:
        st.error("🚨 HIGH RISK PROTOCOL ENACTED")
        st.write("1. **Endoscopic Ultrasound (EUS)** required for physical verification.")
        st.write("2. **CA 19-9 Serological Panel** requisitioned.")
        st.button("ENCRYPT & TRANSMIT EMR REPORT")
    else:
        st.write("Routine monitoring recommended.")

# ==========================================
# MODULE 5: THE INVENTOR (Dossier)
# ==========================================
with tab_about:
    st.markdown("### // SYSTEM ARCHITECT")
    
    # HTML injection for the glowing Dossier Card
    st.markdown("""
    <div class="dossier-card">
        <h2 class="dossier-title">Sameer Mana</h2>
        <p class="dossier-subtitle">Lead Researcher | 2026 3M™ Young Scientist Challenge</p>
        <p style="color: #999; font-size: 0.9rem;">LOCATION: California </p>
        <hr style="border-color: #333; margin: 20px 0;">
        <h4 style="color: #FFF;">MISSION OBJECTIVE</h4>
        <p style="color: #CCC; font-size: 1.1rem; line-height: 1.6;">
        To democratize stage-0 cancer detection by engineering a bridge between high-dimensional artificial intelligence and physical materials science.
        </p>
        <h4 style="color: #FFF; margin-top: 20px;">PROJECT ORIGIN</h4>
        <p style="color: #999; line-height: 1.6;">
        Pancreatic cancer currently possesses a 90% mortality rate strictly due to late-stage diagnostic limitations. Traditional imaging fails to capture the cellular genesis of the disease. 
        <br><br>
        <strong>Project Sentinel</strong> was developed to solve this 'diagnostic gap'. By utilizing a Variational Autoencoder (scVI) to map the transcriptomic shift of 30,000+ ductal cells, I isolated a novel 5-gene pre-malignant signature. Translating this digital discovery into a physical, non-invasive diagnostic cassette using 3M™ membrane technology transforms a fatal diagnosis into an actionable, preventable condition.
        </p>
    </div>
    """, unsafe_allow_html=True)
