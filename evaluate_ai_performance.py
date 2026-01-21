import sys
import os

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from src.logic.ai_assistant import AIAssistant
from src.data.templates import PROGRAM_STAGES
from src.data.ai_knowledge_base import AI_KNOWLEDGE

def main():
    print("========================================")
    print("🤖 AI Assistant Performance Evaluation")
    print("========================================")
    
    assistant = AIAssistant()
    
    total_stages = len(PROGRAM_STAGES)
    stages_with_knowledge = len(AI_KNOWLEDGE)
    
    print(f"\n📊 Coverage Check:")
    print(f"Total UI Stages: {total_stages}")
    print(f"Stages with Knowledge Base: {stages_with_knowledge}")
    
    if total_stages == stages_with_knowledge:
        print("✅ SUCCESS: 100% Stage Coverage")
    else:
        print(f"❌ WARNING: Coverage mismatch! ({stages_with_knowledge}/{total_stages})")
        missing = set(PROGRAM_STAGES.keys()) - set(AI_KNOWLEDGE.keys())
        print(f"   Missing Stages: {missing}")
        
    print("\n========================================")
    print("🔍 Keyword Logic & Response Testing")
    print("========================================")
    
    failed_tests = []
    passed_tests = 0
    total_tests = 0
    
    for stage_name, config in AI_KNOWLEDGE.items():
        print(f"\nEvaluating Stage: [{stage_name}]")
        
        # 1. Test Default/Empty Input
        total_tests += 1
        res = assistant.analyze_input(stage_name, "")
        if res.get("is_generic") and res.get("questions") and res.get("examples"):
             print(f"  ✅ Default input handled correctly.")
             passed_tests += 1
        else:
             print(f"  ❌ FAIL: Default input returned invalid structure.")
             failed_tests.append(f"{stage_name} - Default Input")

        # 2. Test Keywords
        keywords = config.get("keywords", {})
        if not keywords:
            print("  ⚠️ No specific keywords defined for this stage.")
            continue
            
        print(f"  Testing {len(keywords)} keywords...")
        
        for kw in keywords.keys():
            total_tests += 1
            # Exact match test
            res = assistant.analyze_input(stage_name, f"I am writing about {kw}")
            
            # Check if we got specific (non-generic) results
            if not res.get("is_generic") and res.get("questions"):
                # Basic check passed
                pass
            else:
                 # Debug: print why it failed
                 print(f"    ❌ Keyword '{kw}' failed to trigger specific response.")
                 failed_tests.append(f"{stage_name} - Keyword: {kw}")
                 continue

            # Plural/Sentence test check (known limitation, but let's test)
            # We treat this as a separate sub-test observation
            res_plural = assistant.analyze_input(stage_name, f"We have many {kw}s here")
            if res_plural.get("is_generic"):
                 print(f"    ⚠️ Note: Plural '{kw}s' did not trigger specific response (Strict matching).")
            
            passed_tests += 1

    print("\n========================================")
    print("📈 Final Summary")
    print("========================================")
    print(f"Total Tests Run: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {len(failed_tests)}")
    
    if failed_tests:
        print("\nFailures:")
        for f in failed_tests:
            print(f"- {f}")
    else:
        print("\n✅ All core logic tests passed!")

if __name__ == "__main__":
    main()
