from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime
# Books API models
class Book(BaseModel):
    """Representation of a book in the database"""
    title: str
    author: str
    isbn: str
    published_date: datetime

# MCP Protocol models
class ToolCallResult(BaseModel):
    """Result of a tool call execution"""
    result: Any
    error: Optional[str] = None

class ToolCallRequest(BaseModel):
    """Request to call a specific tool with parameters"""
    name: str
    parameters: Dict[str, Any]

class ToolDefinition(BaseModel):
    """Definition of a tool available through the MCP server"""
    name: str
    description: str
    input_schema: Dict[str, Any]
    authentication: Optional[Dict[str, Any]] = None

class MCPRequest(BaseModel):
    """Request containing one or more tool calls"""
    tool_calls: List[ToolCallRequest] = Field(default_factory=list)

class MCPResponse(BaseModel):
    """Response containing results of one or more tool calls"""
    tool_call_results: List[ToolCallResult] = Field(default_factory=list)

class ToolsListResponse(BaseModel):
    """Response listing all available tools"""
    tools: List[ToolDefinition] = Field(default_factory=list)