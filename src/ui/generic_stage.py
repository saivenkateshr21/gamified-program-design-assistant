import streamlit as st
from src.data.templates import PROGRAM_STAGES
from src.logic.ai_assistant import AIAssistant

# Initialize AI
ai_assistant = AIAssistant()

def render_stage(manager, stage_name):
    stage_config = PROGRAM_STAGES.get(stage_name)
    if not stage_config:
        st.error("Stage configuration not found.")
        return

    st.markdown(f"<h1 class='main-header'>{stage_config['title']}</h1>", unsafe_allow_html=True)

    # Coach Tip
    st.markdown(f"""
        <div class='coach-tip'>
            <strong>💡 Coach's Tip:</strong> {stage_config['description']}
        </div>
    """, unsafe_allow_html=True)

    # Render inputs
    for step in stage_config['steps']:
        key = step['key']
        current_val = manager.get_data(stage_name, key)
        
        st.subheader(step['label'])
        
        # Contextual Hint (Thought Starter)
        with st.expander("💡 Need a hint?", expanded=False):
            st.markdown(f"**Think about:** {step.get('help', 'Be specific and realistic.')}")

        if step['type'] == 'text_area':
            val = st.text_area(
                label=step['label'],
                value=current_val,
                placeholder=step['placeholder'],
                key=f"{stage_name}_{key}",
                label_visibility="collapsed",
                height=150
            )
        else:
            val = st.text_input(
                label=step['label'],
                value=current_val,
                placeholder=step['placeholder'],
                key=f"{stage_name}_{key}",
                label_visibility="collapsed"
            )
        
        # Update data on change (handled by session state mostly, but explicit update helps logic)
        if val != current_val:
            manager.update_data(stage_name, key, val)

        # --- AI Assistant Section ---
        # Get suggestions based on current input
        suggestions = ai_assistant.analyze_input(stage_name, current_val)
        
        if suggestions["questions"] or suggestions["examples"]:
            with st.expander("✨ AI Assistant Insights", expanded=True):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 🤔 Suggested Questions")
                    for q in suggestions["questions"]:
                        st.markdown(f"- {q}")
                        
                with col2:
                    st.markdown("### 💡 Recommended Examples")
                    for ex in suggestions["examples"]:
                        st.markdown(f"_{ex}_")
                        
                if suggestions.get("is_generic"):
                    st.caption("Start typing to get more specific suggestions based on your keywords!")
        # -----------------------------

    st.markdown("---")
    st.info("Dont forget to navigate to the next section using the sidebar once you're done!")
