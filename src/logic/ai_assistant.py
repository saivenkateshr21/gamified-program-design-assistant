
from src.data.ai_knowledge_base import AI_KNOWLEDGE
import re

class AIAssistant:
    def __init__(self):
        self.knowledge_base = AI_KNOWLEDGE

    def analyze_input(self, stage_name, user_input):
        """
        Analyzes the user's input and returns relevant guiding questions and examples.
        
        Args:
            stage_name (str): The current program stage (e.g., "Problem", "Outcomes").
            user_input (str): The text entered by the user.
            
        Returns:
            dict: A dictionary containing 'questions' (list) and 'examples' (list).
        """
        stage_data = self.knowledge_base.get(stage_name)
        
        if not stage_data:
            return {"questions": [], "examples": []}
            
        # Default content
        defaults = stage_data.get("defaults", {})
        questions = defaults.get("questions", [])[:] # Copy list
        examples = defaults.get("examples", [])[:]   # Copy list
        
        if not user_input or not user_input.strip():
            # If input is empty, just return defaults as "Getting Started" help
            return {
                "questions": questions,
                "examples": examples,
                "is_generic": True
            }
            
        # Keyword matching
        input_lower = user_input.lower()
        keywords = stage_data.get("keywords", {})
        
        found_keywords = False
        specific_questions = []
        specific_examples = []
        
        for keyword, content in keywords.items():
            # Use regex to find whole words only (prevents "message" matching "age")
            # \b matches word boundary
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, input_lower):
                found_keywords = True
                specific_questions.extend(content.get("questions", []))
                specific_examples.extend(content.get("examples", []))
        
        if found_keywords:
            # Prioritize specific content, but keep some defaults if needed (optional strategy)
            # For now, let's just use specific ones if found, or mix them.
            # Let's return specific ones primarily to be "smart".
            return {
                "questions": specific_questions,
                "examples": specific_examples,
                "is_generic": False
            }
        else:
            return {
                "questions": questions,
                "examples": examples,
                "is_generic": True
            }

    def get_suggestions_for_report(self, stage_name, user_input):
        """
        Helper to get formatted suggestions for the static report.
        """
        analysis = self.analyze_input(stage_name, user_input)
        return analysis
