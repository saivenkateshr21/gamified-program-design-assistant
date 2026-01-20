import streamlit as st

def render_welcome():
    st.markdown("<h1 class='main-header'>🎓 Gamified Program Design Assistant</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        ### Welcome! 👋
        Design your education program in **simple, guided steps**.
        
        **How it works:**
        1.  **Define the Problem**: Understand the root cause.
        2.  **Set Outcomes**: Decide what success looks like.
        3.  **Map Stakeholders**: Know who is involved.
        4.  **Plan Activities**: Actionable steps.
        5.  **Measure Success**: Key metrics.
        
        🚀 **Gamified Experience**: Track your progress in the sidebar and earn badges as you complete sections!
        """)
        
        if st.button("Start Designing Now 🚀"):
            st.info("Please select 'Problem' from the sidebar to begin!")

    with col2:
        st.info("### Why this tool?")
        st.markdown("""
        - **Structured Thinking**: Don't start from a blank page.
        - **Review-Ready**: Generates a standard framework.
        - **No Experts Needed**: Guided prompts help you think like a pro.
        
        *The platform supports program design and planning, not automated decision-making or real-time impact evaluation.*
        """)
