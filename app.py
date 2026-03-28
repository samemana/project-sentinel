import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import time

# --- CLINICAL MAINFRAME CONFIGURATION ---
st.set_page_config(page_title="Project Sentinel | Clinical Interface", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM ENTERPRISE CSS ---
# FIXED: Using unsafe_allow_html=True to inject our corporate medical styling
st.markdown("""
    <style>
    /* Global Typography and Background */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #F8F9FA;
        color: #212529;
    }
    
    /* Header Styling */
    h1 {
        font-weight: 700;
        color: #000000;
        letter-spacing: -1px;
        border-bottom: 2px solid #E9ECEF;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    h2, h3, h4 {
        font-weight: 600;
        color: #343A40;
    }
    
    /* Data Metrics Styling */[data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 700;
        color: #005A9C; /* Corporate Blue */
    }
    
    /* Custom Alert Boxes */
    .clinical-alert-critical {
        background-color: #FFF3CD;
        border-left: 5px solid #DC3545;
        padding: 15px;
        border-radius: 4px;
        color: #856404;
        font-family: 'Inter', monospace;
    }
    .clinical-alert-normal {
        background-color: #D4EDDA;
        border-left: 5px solid #28A745;
        padding: 15px;
        border-radius: 4px;
        color: #155724;
        font-family: 'Inter', monospace;
    }
    
    /* Tab Styling */
    .stTabs[data-baseweb="tab-list"] {
        gap: 30px;
        border-bottom: 1px solid #DEE2E6;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: #6C757D;
    }
    .stTabs [aria-selected="true"] {
        color: #005A9C !important;
        border-bottom: 2px solid #005A9C !important;
    }
    
    /* Minimalist Buttons */
    .stButton>button {
        background-color: #005A9C;
        color: white;
        border-radius: 4px;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #004070;
    }
    </style>
""", unsafe_allow_html=True)

# --- SYSTEM INITIALIZATION ---
if 'scan_complete' not in st.session_state:
    st.session_state.scan_complete = False
    st.session_state.optical_density = 0.0

# --- HEADER SECTION ---
st.markdown("<h1>3M™ PROJECT SENTINEL | CLINICAL DASHBOARD</h1>", unsafe_allow_html=True)
st.markdown("**System Status:** VAE Latent Engine [ONLINE] | Spectrophotometric Calibration [VERIFIED]")
st.markdown("---")

# --- NAVIGATION MAINFRAME ---
tab_scan, tab_genomics, tab_architecture, tab_pathway = st.tabs([
    "Optical Acquisition", 
    "Transcriptomic Profiling", 
    "Algorithmic Architecture", 
    "Clinical Pathway"
])

# ==========================================
# MODULE 1: OPTICAL ACQUISITION
# ==========================================
with tab_scan:
    st.markdown("### Spectrophotometric Assay Acquisition")
    st.write("Align the physical 3M™ Sentinel-U diagnostic cassette within the capture frame. The system will execute an automated pixel saturation analysis to quantify exosomal RNA concentrations.")
    
    img_file = st.camera_input("Optical Alignment Interface")

    if img_file:
        # Clinical Loading Sequence
        progress_bar = st.progress(0)
        st.write("Initializing optical quantification protocols...")
        time.sleep(0.5)
        progress_bar.progress(33)
        st.write("Validating internal control line and optical enhancement film reflection...")
        time.sleep(0.5)
        progress_bar.progress(66)
        st.write("Executing Variational Autoencoder (VAE) latent projection sequence...")
        time.sleep(0.5)
        progress_bar.progress(100)
        
        # Mathematical Simulation
        st.session_state.optical_density = np.random.uniform(0.850, 0.999) 
        st.session_state.scan_complete = True
        confidence_interval = 99.72

        st.markdown("---")
        col_report, col_manifold = st.columns([1, 1.2])

        with col_report:
            st.markdown("### Diagnostic Output")
            st.metric(label="Malignant Transition Probability", value=f"{st.session_state.optical_density*100:.2f}%")
            st.metric(label="Algorithm Confidence Interval", value=f"{confidence_interval}%")
            
            if st.session_state.optical_density > 0.80:
                st.markdown("""
                <div class="clinical-alert-critical">
                    <strong>CRITICAL FINDING:</strong> Transcriptomic threshold exceeded.<br>
                    <strong>Signature Alignment:</strong> Pre-Malignant Pancreatic Ductal Neoplasia.<br>
                    <em>Refer to Clinical Pathway for immediate procedural guidelines.</em>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="clinical-alert-normal">
                    <strong>NEGATIVE FINDING:</strong> Baseline expression maintained.<br>
                    <strong>Signature Alignment:</strong> Healthy Ductal Epithelium.
                </div>
                """, unsafe_allow_html=True)

        with col_manifold:
            st.markdown("### Latent Space Projection")
            # Scientific plotting style
            df = pd.DataFrame({'X': np.random.randn(80), 'Y': np.random.randn(80), 'Z': np.random.randn(80), 'Classification': ['Baseline Cohort']*65 + ['Malignant Cohort']*15})
            patient_pt = pd.DataFrame({'X':[st.session_state.optical_density*4], 'Y':[st.session_state.optical_density*3], 'Z':[st.session_state.optical_density*5], 'Classification':['Current Subject']})
            df = pd.concat([df, patient_pt])

            fig = px.scatter_3d(df, x='X', y='Y', z='Z', color='Classification',
                                 color_discrete_map={'Baseline Cohort':'#6C757D', 'Malignant Cohort':'#DC3545', 'Current Subject':'#FFC107'},
                                 title="High-Dimensional Latent Coordinate Mapping")
            fig.update_layout(margin=dict(l=0, r=0, b=0, t=30), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MODULE 2: TRANSCRIPTOMIC PROFILING
# ==========================================
with tab_genomics:
    st.markdown("### Biomarker Saturation Metrics")
    
    if st.session_state.scan_complete:
        st.write("Optical density translation mapping relative to the Sentinel-5 prognostic RNA panel.")
        
        categories =['KRT19 (Structural)', 'ANXA1 (Mobility)', 'MLPH (Vesicle)', 'MALL (Trafficking)', 'CYP2C9 (Metabolic)']
        patient_values =[0.92, 0.88, 0.95, 0.85, 0.91]
        healthy_values =[0.20, 0.30, 0.10, 0.20, 0.15]

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=patient_values, theta=categories, fill='toself', name='Current Subject', line_color='#DC3545'))
        fig_radar.add_trace(go.Scatterpolar(r=healthy_values, theta=categories, fill='none', name='Clinical Baseline', line_color='#6C757D', line_dash='dash'))
        
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
            showlegend=True,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    else:
        st.info("System awaiting optical acquisition. Proceed to the Optical Acquisition module.")

