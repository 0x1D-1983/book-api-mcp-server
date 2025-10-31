from services import BookService
from models import ToolDefinition
from typing import Dict, Callable, List, Any

# Define tool schemas to expose through MCP
TOOLS = [
    ToolDefinition(
        name="list_books",
        description="Retrieve all books from the database",
        input_schema={
            "type": "object",
            "properties": {},
            "required": []
        }
    ),
    ToolDefinition(
        name="create_book",
        description="Create a new book in the database",
        input_schema={
            "type": "object",
            "properties": {
                "book_data": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "Unique identifier for the book"},
                        "title": {"type": "string", "description": "Title of the book"},
                        "author": {"type": "string", "description": "Author of the book"},
                        "isbn": {"type": "string", "description": "ISBN of the book"},
                        "publishedDate": {"type": "string", "description": "Published date of the book in ISO 8601 UTC format (must end with 'Z', e.g., '2024-04-11T00:00:00Z')"}
                    },
                    "required": ["title", "author"]
                }
            },
            "required": ["book_data"]
        }
    ),
    ToolDefinition(
        name="get_book",
        description="Retrieve a book by ID",
        input_schema={
            "type": "object",
            "properties": {
                "book_id": {"type": "integer", "description": "ID of the book to retrieve"}
            },
            "required": ["book_id"]
        }
    ),
    ToolDefinition(
        name="update_book",
        description="Update an existing book",
        input_schema={
            "type": "object",
            "properties": {
                "book_id": {"type": "integer", "description": "ID of the book to update"},
                "book_data": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "ID of the book (must match book_id)"},
                        "title": {"type": "string", "description": "New title of the book"},
                        "author": {"type": "string", "description": "New author of the book"},
                        "isbn": {"type": "string", "description": "New ISBN of the book"},
                        "publishedDate": {"type": "string", "description": "New published date of the book (ISO 8601 format)"}
                    }
                }
            },
            "required": ["book_id", "book_data"]
        }
    ),
    ToolDefinition(
        name="delete_book",
        description="Delete a book by ID",
        input_schema={
            "type": "object",
            "properties": {
                "book_id": {"type": "integer", "description": "ID of the book to delete"}
            },
            "required": ["book_id"]
        }
    )
]

# Map tool names to their implementation methods
TOOL_IMPLEMENTATIONS = {
    "list_books": BookService.list_books,
    "create_book": BookService.create_book,
    "get_book": BookService.get_book,
    "update_book": BookService.update_book,
    "delete_book": BookService.delete_book
}

def get_tool_implementations() -> Dict[str, Callable]:
    """
    Get the mapping of tool names to their implementation methods
    
    Returns:
        A dictionary mapping tool names to their implementation methods
    """
    return TOOL_IMPLEMENTATIONS

def get_tools_list() -> List[ToolDefinition]:
    """
    Get the list of available tools
    
    Returns:
        A list of tool definitions
    """
    return TOOLS