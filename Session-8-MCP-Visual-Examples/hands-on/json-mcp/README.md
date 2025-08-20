# JSON MCP Configuration Setup

## 🎯 What You'll Build

A simple JSON-based MCP configuration that automatically routes questions to the right models without any programming.

## 📁 Files Overview

- **`mcp-config.json`** - Defines your 3 models and available tools
- **`model-routing.json`** - Smart routing rules for automatic model selection

## 🚀 How to Use

### Step 1: Review the Configuration
```bash
# Look at your model setup
cat mcp-config.json

# Check the routing rules  
cat model-routing.json
```

### Step 2: Test the Routing Logic

**Example Questions and Expected Routing:**

| Question | Detected Keywords | Selected Model | Why |
|----------|------------------|----------------|-----|
| "Write a Python function" | `function` | `code_expert` (codellama) | Code generation needed |
| "Explain recursion" | `explain` | `concept_expert` (deepseek-coder) | Concept explanation needed |
| "Best practices for functions" | `best practices` | `practice_expert` (mistral) | Guidelines and advice needed |
| "Complete Python tutorial" | `complete`, `tutorial` | `ask_all_experts` (all 3) | Comprehensive coverage needed |

### Step 3: Understanding the Magic

**Before JSON MCP:**
```bash
# Manual process (3 separate commands)
curl -X POST http://localhost:11434/api/generate -d '{"model": "deepseek-coder:latest", "prompt": "Explain functions"}'
curl -X POST http://localhost:11434/api/generate -d '{"model": "codellama:latest", "prompt": "Show function examples"}'  
curl -X POST http://localhost:11434/api/generate -d '{"model": "mistral:latest", "prompt": "Function best practices"}'
```

**After JSON MCP:**
```
User: "Explain Python functions with examples and best practices"
MCP: *reads routing rules* → *detects comprehensive question* → *uses ask_all_experts* → *coordinates all 3 models automatically*
```

## 🎨 Customization

### Add New Routing Rules
Edit `model-routing.json` to add new question types:

```json
{
  "name": "debugging_questions",
  "keywords": ["error", "bug", "fix", "debug", "not working"],
  "targetModel": "code_expert",
  "confidence": 0.9
}
```

### Modify Model Assignments
Edit `mcp-config.json` to change which model handles what:

```json
"specialties": ["your", "custom", "keywords"]
```

## 🧪 Testing Your Setup

1. **Verify Models Available:**
   ```bash
   curl http://localhost:11434/api/tags
   ```

2. **Test Individual Models:**
   ```bash
   # Test deepseek-coder
   curl -X POST http://localhost:11434/api/generate -d '{"model": "deepseek-coder:latest", "prompt": "Hello", "stream": false}'
   
   # Test codellama  
   curl -X POST http://localhost:11434/api/generate -d '{"model": "codellama:latest", "prompt": "Hello", "stream": false}'
   
   # Test mistral
   curl -X POST http://localhost:11434/api/generate -d '{"model": "mistral:latest", "prompt": "Hello", "stream": false}'
   ```

## 🎯 What You've Learned

- **Model Specialization:** Each model has specific strengths
- **Smart Routing:** Keywords automatically select the right model
- **Configuration Over Code:** JSON rules eliminate manual model selection
- **MCP Coordination:** How MCP orchestrates multiple models seamlessly

## 🔗 Next Steps

- Try different question types and see which models get selected
- Modify the routing rules to match your specific needs
- Experiment with combining multiple models for complex questions

**You've just configured your first MCP system! 🎉**
