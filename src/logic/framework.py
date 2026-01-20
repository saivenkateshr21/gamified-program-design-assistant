import json
import streamlit as st
from src.data.templates import PROGRAM_STAGES

class FrameworkManager:
    def __init__(self):
        # Initialize session state for program data if not exists
        if 'program_data' not in st.session_state:
            st.session_state.program_data = {}
        
        # Initialize progress tracker
        if 'progress' not in st.session_state:
            st.session_state.progress = {stage: False for stage in PROGRAM_STAGES.keys()}

    def update_data(self, stage, key, value):
        """Updates the program data for a specific stage and key."""
        if stage not in st.session_state.program_data:
            st.session_state.program_data[stage] = {}
        
        st.session_state.program_data[stage][key] = value
        self.check_stage_completion(stage)

    def get_data(self, stage, key):
        """Retrieves data for a specific stage and key."""
        return st.session_state.program_data.get(stage, {}).get(key, "")

    def check_stage_completion(self, stage):
        """Checks if a stage is complete based on inputs."""
        stage_config = PROGRAM_STAGES.get(stage)
        if not stage_config:
            return
        
        # Check if all fields in the stage have some content
        data = st.session_state.program_data.get(stage, {})
        is_complete = all(data.get(step['key'], "").strip() != "" for step in stage_config['steps'])
        
        st.session_state.progress[stage] = is_complete

    def get_progress_percentage(self):
        """Calculates total progress percentage."""
        total_stages = len(PROGRAM_STAGES)
        completed_stages = sum(st.session_state.progress.values())
        return int((completed_stages / total_stages) * 100) if total_stages > 0 else 0

    def export_data(self):
        """Exports the program data as a JSON string."""
        return json.dumps(st.session_state.program_data, indent=4)

    def generate_markdown_report(self):
        """Generates a markdown report of the program design."""
        md = "# Gamified Program Design Framework\n\n"
        for stage_key, stage_info in PROGRAM_STAGES.items():
            md += f"## {stage_info['title']}\n\n"
            data = st.session_state.program_data.get(stage_key, {})
            for step in stage_info['steps']:
                val = data.get(step['key'], "*(Not answered)*")
                md += f"**{step['label']}**:\n{val}\n\n"
            md += "---\n\n"
        return md

    def generate_pdf(self, filename="program_design.pdf"):
        """Generates a PDF report of the program design."""
        from fpdf import FPDF
        
        class PDF(FPDF):
            def header(self):
                self.set_font('Arial', 'B', 15)
                self.cell(0, 10, 'Gamified Program Design Framework', 0, 1, 'C')
                self.ln(10)

            def footer(self):
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        for stage_key, stage_info in PROGRAM_STAGES.items():
            # Stage Title
            pdf.set_font("Arial", 'B', 14)
            pdf.set_text_color(40, 167, 69) # Green color
            pdf.cell(0, 10, stage_info['title'], 0, 1)
            pdf.set_text_color(0, 0, 0) # Reset color
            pdf.ln(2)
            
            # Content
            data = st.session_state.program_data.get(stage_key, {})
            pdf.set_font("Arial", size=12)
            
            for step in stage_info['steps']:
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(0, 8, step['label'], 0, 1)
                
                pdf.set_font("Arial", size=11)
                val = data.get(step['key'], "*(Not answered)*")
                pdf.multi_cell(0, 6, val)
                pdf.ln(4)
            
            pdf.ln(5)
            
        return pdf.output(dest='S').encode('latin-1', 'replace')

    def generate_text_file(self):
        """Generates a plain text representation."""
        txt = "GAMIFIED PROGRAM DESIGN FRAMEWORK\n"
        txt += "="*40 + "\n\n"
        
        for stage_key, stage_info in PROGRAM_STAGES.items():
            txt += f"[{stage_info['title']}]\n"
            txt += "-"*len(stage_info['title']) + "\n"
            
            data = st.session_state.program_data.get(stage_key, {})
            for step in stage_info['steps']:
                val = data.get(step['key'], "(Not answered)")
                txt += f"{step['label']}:\n{val}\n\n"
            txt += "\n"
            
        return txt
        return txt

    def calculate_readiness_score(self):
        """Calculates a readiness score broken down by Coverage and Depth."""
        total_fields = 0
        filled_fields = 0
        deep_fields = 0
        
        for stage_key, stage_info in PROGRAM_STAGES.items():
            data = st.session_state.program_data.get(stage_key, {})
            for step in stage_info['steps']:
                total_fields += 1
                val = data.get(step['key'], "").strip()
                if val:
                    filled_fields += 1
                    # Simple rule for "Review Ready" depth: > 40 chars
                    if len(val) > 40:
                        deep_fields += 1
                        
        coverage_score = int((filled_fields / total_fields) * 100) if total_fields > 0 else 0
        depth_score = int((deep_fields / total_fields) * 100) if total_fields > 0 else 0
        
        # Weighted Score: 60% Coverage (doing the work), 40% Depth (doing it well)
        final_score = int((coverage_score * 0.6) + (depth_score * 0.4))
        
        return {
            "total": final_score,
            "coverage": coverage_score,
            "depth": depth_score
        }

    def get_gaps_report(self):
        """Identifies gaps with supportive, coach-like feedback."""
        gaps = []
        
        for stage_key, stage_info in PROGRAM_STAGES.items():
            data = st.session_state.program_data.get(stage_key, {})
            for step in stage_info['steps']:
                val = data.get(step['key'], "").strip()
                
                if not val:
                    gaps.append({
                        "stage": stage_info['title'],
                        "field": step['label'],
                        "issue": "This section is empty.",
                        "tip": f"Coach says: Even a rough draft helps! Try outlining 2-3 bullet points for '{step['label']}'.",
                        "severity": "high"
                    })
                elif len(val) <= 40:
                    gaps.append({
                        "stage": stage_info['title'],
                        "field": step['label'],
                        "issue": "A bit brief.",
                        "tip": f"Coach says: Could you add one more detail to '{step['label']}' to clarify your thought process?",
                        "severity": "medium"
                    })
        return gaps
