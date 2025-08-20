#!/bin/bash

QUESTION="Plan a 3-day trip to Paris for a family with kids"

echo "🎯 MCP DEMONSTRATION: Before vs After"
echo "====================================="
echo ""
echo "📝 Question: '$QUESTION'"
echo ""

echo "❌ BEFORE MCP (Manual Model Selection):"
echo "   Student command: curl ... deepseek-coder-fast ..."
echo "   Result:"
curl -s -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"deepseek-coder-fast:latest\", \"prompt\": \"$QUESTION\", \"stream\": false}" \
  | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    response = data.get('response', 'No response')
    print('   \"' + response[:100] + '...\"')
except:
    print('   Error getting response')
"

echo ""
echo "   ❌ Problem: Wrong model choice, wasted time!"
echo ""

echo "✅ AFTER MCP (Automatic Selection):"
echo "   Student command: ./mcp \"$QUESTION\""
echo "   MCP automatically:"
echo "   ✓ Analyzes question keywords"
echo "   ✓ Selects appropriate model (phi-fast:latest)"
echo "   ✓ Gets helpful response immediately"
echo ""

echo "🎯 KEY BENEFIT:"
echo "   Before: Manual guessing → Often wrong → Frustration"
echo "   After: MCP intelligence → Always right → Success"
