# 📋 Prerequisites Setup Guide for MCP Session

## 🎯 Complete Setup Checklist

Follow this guide step-by-step to ensure your system is ready for the MCP learning session.

## 🐳 Docker Installation & Configuration

### Ubuntu/Debian Systems:
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
docker-compose --version
docker run hello-world
```

### CentOS/RHEL/Fedora:
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

### macOS:
```bash
# Option 1: Download Docker Desktop
# Visit: https://docs.docker.com/desktop/mac/install/

# Option 2: Using Homebrew
brew install --cask docker

# Start Docker Desktop application
# Verify in terminal:
docker --version
docker-compose --version
```

### Windows:
```bash
# Option 1: Download Docker Desktop
# Visit: https://docs.docker.com/desktop/windows/install/

# Option 2: Using Chocolatey
choco install docker-desktop

# Option 3: Using winget
winget install Docker.DockerDesktop

# Verify in PowerShell/CMD:
docker --version
docker-compose --version
```

## 🤖 Ollama Installation & Setup

### Method 1: Direct Installation (Recommended)

**Linux & macOS:**
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama service (runs in background)
ollama serve &

# Verify installation
ollama --version
curl http://localhost:11434/api/tags
```

**Windows:**
```bash
# Download installer from: https://ollama.ai/download/windows
# Or use package managers:

# Using winget:
winget install Ollama.Ollama

# Using Chocolatey:
choco install ollama

# Verify installation:
ollama --version
```

### Method 2: Docker Installation (Alternative)
```bash
# Pull Ollama Docker image
docker pull ollama/ollama:latest

# Run Ollama in Docker
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama:/root/.ollama \
  ollama/ollama

# Verify it's running
docker ps
curl http://localhost:11434/api/tags
```

## 📥 Download Required AI Models

### Download Models Locally:
```bash
# Download lightweight general-purpose model (2GB)
ollama pull llama3.2:3b

# Download code-specialized model (4GB)
ollama pull codellama:7b-instruct

# Alternative smaller models (if memory constrained):
# ollama pull llama3.2:1b        # 1GB - very lightweight
# ollama pull codellama:7b-code  # 3.8GB - smaller code model

# Verify models are downloaded
ollama list
```

### Test Models Are Working:
```bash
# Test general model
ollama run llama3.2:3b "Hello, can you explain what you do?"

# Test code model
ollama run codellama:7b-instruct "Write a simple Python hello world function"

# Quick API test
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2:3b",
    "prompt": "Say hello",
    "stream": false
  }'
```

## 🐍 Python Environment Setup

### Install Python (if not already installed):
```bash
# Ubuntu/Debian:
sudo apt install -y python3 python3-pip python3-venv

# CentOS/RHEL/Fedora:
sudo dnf install -y python3 python3-pip

# macOS (using Homebrew):
brew install python3

# Windows: Download from python.org or use:
winget install Python.Python.3.11
```

### Create Virtual Environment:
```bash
# Create virtual environment
python3 -m venv mcp-learning-env

# Activate virtual environment
# Linux/macOS:
source mcp-learning-env/bin/activate

# Windows:
mcp-learning-env\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install mcp httpx asyncio-mqtt pydantic python-dotenv
```

## ✅ Complete System Verification

### Run This Verification Script:
```bash
#!/bin/bash
echo "🔍 MCP Prerequisites Verification"
echo "================================="

# Check Docker
echo "📦 Checking Docker..."
if command -v docker &> /dev/null; then
    echo "✅ Docker installed: $(docker --version)"
    if docker ps &> /dev/null; then
        echo "✅ Docker is running"
    else
        echo "❌ Docker is not running - start with: sudo systemctl start docker"
    fi
else
    echo "❌ Docker not installed"
fi

# Check Docker Compose
if command -v docker-compose &> /dev/null; then
    echo "✅ Docker Compose installed: $(docker-compose --version)"
else
    echo "❌ Docker Compose not installed"
fi

# Check Ollama
echo "🤖 Checking Ollama..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama installed: $(ollama --version)"
    
    # Check if Ollama service is running
    if curl -s http://localhost:11434/api/tags &> /dev/null; then
        echo "✅ Ollama service is running"
        
        # Check models
        echo "📚 Checking models..."
        if ollama list | grep -q "llama3.2:3b"; then
            echo "✅ llama3.2:3b model available"
        else
            echo "❌ llama3.2:3b model not found - run: ollama pull llama3.2:3b"
        fi
        
        if ollama list | grep -q "codellama:7b-instruct"; then
            echo "✅ codellama:7b-instruct model available"
        else
            echo "❌ codellama:7b-instruct model not found - run: ollama pull codellama:7b-instruct"
        fi
    else
        echo "❌ Ollama service not running - start with: ollama serve"
    fi
else
    echo "❌ Ollama not installed"
fi

# Check Python
echo "🐍 Checking Python..."
if command -v python3 &> /dev/null; then
    echo "✅ Python installed: $(python3 --version)"
else
    echo "❌ Python3 not installed"
fi

# Check system resources
echo "💾 Checking system resources..."
echo "RAM: $(free -h | grep '^Mem:' | awk '{print $2}' 2>/dev/null || echo 'Unable to check')"
echo "Disk: $(df -h . | tail -1 | awk '{print $4}' 2>/dev/null || echo 'Unable to check') available"

echo "================================="
echo "🎯 Prerequisites check complete!"
```

### Save and Run Verification:
```bash
# Save the script
curl -o verify-setup.sh https://raw.githubusercontent.com/manikcloud/ai-learning-path/main/Session-8-MCP-Visual-Examples/verify-setup.sh

# Make executable and run
chmod +x verify-setup.sh
./verify-setup.sh
```

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
# Service not starting:
ollama serve  # Run in foreground to see errors

# Models not downloading:
# Check internet connection
ping ollama.ai

# Check disk space
df -h

# Clear cache and retry
rm -rf ~/.ollama/models/*
ollama pull llama3.2:3b
```

### Memory Issues:
```bash
# If system has < 8GB RAM, use smaller models:
ollama pull llama3.2:1b          # 1GB instead of 3GB
ollama pull codellama:7b-code    # 3.8GB instead of 4GB

# Monitor memory usage:
htop  # or top on basic systems
```

## 📊 Minimum System Requirements

| Component | Minimum | Recommended | Notes |
|-----------|---------|-------------|-------|
| **RAM** | 8GB | 16GB+ | Models load into RAM |
| **Storage** | 10GB free | 20GB+ | For models and Docker images |
| **CPU** | 4 cores | 8+ cores | More cores = faster inference |
| **Internet** | Stable | High-speed | For model downloads (6GB total) |
| **OS** | Linux/macOS/Windows | Linux preferred | Better Docker support |

## 🎯 Ready to Proceed?

Once all items show ✅ in the verification script, you're ready to start the MCP learning session!

**Next Steps:**
1. Navigate to the main README.md
2. Follow the "Three-Step Learning Experience"
3. Experience the MCP transformation!

**Need Help?**
- Check the troubleshooting section above
- Review Docker/Ollama official documentation
- Ensure all prerequisites are met before proceeding
