# 🚀 Quick Start: MCP Visual Examples

## ⏱️ 1-Hour Complete Setup

### Phase 1: Setup (15 minutes)

**Step 1: Start Ollama Container**
```bash
cd /home/k8s/ai-learning-path/Session-8-MCP-Visual-Examples/resources
docker-compose up -d
```

**Step 2: Download Models**
```bash
# Download models (this takes time - grab coffee! ☕)
docker exec -it ollama-mcp-demo ollama pull llama3.2:3b
docker exec -it ollama-mcp-demo ollama pull codellama:7b-instruct

# Verify installation
docker exec -it ollama-mcp-demo ollama list
```

### Phase 2: Experience "Before MCP" (15 minutes)

**Test Direct Model Calls (The Painful Way):**

```bash
# Test general model
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2:3b",
    "prompt": "Explain Python functions and show examples",
    "stream": false
  }'

# Test code model  
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "codellama:7b-instruct", 
    "prompt": "Explain Python functions and show examples",
    "stream": false
  }'
```

**Notice the problems:**
- ❌ Two separate commands
- ❌ Raw JSON output
- ❌ No coordination between responses
- ❌ Manual work to compare

### Phase 3: Experience "With MCP" (30 minutes)

**Step 1: Install MCP Dependencies**
```bash
cd /home/k8s/ai-learning-path/Session-8-MCP-Visual-Examples
pip install -r resources/requirements.txt
```

**Step 2: Run MCP Server**
```bash
cd hands-on/mcp-server
python simple_mcp_server.py
```

**Step 3: Test MCP Tools**

In another terminal, test the MCP server using the Amazon Q CLI or any MCP-compatible client:

```bash
# Example MCP tool calls (syntax may vary by client)
# These demonstrate the coordinated responses

# Single model with smart routing
ask_single_model("Explain Python functions", "auto")

# Both models with comparison
ask_both_models("Explain Python functions and show examples")

# Complete learning content
create_learning_content("Python functions")
```

## 🎯 The Transformation You'll See

### Before MCP:
```
Raw Response 1: {"response": "Functions are reusable blocks..."}
Raw Response 2: {"response": "def example():\n    return 'hello'"}
```

### After MCP:
```
🎯 COORDINATED RESPONSE:
📚 Concept (llama3.2:3b): "Functions are like recipes..."
💻 Code (codellama:7b): "def greet(name): return f'Hello {name}!'"
🧠 Synthesis: "Notice how the concept matches the code structure..."
✅ Result: Complete understanding in one response!
```

## 🎨 Choose Your Learning Path

### 🎭 **Creative Path**: Story Chain Example
```bash
# Try this with your MCP server:
ask_both_models("Write a story about a robot learning to cook")
# See creative narrative + technical accuracy combined!
```

### 🌍 **Language Path**: Translation + Culture
```bash
ask_both_models("Translate 'I love programming' to Spanish and explain cultural context")
# See translation + cultural insights together!
```

### 💻 **Technical Path**: Code Learning
```bash
create_learning_content("recursion in programming")
# See theory + practice + integration!
```

## 📊 Success Metrics

You'll know MCP is working when you see:

✅ **Coordinated Responses**: Multiple models working together
✅ **Intelligent Routing**: Right model for each task
✅ **Synthesis**: Combined insights, not separate outputs
✅ **Better Quality**: More comprehensive than single model
✅ **Seamless Experience**: Natural conversation, not technical commands

## 🔧 Troubleshooting

**Models not downloading?**
```bash
# Check container logs
docker logs ollama-mcp-demo

# Check available space
df -h
```

**MCP server not starting?**
```bash
# Check Python version (needs 3.8+)
python --version

# Install dependencies again
pip install --upgrade -r resources/requirements.txt
```

**Can't connect to models?**
```bash
# Test Ollama directly
curl http://localhost:11434/api/tags
```

## 🎉 What You've Accomplished

After completing this quick start:

1. ✅ **Experienced the Problem**: Saw manual model coordination pain
2. ✅ **Witnessed the Solution**: MCP's intelligent orchestration  
3. ✅ **Built Working System**: Your own MCP server with dual models
4. ✅ **Understood the Value**: Why MCP matters for AI applications

## 🔗 Next Steps

- Explore more complex MCP patterns
- Add additional models to your setup
- Build custom MCP tools for your specific needs
- Share your MCP creations with others

**Congratulations! You've just experienced the MCP transformation! 🎯**

The difference between "before" and "after" MCP should now be crystal clear. You've seen how MCP turns chaotic manual model coordination into seamless AI orchestration.

Ready to build more advanced MCP applications? The foundation is set! 🚀
