from fastapi import FastAPI
from routes import router
from config import APP_TITLE, APP_DESCRIPTION, APP_VERSION

# Create FastAPI app
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

# Include API routes
app.include_router(router)

# Add root endpoint
@app.get("/")
def root():
    """
    Root endpoint
    
    Returns basic information about the MCP server.
    """
    return {
        "name": APP_TITLE,
        "version": APP_VERSION,
        "description": APP_DESCRIPTION,
        "docs_url": "/docs"
    }

# Startup event to log server start
@app.on_event("startup")
def startup_event():
    print("Starting MCP Server for Books API...")

# Shutdown event to log server stop
@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down MCP Server...")