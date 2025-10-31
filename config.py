import os

# Server configuration
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8080  # Default to port 8080

# Application settings
APP_TITLE = "MCP Server for Books API"
APP_DESCRIPTION = "Model Context Protocol server that exposes a Books API for use by AI assistants"
APP_VERSION = "1.0.0"

def get_server_host() -> str:
    """Get the server host from environment variable or use default"""
    return os.getenv("MCP_SERVER_HOST", DEFAULT_HOST)

def get_server_port() -> int:
    """Get the server port from environment variable or use default"""
    port_str = os.getenv("MCP_SERVER_PORT", str(DEFAULT_PORT))
    try:
        return int(port_str)
    except ValueError:
        return DEFAULT_PORT