# Books API MCP Server

A Model Context Protocol (MCP) server that exposes book management tools for AI assistants. This server provides a bridge between AI applications and a .NET Books API, enabling seamless book collection management through standardized MCP tool calls.

The .NET Book API backend that this MCP server interacts with is available at: [https://github.com/0x1D-1983/book-api](https://github.com/0x1D-1983/book-api).


## Features

- **MCP Protocol Support**: Implements Model Context Protocol for tool discovery and execution
- **RESTful API Integration**: Connects to a .NET Books API backend
- **Comprehensive CRUD Operations**: Full Create, Read, Update, and Delete functionality for books
- **FastAPI Framework**: Modern, fast, and easy-to-maintain Python web framework
- **Type-Safe Models**: Uses Pydantic for robust data validation
- **Error Handling**: Comprehensive error handling with clear error messages

## Available Tools

The MCP server exposes the following tools:

### 1. `list_books`

Retrieve all books from the database.

**Parameters:**
- None

**Returns:**
- Array of book objects with the following fields:
  - `id` (integer): Unique book identifier
  - `title` (string): Book title
  - `author` (string): Book author
  - `isbn` (string): International Standard Book Number
  - `publishedDate` (string): Publication date in ISO 8601 format
  - `createdAt` (string): Record creation timestamp

**Example Usage:**
```python
result = BookService.list_books()
# Returns: List of all books in the database
```

---

### 2. `get_book`

Retrieve a specific book by its ID.

**Parameters:**
- `book_id` (integer, required): The unique identifier of the book to retrieve

**Returns:**
- Book object with full details, or error if book not found

**Example Usage:**
```python
result = BookService.get_book(1)
# Returns: Book with ID 1
```

---

### 3. `create_book`

Create a new book in the database.

**Parameters:**
- `book_data` (object, required): Book information object containing:
  - `id` (integer, optional): Unique identifier for the book
  - `title` (string, required): Title of the book
  - `author` (string, required): Author of the book
  - `isbn` (string, optional): ISBN of the book
  - `publishedDate` (string, optional): Publication date in **ISO 8601 UTC format** (must end with 'Z', e.g., `2024-04-11T00:00:00Z`)

**Returns:**
- Created book object with all fields including generated `createdAt` timestamp

**Example Usage:**
```python
book_data = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "isbn": "978-0743273565",
    "publishedDate": "1925-04-10T00:00:00Z"
}
result = BookService.create_book(book_data)
```

**Important:** The `publishedDate` field must be in ISO 8601 UTC format ending with 'Z' to ensure PostgreSQL compatibility.

---

### 4. `update_book`

Update an existing book's information.

**Parameters:**
- `book_id` (integer, required): The unique identifier of the book to update
- `book_data` (object, required): Updated book information object containing:
  - `id` (integer): ID of the book (must match `book_id`)
  - `title` (string, optional): New title
  - `author` (string, optional): New author
  - `isbn` (string, optional): New ISBN
  - `publishedDate` (string, optional): New publication date in **ISO 8601 UTC format** (must end with 'Z')

**Returns:**
- Success message if update was successful, or error if book not found

**Example Usage:**
```python
book_data = {
    "id": 1,
    "title": "Updated Title",
    "author": "Updated Author",
    "isbn": "978-1234567890",
    "publishedDate": "2023-01-01T00:00:00Z"
}
result = BookService.update_book(1, book_data)
```

---

### 5. `delete_book`

Delete a book from the database.

**Parameters:**
- `book_id` (integer, required): The unique identifier of the book to delete

**Returns:**
- Success message if deletion was successful, or error if book not found

**Example Usage:**
```python
result = BookService.delete_book(1)
# Returns: Success message confirming deletion
```

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Access to a running Books API instance (default: `http://localhost:5288`)
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd book-api-mcp-server
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn requests pydantic
   ```

   Or if you have a `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Books API URL:**
   
   Edit `services.py` and update the `BOOKS_API_URL` constant if your Books API is running on a different host/port:
   ```python
   BOOKS_API_URL = "http://localhost:5288"  # Update as needed
   ```

5. **Run the server:**
   ```bash
   python run.py
   ```

   The server will start on `http://0.0.0.0:8080` by default.

   You can customize the host and port using environment variables:
   ```bash
   export MCP_SERVER_HOST=localhost
   export MCP_SERVER_PORT=8080
   python run.py
   ```

### Testing the Server

1. **Check server health:**
   ```bash
   curl http://localhost:8080/health
   ```

2. **List available tools:**
   ```bash
   curl http://localhost:8080/tools
   ```

3. **Run the test suite:**
   ```bash
   python test_tools.py
   ```

---

## Configuration

### Environment Variables

- `MCP_SERVER_HOST`: Server host address (default: `0.0.0.0`)
- `MCP_SERVER_PORT`: Server port number (default: `8080`)
- `BOOKS_API_URL`: Base URL of the Books API (configured in `services.py`, default: `http://localhost:5288`)

### Cursor Integration

To use this MCP server with Cursor, add the following to your `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "books-api": {
      "command": "python3",
      "args": ["/path/to/book-api-mcp-server/run.py"]
    }
  }
}
```

**Note:** Restart Cursor after updating the MCP configuration for changes to take effect.

---

## API Endpoints

The MCP server exposes the following HTTP endpoints:

- `GET /`: Root endpoint with server information
- `GET /tools`: List all available MCP tools
- `POST /tool-calls`: Execute one or more tool calls
- `GET /health`: Health check endpoint
- `GET /docs`: Interactive API documentation (FastAPI Swagger UI)

---

## Usage Examples

### Using Python Client

```python
from services import BookService
import json

# List all books
books = BookService.list_books()
print(json.dumps(books.result, indent=2))

# Get a specific book
book = BookService.get_book(1)
print(json.dumps(book.result, indent=2))

# Create a new book
new_book = {
    "title": "1984",
    "author": "George Orwell",
    "isbn": "978-0451524935",
    "publishedDate": "1949-06-08T00:00:00Z"
}
result = BookService.create_book(new_book)
print(json.dumps(result.result, indent=2))

# Update a book
updated_data = {
    "id": 1,
    "title": "Nineteen Eighty-Four",
    "author": "George Orwell"
}
result = BookService.update_book(1, updated_data)

# Delete a book
result = BookService.delete_book(1)
```

### Using HTTP API

```bash
# List all tools
curl http://localhost:8080/tools

# Call a tool
curl -X POST http://localhost:8080/tool-calls \
  -H "Content-Type: application/json" \
  -d '{
    "tool_calls": [
      {
        "name": "list_books",
        "parameters": {}
      }
    ]
  }'
```

---

## Project Structure

```
book-api-mcp-server/
├── main.py              # FastAPI application and server setup
├── routes.py            # API route handlers for MCP endpoints
├── tools.py             # Tool definitions and schemas
├── services.py          # Business logic and Books API integration
├── models.py            # Pydantic models for data validation
├── config.py            # Configuration settings
├── run.py               # Server entry point
├── test_tools.py        # Test suite for validating tools
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

---

## Date Format Requirements

**Important:** All date fields (`publishedDate`) must be provided in ISO 8601 UTC format ending with 'Z'. This is required for PostgreSQL compatibility.

**Correct Format:**
- `2024-04-11T00:00:00Z`
- `2023-05-11T12:30:45Z`

**Incorrect Formats (will cause errors):**
- `2024-04-11T00:00:00` (missing 'Z')
- `2024-04-11` (not full ISO 8601)
- `04/11/2024` (not ISO 8601)

---

## Technologies

- **Python 3.8+**: Programming language
- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Pydantic**: Data validation using Python type annotations
- **Requests**: HTTP library for making API calls to the Books API

---

## Error Handling

All tools return a `ToolCallResult` object with the following structure:

```python
{
    "result": <data> | None,  # Result data if successful
    "error": <string> | None  # Error message if operation failed
}
```

Common error scenarios:
- **404 Not Found**: Book with specified ID does not exist
- **400 Bad Request**: Invalid input data (e.g., missing required fields, invalid date format)
- **500 Server Error**: Database or API connection issues
- **Connection Error**: Books API is not accessible

---

## Troubleshooting

### Server won't start
- Check if port 8080 is already in use
- Verify Python version (3.8+)
- Ensure all dependencies are installed

### Tools return connection errors
- Verify the Books API is running and accessible
- Check the `BOOKS_API_URL` in `services.py`
- Test the Books API directly: `curl http://localhost:5288/books`

### Date format errors
- Ensure all dates end with 'Z' for UTC timezone
- Use full ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`

---

## License

This project is part of a book management system demonstration.

