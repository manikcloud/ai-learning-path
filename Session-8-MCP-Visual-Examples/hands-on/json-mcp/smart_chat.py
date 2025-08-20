#!/usr/bin/env python3
"""
Smart Chat CLI - Automatic Model Selection
Usage: python smart_chat.py "Your question here"
"""

import json
import sys
import subprocess
import time

def load_routing_config():
    """Load routing rules from JSON config"""
    try:
        with open('smart-mcp.json', 'r') as f:
            config = json.load(f)
            return config['mcp_routing']['routing_rules']
    except Exception as e:
        print(f"Error loading config: {e}")
        return None

def analyze_question(question, routing_rules):
    """Analyze question and select best model"""
    question_lower = question.lower()
    
    # Check travel keywords
    travel_keywords = routing_rules['travel_questions']['keywords']
    if any(keyword in question_lower for keyword in travel_keywords):
        return {
            'model': routing_rules['travel_questions']['use_model'],
            'reason': f"Detected travel keywords: {[k for k in travel_keywords if k in question_lower]}",
            'category': 'travel_questions'
        }
    
    # Check coding keywords  
    coding_keywords = routing_rules['coding_questions']['keywords']
    if any(keyword in question_lower for keyword in coding_keywords):
        return {
            'model': routing_rules['coding_questions']['use_model'],
            'reason': f"Detected coding keywords: {[k for k in coding_keywords if k in question_lower]}",
            'category': 'coding_questions'
        }
    
    # Check general keywords
    general_keywords = routing_rules['general_questions']['keywords']
    if any(keyword in question_lower for keyword in general_keywords):
        return {
            'model': routing_rules['general_questions']['use_model'],
            'reason': f"Detected general keywords: {[k for k in general_keywords if k in question_lower]}",
            'category': 'general_questions'
        }
    
    # Default fallback
    return {
        'model': 'phi-fast:latest',
        'reason': 'No specific keywords detected, using default general model',
        'category': 'default'
    }

def call_ollama(model, prompt):
    """Call Ollama API using curl"""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    cmd = [
        'curl', '-s', '-X', 'POST', 'http://localhost:11434/api/generate',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps(payload)
    ]
    
    try:
        print(f"🔄 Calling {model}...")
        start_time = time.time()
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        end_time = time.time()
        
        if result.returncode == 0:
            response_data = json.loads(result.stdout)
            return {
                'response': response_data.get('response', 'No response received'),
                'time': round(end_time - start_time, 2),
                'success': True
            }
        else:
            return {
                'response': f"Error: {result.stderr}",
                'time': 0,
                'success': False
            }
            
    except subprocess.TimeoutExpired:
        return {
            'response': "Error: Request timed out",
            'time': 0,
            'success': False
        }
    except Exception as e:
        return {
            'response': f"Unexpected error: {str(e)}",
            'time': 0,
            'success': False
        }

def main():
    if len(sys.argv) != 2:
        print("Usage: python smart_chat.py \"Your question here\"")
        print("\nExamples:")
        print("  python smart_chat.py \"What's the best time to visit Paris?\"")
        print("  python smart_chat.py \"Write a Python function to sort a list\"")
        sys.exit(1)
    
    question = sys.argv[1]
    
    print("🤖 Smart Chat - Automatic Model Selection")
    print("=" * 50)
    print(f"📝 Question: {question}")
    print()
    
    # Load routing configuration
    routing_rules = load_routing_config()
    if not routing_rules:
        print("❌ Could not load routing configuration")
        sys.exit(1)
    
    # Analyze question and select model
    selection = analyze_question(question, routing_rules)
    
    print("🧠 Smart Analysis:")
    print(f"   ✓ Category: {selection['category']}")
    print(f"   ✓ Selected Model: {selection['model']}")
    print(f"   ✓ Reason: {selection['reason']}")
    print()
    
    # Call the selected model
    result = call_ollama(selection['model'], question)
    
    if result['success']:
        print("✅ Smart Response:")
        print("-" * 20)
        print(result['response'])
        print()
        print(f"⏱️  Response time: {result['time']}s")
    else:
        print("❌ Error:")
        print(result['response'])

if __name__ == "__main__":
    main()