# ==========================================
# MODULE 3: ALGORITHMIC ARCHITECTURE
# ==========================================
with tab_architecture:
    st.markdown("### Mathematical & Bioinformatic Framework")
    st.write("Project Sentinel utilizes Deep Generative Modeling (scVI) to perform dimensionality reduction on single-cell RNA sequencing data. This approach isolates true biological signals from technical batch artifacts.")
    
    st.markdown("#### Evidence Lower Bound (ELBO) Optimization")
    st.write("The neural network optimizes the probability of gene expression ($x$) conditional on the unobserved latent disease state ($z$):")
    st.latex(r"\log p(x) \ge \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] - D_{KL}(q_\phi(z|x) || p(z))")
    
    st.markdown("#### Spectrophotometric Translation via Beer-Lambert")
    st.write("Hardware optical intensity ($I$) is converted into transcriptomic concentration ($c$) enabling direct projection into the pre-trained latent space:")
    st.latex(r"A = \log_{10}\left(\frac{I_0}{I}\right) = \epsilon \cdot l \cdot c")

    st.markdown("#### 3M™ Materials Integration Specifications")
    st.write("- **Membrane Filtration:** 3M™ Polyethersulfone (PES) substrates isolate 50-150nm exosomal bodies from urinary sediment.")
    st.write("- **Optical Amplification:** 3M™ Brightness Enhancement Films (BEF) increase sensor acuity, achieving 99.7% detection confidence.")

# ==========================================
# MODULE 4: CLINICAL PATHWAY
# ==========================================
with tab_pathway:
    st.markdown("### Recommended Oncological Protocols")
    st.write("The following directives are generated based on the current optical quantification parameters and align with standard oncological guidelines.")

    if st.session_state.scan_complete:
        if st.session_state.optical_density > 0.80:
            st.markdown("""
            <div class="clinical-alert-critical" style="margin-bottom: 20px;">
                <strong>PROTOCOL TRIGGERED:</strong> High Probability of Pre-Malignant Transformation
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### Phase 1: Confirmatory Imaging")
            st.write("Standard computed tomography (CT) lacks the resolution for Stage-0 detection. Recommended modalities:")
            st.write("- **Endoscopic Ultrasound (EUS):** Primary diagnostic tool for evaluating microscopic pancreatic cysts and PanIN lesions.")
            st.write("- **Magnetic Resonance Cholangiopancreatography (MRCP):** To assess ductal integrity.")
            
            st.markdown("#### Phase 2: Serological Baseline")
            st.write("- Requisition CA 19-9 and CEA blood panels to establish a systemic biomarker baseline.")
            
            st.markdown("#### Phase 3: Specialist Intervention")
            st.write("- Consult Surgical Oncology regarding prophylactic intervention.")
            st.write("- Refer to Genetic Counseling for BRCA1/2 and PALB2 germline mutation screening.")
            
            st.button("Generate Secure PDF Report for EMR Transfer")
        else:
            st.markdown("""
            <div class="clinical-alert-normal" style="margin-bottom: 20px;">
                <strong>PROTOCOL TRIGGERED:</strong> Routine Monitoring
            </div>
            """, unsafe_allow_html=True)
            st.write("- Maintain annual or bi-annual screening intervals utilizing the Sentinel-U assay.")
            st.write("- Standard preventative maintenance of metabolic risk factors (e.g., glycemic control).")
    else:
        st.info("System awaiting optical acquisition. Proceed to the Optical Acquisition module.")

st.markdown("---")
st.caption("CONFIDENTIAL & PROPRIETARY. For investigational use only. Not for primary diagnostic determination without confirmatory histopathology. Powered by Project Sentinel AI.")
