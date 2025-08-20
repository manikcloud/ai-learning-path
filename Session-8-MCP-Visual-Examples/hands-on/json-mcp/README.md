# JSON MCP Configuration - Complete Setup & Demo

## 🎯 What You'll Build

A simple JSON-based MCP configuration that automatically routes questions to the right models without any programming.

---

## 📋 Prerequisites Setup

### 🐳 Docker Installation

#### Ubuntu/Debian Systems:
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Docker and Docker Compose
sudo apt install -y docker.io docker-compose curl

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add current user to docker group
sudo usermod -aG docker $USER

# Apply group changes (logout/login or use newgrp)
newgrp docker

# Verify Docker installation
docker --version
docker run hello-world
```

#### CentOS/RHEL/Fedora:
```bash
# Install Docker
sudo dnf install -y docker docker-compose

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
docker run hello-world
```

#### macOS:
```bash
# Download Docker Desktop from: https://docs.docker.com/desktop/mac/install/
# Or using Homebrew:
brew install --cask docker

# Start Docker Desktop application
# Verify in terminal:
docker --version
```

#### Windows:
```bash
# Download Docker Desktop from: https://docs.docker.com/desktop/windows/install/
# Or using Chocolatey:
choco install docker-desktop

# Verify in PowerShell/CMD:
docker --version
```

### 🤖 Ollama Setup (Docker Method)

#### Run Ollama in Docker Container:
```bash
# Pull and run Ollama Docker container
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama:/root/.ollama \
  ollama/ollama

# Verify it's running
docker ps
curl http://localhost:11434/api/tags
```

### 📥 Download Required AI Models

#### Download Models via Docker:
```bash
# Download lightweight models for the demo
docker exec -it ollama ollama pull phi-fast:latest
docker exec -it ollama ollama pull deepseek-coder-fast:latest
docker exec -it ollama ollama pull mistral:latest

# Verify models are downloaded
docker exec -it ollama ollama list
```

#### Test Models Are Working:
```bash
# Test general model
docker exec -it ollama ollama run phi-fast:latest "Hello, can you help with travel planning?"

# Test code model
docker exec -it ollama ollama run deepseek-coder-fast:latest "Write a simple Python function"

# Quick API test
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-fast:latest",
    "prompt": "Say hello",
    "stream": false
  }'
```

### ✅ Quick Verification

#### Simple Verification Commands:
```bash
# 1. Check Docker is running
docker ps

# 2. Check Ollama container is running  
docker ps | grep ollama

# 3. Check Ollama API is responding
curl http://localhost:11434/api/tags

# 4. Check models are available
docker exec ollama ollama list

# 5. Test a model works
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "phi-fast:latest", "prompt": "Hello", "stream": false}'
```

**If all commands return successful responses, you're ready!**

---

## 📁 Files Overview

- **`smart-mcp.json`** - MCP routing configuration with smart model selection rules
- **`smart_chat.py`** - CLI script that demonstrates automatic model routing

---

## 🚀 How to Use

### **Step 1: Review the Configuration**
```bash
# Look at your MCP routing setup
cat smart-mcp.json

# Check the smart chat script
cat smart_chat.py
```

### **Step 2: Test Smart Model Selection**

**Travel Question (routes to phi-fast:latest):**
```bash
python3 smart_chat.py "What's the best time to visit Paris?"
```

**Coding Question (routes to deepseek-coder-fast:latest):**
```bash
python3 smart_chat.py "Write a Python function to sort a list"
```

**General Question (routes to mistral:latest):**
```bash
python3 smart_chat.py "Explain what machine learning is"
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

---

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
| **Travel** | trip, travel, visit, vacation, plan | phi-fast:latest | General model good for travel |
| **Coding** | function, code, programming, debug | deepseek-coder-fast:latest | Specialized coding model |
| **General** | explain, what is, how to | mistral:latest | Good for explanations |

---

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

---

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

---

## 🚨 Common Issues & Solutions

### Docker Issues:
```bash
# Permission denied error:
sudo usermod -aG docker $USER
newgrp docker

# Docker daemon not running:
sudo systemctl start docker

# Port conflicts:
sudo lsof -i :11434  # Check what's using port 11434
```

### Ollama Issues:
```bash
# Container not starting:
docker logs ollama  # Check container logs

# Models not downloading:
# Check internet connection and disk space
docker exec -it ollama ollama pull phi-fast:latest

# Clear cache and retry:
docker stop ollama
docker rm ollama
docker volume rm ollama
# Then run the docker run command again
```

---

## 📊 Minimum System Requirements

| Component | Minimum | Recommended | Notes |
|-----------|---------|-------------|-------|
| **RAM** | 8GB | 16GB+ | Models load into RAM |
| **Storage** | 10GB free | 20GB+ | For models and Docker images |
| **CPU** | 4 cores | 8+ cores | More cores = faster inference |
| **Internet** | Stable | High-speed | For model downloads (6GB total) |
| **OS** | Linux/macOS/Windows | Linux preferred | Better Docker support |

---

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
