import uvicorn
from config import get_server_host, get_server_port

def main():
    """Start the MCP server"""
    host = get_server_host()
    port = get_server_port()
    
    print(f"Starting MCP Server on {host}:{port}")
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True
    )

if __name__ == "__main__":
    main()