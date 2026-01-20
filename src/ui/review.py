import streamlit as st

def render_review(manager):
    st.markdown("<h1 class='main-header'>📋 Review & Download</h1>", unsafe_allow_html=True)

    # --- Intelligence Features ---
    # --- Intelligence Features ---
    st.subheader("📊 Program Readiness Score")
    score_data = manager.calculate_readiness_score()
    score = score_data['total']
    
    # Gamified Levels
    if score >= 85:
        level = "🏆 Grant-Ready"
        score_color = "green"
        msg = "Excellent work! Your program design is detailed and structured."
    elif score >= 50:
        level = "🚀 Emerging Draft"
        score_color = "orange"
        msg = "Good foundation! You've covered the basics, but some details are light."
    else:
        level = "📝 Concept Note"
        score_color = "red"
        msg = "Just starting out! Keep going, every section you fill builds the story."

    col_score, col_details = st.columns([1, 2])
    with col_score:
        st.markdown(f"""
            <div style='text-align:center'>
                <h1 style='color:{score_color}; margin:0; font-size: 3.5rem;'>{score}</h1>
                <p style='font-size: 1.2rem; font-weight:bold; color: #555;'>{level}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col_details:
        st.info(f"**Coach's Feedback:** {msg}")
        st.write("**Score Breakdown:**")
        st.progress(score_data['coverage'] / 100, text=f"Coverage (Fields Filled): {score_data['coverage']}%")
        st.progress(score_data['depth'] / 100, text=f"Depth (Detail Level): {score_data['depth']}%")
        st.caption("*Tips: Fill all fields for Coverage. Add detailed descriptions (>40 chars) for Depth.*")

    # Gap Analysis
    gaps = manager.get_gaps_report()
    if gaps:
        st.subheader("🧐 What's Missing? (Coach's Suggestions)")
        with st.expander(f"View {len(gaps)} Suggestions to Improve", expanded=True):
            for gap in gaps:
                icon = "🛑" if gap['severity'] == "high" else "💡"
                st.markdown(f"""
                    **{icon} {gap['stage']} / {gap['field']}**  
                    *Issue:* {gap['issue']}  
                    **Suggestion:** {gap['tip']}
                """)
                st.divider()
    else:
        st.success("✅ All clear! Your program design looks robust and ready for review.")

    st.markdown("---")
    st.markdown("### Preview")
    
    # Generate Markdown Report
    report = manager.generate_markdown_report()
    st.markdown(report)

    st.markdown("---")
    st.subheader("📥 Download Options")

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="Download as PDF",
            data=manager.generate_pdf(),
            file_name="program_design.pdf",
            mime="application/pdf"
        )
    
    with col2:
        st.download_button(
            label="Download as Text/Doc",
            data=manager.generate_text_file(),
            file_name="program_design.txt",
            mime="text/plain"
        )
