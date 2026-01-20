import streamlit as st
from src.data.templates import PROGRAM_STAGES

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

    st.markdown("---")
    st.info("Dont forget to navigate to the next section using the sidebar once you're done!")
