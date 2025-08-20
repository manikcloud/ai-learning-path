#!/usr/bin/env python3
"""
Simple MCP Server for Dual Model Coordination
Demonstrates the power of MCP by coordinating two Ollama models
"""

import asyncio
import json
import logging
from typing import Any, Dict, List, Optional
import httpx
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dual-model-mcp")

class DualModelMCP:
    """MCP Server that coordinates two Ollama models"""
    
    def __init__(self):
        self.ollama_base_url = "http://localhost:11434"
        self.models = {
            "general": "llama3.2:3b",      # Better for explanations
            "code": "codellama:7b-instruct" # Better for code
        }
        
    async def call_ollama(self, model: str, prompt: str) -> str:
        """Call Ollama API with specified model"""
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    f"{self.ollama_base_url}/api/generate",
                    json={
                        "model": model,
                        "prompt": prompt,
                        "stream": False
                    }
                )
                response.raise_for_status()
                result = response.json()
                return result.get("response", "No response received")
        except Exception as e:
            logger.error(f"Error calling Ollama: {e}")
            return f"Error: {str(e)}"
    
    async def smart_route(self, question: str) -> str:
        """Intelligently route question to best model"""
        code_keywords = ["function", "code", "programming", "python", "javascript", 
                        "algorithm", "debug", "syntax", "class", "method"]
        
        question_lower = question.lower()
        if any(keyword in question_lower for keyword in code_keywords):
            return "code"
        return "general"
    
    async def ask_single_model(self, question: str, model_type: str = "auto") -> Dict[str, Any]:
        """Ask a single model"""
        if model_type == "auto":
            model_type = await self.smart_route(question)
        
        model_name = self.models.get(model_type, self.models["general"])
        response = await self.call_ollama(model_name, question)
        
        return {
            "model_used": model_name,
            "model_type": model_type,
            "response": response,
            "routing_reason": f"Selected {model_type} model for this type of question"
        }
    
    async def ask_both_models(self, question: str) -> Dict[str, Any]:
        """Ask both models and compare responses"""
        # Call both models concurrently
        general_task = self.call_ollama(self.models["general"], question)
        code_task = self.call_ollama(self.models["code"], question)
        
        general_response, code_response = await asyncio.gather(general_task, code_task)
        
        # Create synthesis
        synthesis_prompt = f"""
        Compare these two responses to the question: "{question}"
        
        Response 1 (General Model): {general_response}
        Response 2 (Code Model): {code_response}
        
        Provide a brief synthesis highlighting:
        1. Key similarities
        2. Unique insights from each
        3. Which response is better for what purpose
        """
        
        synthesis = await self.call_ollama(self.models["general"], synthesis_prompt)
        
        return {
            "question": question,
            "responses": {
                "general_model": {
                    "model": self.models["general"],
                    "response": general_response
                },
                "code_model": {
                    "model": self.models["code"], 
                    "response": code_response
                }
            },
            "synthesis": synthesis,
            "recommendation": "Use both responses for comprehensive understanding"
        }
    
    async def create_learning_content(self, topic: str) -> Dict[str, Any]:
        """Create comprehensive learning content using both models"""
        
        # Get conceptual explanation from general model
        concept_prompt = f"Explain {topic} in simple, easy-to-understand terms with analogies and examples"
        concept_response = await self.call_ollama(self.models["general"], concept_prompt)
        
        # Get practical examples from code model
        practical_prompt = f"Provide practical code examples and implementation details for {topic}"
        practical_response = await self.call_ollama(self.models["code"], practical_prompt)
        
        # Create integrated learning content
        integration_prompt = f"""
        Create a comprehensive learning guide that combines:
        
        Conceptual Understanding: {concept_response}
        Practical Implementation: {practical_response}
        
        Structure this as a complete learning resource with:
        1. Clear explanation
        2. Practical examples
        3. Key takeaways
        """
        
        integrated_content = await self.call_ollama(self.models["general"], integration_prompt)
        
        return {
            "topic": topic,
            "learning_components": {
                "concept": concept_response,
                "practice": practical_response,
                "integrated": integrated_content
            },
            "learning_path": "Concept → Practice → Integration",
            "models_used": list(self.models.values())
        }

# Initialize MCP Server
server = Server("dual-model-coordinator")
dual_model = DualModelMCP()

@server.list_tools()
async def handle_list_tools() -> List[Tool]:
    """List available MCP tools"""
    return [
        Tool(
            name="ask_single_model",
            description="Ask a single AI model (auto-selects best model or specify type)",
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "The question to ask"
                    },
                    "model_type": {
                        "type": "string", 
                        "enum": ["general", "code", "auto"],
                        "description": "Which model to use (auto = smart routing)",
                        "default": "auto"
                    }
                },
                "required": ["question"]
            }
        ),
        Tool(
            name="ask_both_models",
            description="Ask both models and get comparative analysis",
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "The question to ask both models"
                    }
                },
                "required": ["question"]
            }
        ),
        Tool(
            name="create_learning_content",
            description="Create comprehensive learning content using both models",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The topic to create learning content for"
                    }
                },
                "required": ["topic"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls"""
    try:
        if name == "ask_single_model":
            result = await dual_model.ask_single_model(
                arguments["question"],
                arguments.get("model_type", "auto")
            )
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
        
        elif name == "ask_both_models":
            result = await dual_model.ask_both_models(arguments["question"])
            return [TextContent(
                type="text", 
                text=json.dumps(result, indent=2)
            )]
        
        elif name == "create_learning_content":
            result = await dual_model.create_learning_content(arguments["topic"])
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
        
        else:
            raise ValueError(f"Unknown tool: {name}")
            
    except Exception as e:
        logger.error(f"Error in tool {name}: {e}")
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}"
        )]

async def main():
    """Run the MCP server"""
    logger.info("Starting Dual Model MCP Server...")
    logger.info(f"Available models: {dual_model.models}")
    
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="dual-model-coordinator",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=None,
                    experimental_capabilities=None,
                )
            )
        )

if __name__ == "__main__":
    asyncio.run(main())
