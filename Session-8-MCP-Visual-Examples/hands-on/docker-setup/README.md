# Docker Setup for MCP + Ollama

## 🎯 Goal
Set up Ollama in Docker with two different models to demonstrate MCP coordination.

## 📋 Prerequisites
- Docker installed and running
- At least 8GB RAM available
- Internet connection for model downloads

## 🚀 Quick Setup

### Step 1: Create Docker Compose File

```yaml
# docker-compose.yml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama-mcp-demo
    ports:
      - "11434:11434"
    volumes:
      - ollama-data:/root/.ollama
    environment:
      - OLLAMA_HOST=0.0.0.0
    restart: unless-stopped
    # Uncomment for GPU support (NVIDIA)
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: 1
    #           capabilities: [gpu]

volumes:
  ollama-data:
    driver: local
```

### Step 2: Start Ollama Container

```bash
# Start the container
docker-compose up -d

# Check if it's running
docker ps

# Check logs
docker logs ollama-mcp-demo
```

### Step 3: Download Models

```bash
# Download general purpose model (fast, good for explanations)
docker exec -it ollama-mcp-demo ollama pull llama3.2:3b

# Download code-focused model (better for programming)
docker exec -it ollama-mcp-demo ollama pull codellama:7b-instruct

# Verify models are installed
docker exec -it ollama-mcp-demo ollama list
```

## 🧪 Test Your Setup

### Test Model 1 (General Purpose):
```bash
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2:3b",
    "prompt": "Explain what a function is in simple terms",
    "stream": false
  }'
```

### Test Model 2 (Code Focused):
```bash
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "codellama:7b-instruct",
    "prompt": "Write a simple Python function example",
    "stream": false
  }'
```

## 📊 Model Comparison

| Model | Size | Strengths | Best For |
|-------|------|-----------|----------|
| llama3.2:3b | ~2GB | Explanations, conversations | Theory, concepts, general questions |
| codellama:7b-instruct | ~4GB | Code generation, technical accuracy | Programming, technical documentation |

## 🔧 Troubleshooting

### Common Issues:

**1. Port Already in Use:**
```bash
# Check what's using port 11434
sudo lsof -i :11434

# Kill the process or change port in docker-compose.yml
```

**2. Out of Memory:**
```bash
# Check available memory
free -h

# Use smaller models if needed:
docker exec -it ollama-mcp-demo ollama pull llama3.2:1b
docker exec -it ollama-mcp-demo ollama pull codellama:7b-code  # smaller variant
```

**3. Slow Model Downloads:**
```bash
# Check download progress
docker exec -it ollama-mcp-demo ollama ps

# Resume interrupted downloads
docker exec -it ollama-mcp-demo ollama pull <model-name>
```

## 🎯 Verification Checklist

Before proceeding to MCP setup, ensure:

- [ ] Docker container is running
- [ ] Port 11434 is accessible
- [ ] Both models are downloaded
- [ ] Both models respond to test queries
- [ ] No error messages in logs

## 🔗 Next Steps

Once your Docker setup is working:
1. Move to the MCP server setup
2. Build your first MCP coordination example
3. Experience the before/after transformation!

Your Ollama models are now ready to be orchestrated by MCP! 🎉
