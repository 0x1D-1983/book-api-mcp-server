from fastapi import APIRouter, HTTPException
from models import MCPRequest, MCPResponse, ToolsListResponse, ToolCallResult
from tools import get_tool_implementations, get_tools_list

# Create router
router = APIRouter()

@router.get("/tools", response_model=ToolsListResponse)
def list_tools():
    """
    List all available tools
    
    This endpoint complies with the MCP specification for tool discovery.
    Returns a list of all tools available through this MCP server.
    """
    return ToolsListResponse(tools=get_tools_list())

@router.post("/tool-calls", response_model=MCPResponse)
def process_tool_calls(request: MCPRequest):
    """
    Process tool calls
    
    This endpoint complies with the MCP specification for tool execution.
    It accepts a list of tool calls, executes them, and returns the results.
    """
    results = []
    tool_implementations = get_tool_implementations()
    
    for tool_call in request.tool_calls:
        if tool_call.name not in tool_implementations:
            results.append(ToolCallResult(
                result=None,
                error=f"Unknown tool: {tool_call.name}"
            ))
            continue
            
        # Get the implementation
        implementation = tool_implementations[tool_call.name]
        
        # Execute the tool
        result = implementation(**tool_call.parameters)
        results.append(result)
    
    return MCPResponse(tool_call_results=results)

@router.get("/health")
def health_check():
    """
    Health check endpoint
    
    Returns the status of the MCP server and the number of available tools.
    """
    return {
        "status": "healthy",
        "available_tools": len(get_tools_list())
    }