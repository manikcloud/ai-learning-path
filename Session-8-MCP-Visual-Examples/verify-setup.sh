#!/bin/bash

# MCP Prerequisites Verification Script
# This script checks if your system is ready for the MCP learning session

echo "🔍 MCP Prerequisites Verification"
echo "================================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
PASSED=0
FAILED=0

# Function to print success
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
    ((PASSED++))
}

# Function to print failure
print_failure() {
    echo -e "${RED}❌ $1${NC}"
    ((FAILED++))
}

# Function to print warning
print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check Docker installation
echo "📦 Checking Docker..."
if command -v docker &> /dev/null; then
    DOCKER_VERSION=$(docker --version 2>/dev/null)
    print_success "Docker installed: $DOCKER_VERSION"
    
    # Check if Docker is running
    if docker ps &> /dev/null; then
        print_success "Docker daemon is running"
        
        # Test Docker with hello-world
        if docker run --rm hello-world &> /dev/null; then
            print_success "Docker is working correctly"
        else
            print_failure "Docker test failed - check permissions"
        fi
    else
        print_failure "Docker daemon not running - start with: sudo systemctl start docker"
    fi
else
    print_failure "Docker not installed - install from https://docker.com"
fi

# Check Docker Compose
echo ""
echo "🔧 Checking Docker Compose..."
if command -v docker-compose &> /dev/null; then
    COMPOSE_VERSION=$(docker-compose --version 2>/dev/null)
    print_success "Docker Compose installed: $COMPOSE_VERSION"
else
    print_failure "Docker Compose not installed"
fi

# Check Ollama installation
echo ""
echo "🤖 Checking Ollama..."
if command -v ollama &> /dev/null; then
    OLLAMA_VERSION=$(ollama --version 2>/dev/null)
    print_success "Ollama installed: $OLLAMA_VERSION"
    
    # Check if Ollama service is running
    if curl -s http://localhost:11434/api/tags &> /dev/null; then
        print_success "Ollama service is running on port 11434"
        
        # Check available models
        echo ""
        echo "📚 Checking AI models..."
        MODELS=$(ollama list 2>/dev/null)
        
        if echo "$MODELS" | grep -q "llama3.2:3b"; then
            print_success "llama3.2:3b model available"
        else
            print_failure "llama3.2:3b model not found - run: ollama pull llama3.2:3b"
        fi
        
        if echo "$MODELS" | grep -q "codellama:7b-instruct"; then
            print_success "codellama:7b-instruct model available"
        else
            print_failure "codellama:7b-instruct model not found - run: ollama pull codellama:7b-instruct"
        fi
        
        # Test model response
        echo ""
        echo "🧪 Testing model responses..."
        TEST_RESPONSE=$(curl -s -X POST http://localhost:11434/api/generate \
            -H "Content-Type: application/json" \
            -d '{"model": "llama3.2:3b", "prompt": "Hello", "stream": false}' 2>/dev/null)
        
        if echo "$TEST_RESPONSE" | grep -q "response"; then
            print_success "Models are responding correctly"
        else
            print_warning "Models installed but not responding - may need time to load"
        fi
        
    else
        print_failure "Ollama service not running - start with: ollama serve"
    fi
else
    print_failure "Ollama not installed - install from https://ollama.ai"
fi

# Check Python installation
echo ""
echo "🐍 Checking Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>/dev/null)
    print_success "Python installed: $PYTHON_VERSION"
    
    # Check Python version (need 3.8+)
    PYTHON_MAJOR=$(python3 -c "import sys; print(sys.version_info.major)" 2>/dev/null)
    PYTHON_MINOR=$(python3 -c "import sys; print(sys.version_info.minor)" 2>/dev/null)
    
    if [[ $PYTHON_MAJOR -eq 3 && $PYTHON_MINOR -ge 8 ]]; then
        print_success "Python version is compatible (3.8+ required)"
    else
        print_failure "Python version too old - need Python 3.8 or higher"
    fi
    
    # Check pip
    if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
        print_success "pip is available"
    else
        print_failure "pip not found - install with: sudo apt install python3-pip"
    fi
    
else
    print_failure "Python3 not installed"
fi

# Check system resources
echo ""
echo "💾 Checking system resources..."

# Check RAM
if command -v free &> /dev/null; then
    TOTAL_RAM=$(free -m | grep '^Mem:' | awk '{print $2}')
    if [[ $TOTAL_RAM -gt 8000 ]]; then
        print_success "RAM: ${TOTAL_RAM}MB (sufficient for MCP session)"
    elif [[ $TOTAL_RAM -gt 4000 ]]; then
        print_warning "RAM: ${TOTAL_RAM}MB (minimum met, but 8GB+ recommended)"
    else
        print_failure "RAM: ${TOTAL_RAM}MB (insufficient - need at least 4GB, 8GB+ recommended)"
    fi
else
    print_warning "Cannot check RAM - ensure you have at least 8GB"
fi

# Check disk space
AVAILABLE_SPACE=$(df -BG . | tail -1 | awk '{print $4}' | sed 's/G//')
if [[ $AVAILABLE_SPACE -gt 15 ]]; then
    print_success "Disk space: ${AVAILABLE_SPACE}GB available (sufficient)"
elif [[ $AVAILABLE_SPACE -gt 10 ]]; then
    print_warning "Disk space: ${AVAILABLE_SPACE}GB available (minimum met)"
else
    print_failure "Disk space: ${AVAILABLE_SPACE}GB available (need at least 10GB)"
fi

# Check network connectivity
echo ""
echo "🌐 Checking network connectivity..."
if ping -c 1 ollama.ai &> /dev/null; then
    print_success "Network connectivity to ollama.ai working"
else
    print_failure "Cannot reach ollama.ai - check internet connection"
fi

if ping -c 1 github.com &> /dev/null; then
    print_success "Network connectivity to github.com working"
else
    print_failure "Cannot reach github.com - check internet connection"
fi

# Summary
echo ""
echo "================================="
echo "📊 VERIFICATION SUMMARY"
echo "================================="
echo -e "${GREEN}✅ Passed: $PASSED${NC}"
echo -e "${RED}❌ Failed: $FAILED${NC}"
echo ""

if [[ $FAILED -eq 0 ]]; then
    echo -e "${GREEN}🎉 ALL PREREQUISITES MET!${NC}"
    echo "You're ready to start the MCP learning session!"
    echo ""
    echo "Next steps:"
    echo "1. Navigate to the main README.md"
    echo "2. Follow the 'Three-Step Learning Experience'"
    echo "3. Experience the MCP transformation!"
elif [[ $FAILED -le 2 ]]; then
    echo -e "${YELLOW}⚠️  MOSTLY READY${NC}"
    echo "You have minor issues that should be resolved before starting."
    echo "Check the failed items above and follow the suggested solutions."
elif [[ $FAILED -le 5 ]]; then
    echo -e "${YELLOW}🔧 SETUP NEEDED${NC}"
    echo "Several prerequisites need attention before starting the session."
    echo "Please resolve the failed items and run this script again."
else
    echo -e "${RED}🚫 SIGNIFICANT SETUP REQUIRED${NC}"
    echo "Multiple prerequisites are missing. Please:"
    echo "1. Review the PREREQUISITES.md file"
    echo "2. Install missing components"
    echo "3. Run this verification script again"
fi

echo ""
echo "For detailed setup instructions, see: PREREQUISITES.md"
echo "For help, check the troubleshooting section in the documentation."
