import streamlit as st
from src.logic.framework import FrameworkManager
from src.data.templates import PROGRAM_STAGES
import importlib

# Page configuration
st.set_page_config(
    page_title="Gamified Program Design Assistant",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for aesthetics (Green/Blue theme for education/NGO)
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #28a745;
    }
    .main-header {
        font-size: 2.5rem;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .coach-tip {
        background-color: #e8f5e9;
        border-left: 4px solid #28a745;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 4px;
        color: #2e7d32;
    }
    .sidebar-text {
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Logic
manager = FrameworkManager()

# Sidebar Navigation
st.sidebar.title("🧭 Navigation")

# Navigation Options
options = ["Home"] + list(PROGRAM_STAGES.keys()) + ["Review & Download"]
selection = st.sidebar.radio("Go to:", options)

# Progress Tracking
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Your Progress")
progress = manager.get_progress_percentage()
st.sidebar.progress(progress / 100)
st.sidebar.caption(f"{progress}% Complete")

# Show completion badges
st.sidebar.markdown("### Milestones")
for stage in PROGRAM_STAGES.keys():
    is_done = st.session_state.progress.get(stage, False)
    icon = "✅" if is_done else "⬜"
    st.sidebar.markdown(f"{icon} {stage}")

# Routing Logic
if selection == "Home":
    from src.ui.welcome import render_welcome
    render_welcome()

elif selection == "Review & Download":
    from src.ui.review import render_review
    render_review(manager)

else:
    # Generic rendering for standard stages
    from src.ui.generic_stage import render_stage
    render_stage(manager, selection)
