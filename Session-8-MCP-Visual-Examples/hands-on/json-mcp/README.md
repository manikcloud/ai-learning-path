# JSON MCP Configuration Setup

## 🎯 What You'll Build

A simple JSON-based MCP configuration that automatically routes questions to the right models without any programming.

## 📁 Files Overview

- **`smart-mcp.json`** - MCP routing configuration with smart model selection rules
- **`smart_chat.py`** - CLI script that demonstrates automatic model routing
- **`mcp`** - Simple MCP command wrapper

## 🚀 How to Use

### Step 1: Review the Configuration
```bash
# Look at your MCP routing setup
cat smart-mcp.json

# Check the smart chat script
cat smart_chat.py
```

### Step 2: Test Smart Model Selection

**Travel Question (should select phi-fast:latest):**
```bash
python3 smart_chat.py "What's the best time to visit Paris?"
```

**Coding Question (should select deepseek-coder-fast:latest):**
```bash
python3 smart_chat.py "Write a Python function to sort a list"
```

### **Step 3: Experience the Before vs After Transformation**
```bash
# First: Try manual model selection (the problem)
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "deepseek-coder-fast:latest", "prompt": "Plan a trip to Paris", "stream": false}'
# Result: ❌ Model refuses with "not suitable for travel itineraries"

# Then: Use MCP smart selection (the solution)  
python3 smart_chat.py "Plan a trip to Paris"
# Result: ✅ Helpful travel planning response
```

## 🎯 Understanding the Magic

**Before MCP (Manual Selection):**
```bash
# Student manually tries different models - often gets wrong results
curl -X POST http://localhost:11434/api/generate \
  -d '{"model": "deepseek-coder-fast:latest", "prompt": "Plan a trip to Paris"}'
# Result: ❌ "I'm sorry... not suitable for travel itineraries"
```

**After MCP (Smart Selection):**
```bash
# MCP automatically analyzes and selects the right model
python3 smart_chat.py "Plan a trip to Paris"
# Result: ✅ Helpful travel planning response
```

## 🧠 How Smart Routing Works

The `smart-mcp.json` file contains routing rules:

| Question Type | Keywords | Selected Model | Why |
|---------------|----------|----------------|-----|
| **Travel** | trip, travel, visit, vacation | phi-fast:latest | General model good for travel |
| **Coding** | function, code, programming | deepseek-coder-fast:latest | Specialized coding model |
| **General** | explain, what is, how to | mistral:latest | Good for explanations |

## 🎨 Customization

### Add New Routing Rules
Edit `smart-mcp.json` to add new question types:

```json
"new_question_type": {
  "keywords": ["your", "custom", "keywords"],
  "use_model": "your-preferred-model:latest",
  "avoid_model": "model-to-avoid:latest"
}
```

## 🧪 Testing Your Setup

1. **Verify Models Available:**
   ```bash
   curl http://localhost:11434/api/tags
   ```

2. **Test Individual Models:**
   ```bash
   # Test phi-fast
   curl -X POST http://localhost:11434/api/generate \
     -d '{"model": "phi-fast:latest", "prompt": "Hello", "stream": false}'
   
   # Test deepseek-coder-fast
   curl -X POST http://localhost:11434/api/generate \
     -d '{"model": "deepseek-coder-fast:latest", "prompt": "Hello", "stream": false}'
   ```

3. **Test Smart Routing:**
   ```bash
   # Different question types should route to different models
   python3 smart_chat.py "Plan a vacation"        # → phi-fast
   python3 smart_chat.py "Write a function"       # → deepseek-coder-fast
   python3 smart_chat.py "Explain recursion"      # → mistral
   ```

## 🎯 What You've Learned

- **Model Specialization:** Each model has specific strengths and weaknesses
- **Smart Routing:** Keywords automatically select the appropriate model
- **MCP Value:** Eliminates manual model selection and wrong choices
- **Automatic Coordination:** One question, right model, helpful response

## 🔗 Next Steps

- Try different question types and observe model selection
- Modify routing rules to match your specific needs
- Experiment with new models and routing strategies
- Experience the transformation from manual guessing to intelligent automation

**You've successfully built and tested an MCP-inspired smart routing system!** 🎉
