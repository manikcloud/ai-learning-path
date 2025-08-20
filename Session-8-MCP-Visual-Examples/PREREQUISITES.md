# 📋 Prerequisites Setup Guide for MCP Session

## 🎯 Simple Setup Checklist

Follow this guide to get your system ready for the MCP learning session.

## 🐳 Docker Installation

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
# Download Docker Desktop from: https://docs.docker.com/desktop/mac/install/
# Or using Homebrew:
brew install --cask docker

# Start Docker Desktop application
# Verify in terminal:
docker --version
```

### Windows:
```bash
# Download Docker Desktop from: https://docs.docker.com/desktop/windows/install/
# Or using Chocolatey:
choco install docker-desktop

# Verify in PowerShell/CMD:
docker --version
```

## 🤖 Ollama Setup (Docker Method)

### Run Ollama in Docker Container:
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

## 📥 Download Required AI Models

### Download Models via Docker:
```bash
# Download lightweight models for the demo
docker exec -it ollama ollama pull phi-fast:latest
docker exec -it ollama ollama pull deepseek-coder-fast:latest
docker exec -it ollama ollama pull mistral:latest

# Verify models are downloaded
docker exec -it ollama ollama list
```

### Test Models Are Working:
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

## ✅ Quick Verification

### Simple Verification Commands:
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
1. Navigate to the main [README.md](README.md)
2. Follow the "Three-Step Learning Experience"
3. Experience the MCP transformation!

**Need Help?**
- Check the troubleshooting section above
- Review Docker/Ollama official documentation
- Ensure all prerequisites are met before proceeding
