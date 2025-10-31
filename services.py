from models import Book, ToolCallResult
import requests
from typing import Dict, Any

# Base URL of the Books API
BOOKS_API_URL = "http://localhost:5288"

class BookService:

    @staticmethod
    def list_books() -> ToolCallResult:
        """
        Retrieve all books from the Books API
        
        Returns:
            ToolCallResult with the list of books or an error message
        """
        try:
            # Make API request to the Books API
            response = requests.get(f"{BOOKS_API_URL}/books")
            
            # Handle different response statuses
            if response.status_code == 200:
                return ToolCallResult(
                    result=response.json()
                )
            else:
                return ToolCallResult(
                    result=None,
                    error=f"API Error: {response.status_code} - {response.text}"
                )
                
        except requests.RequestException as e:
            return ToolCallResult(
                result=None,
                error=f"Failed to connect to Books API: {str(e)}"
            )
        except Exception as e:
            return ToolCallResult(
                result=None,
                error=f"Error retrieving books: {str(e)}"
            )

    @staticmethod
    def create_book(book_data: dict) -> ToolCallResult:
        """
        Create a new book by calling the Books API
        
        Args:
            book_data: Dictionary containing book details (id, title, author, isbn, publishedDate)
                - publishedDate must be in ISO 8601 UTC format ending with 'Z' (e.g., '2024-04-11T00:00:00Z')
            
        Returns:
            ToolCallResult with the created book or an error message
        """
        try:
            # Make API request to the Books API
            # The API expects POST to /books with book data in the body
            response = requests.post(
                f"{BOOKS_API_URL}/books",
                json=book_data
            )
            
            # Handle different response statuses
            if response.status_code == 201:  # Created
                return ToolCallResult(
                    result=response.json()
                )
            elif response.status_code == 400:
                return ToolCallResult(
                    result=None,
                    error=f"Bad request: {response.text}"
                )
            else:
                return ToolCallResult(
                    result=None,
                    error=f"API Error: {response.status_code} - {response.text}"
                )
                
        except requests.RequestException as e:
            return ToolCallResult(
                result=None,
                error=f"Failed to connect to Books API: {str(e)}"
            )
        except Exception as e:
            return ToolCallResult(
                result=None,
                error=f"Error creating book: {str(e)}"
            )

    @staticmethod
    def get_book(book_id: int) -> ToolCallResult:
        """
        Retrieve a book by ID from the Books API
        
        Args:
            book_id: ID of the book to retrieve
            
        Returns:
            ToolCallResult with the book data or an error message
        """
        try:
            book_id = int(book_id)
            
            # Make API request to the Books API
            response = requests.get(f"{BOOKS_API_URL}/books/{book_id}")
            
            # Handle different response statuses
            if response.status_code == 200:
                return ToolCallResult(
                    result=response.json()
                )
            elif response.status_code == 404:
                return ToolCallResult(
                    result=None,
                    error=f"Book with ID {book_id} not found"
                )
            else:
                return ToolCallResult(
                    result=None,
                    error=f"API Error: {response.status_code} - {response.text}"
                )
                
        except requests.RequestException as e:
            return ToolCallResult(
                result=None,
                error=f"Failed to connect to Books API: {str(e)}"
            )
        except Exception as e:
            return ToolCallResult(
                result=None,
                error=f"Error retrieving book: {str(e)}"
            )

    @staticmethod
    def update_book(book_id: int, book_data: dict) -> ToolCallResult:
        """
        Update an existing book via the Books API
        
        Args:
            book_id: ID of the book to update
            book_data: Dictionary containing updated book details (must include id matching book_id)
                - publishedDate must be in ISO 8601 UTC format ending with 'Z' (e.g., '2024-04-11T00:00:00Z')
            
        Returns:
            ToolCallResult with the updated book or an error message
        """
        try:
            book_id = int(book_id)
            
            # Ensure book_data has the correct id
            book_data["id"] = book_id
            
            # Make API request to the Books API using PUT method
            response = requests.put(
                f"{BOOKS_API_URL}/books/{book_id}",
                json=book_data
            )
            
            # Handle different response statuses
            if response.status_code == 204:  # NoContent
                return ToolCallResult(
                    result={"message": "Book updated successfully"}
                )
            elif response.status_code == 400:
                return ToolCallResult(
                    result=None,
                    error=f"Bad request: {response.text}"
                )
            elif response.status_code == 404:
                return ToolCallResult(
                    result=None,
                    error=f"Book with ID {book_id} not found"
                )
            else:
                return ToolCallResult(
                    result=None,
                    error=f"API Error: {response.status_code} - {response.text}"
                )
                
        except requests.RequestException as e:
            return ToolCallResult(
                result=None,
                error=f"Failed to connect to Books API: {str(e)}"
            )
        except Exception as e:
            return ToolCallResult(
                result=None,
                error=f"Error updating book: {str(e)}"
            )

    @staticmethod
    def delete_book(book_id: int) -> ToolCallResult:
        """
        Delete a book by ID via the Books API
        
        Args:
            book_id: ID of the book to delete
            
        Returns:
            ToolCallResult with the deleted book or an error message
        """
        try:
            book_id = int(book_id)
            
            # Make API request to the Books API
            response = requests.delete(f"{BOOKS_API_URL}/books/{book_id}")
            
            # Handle different response statuses
            if response.status_code == 204:  # NoContent
                return ToolCallResult(
                    result={"message": "Book deleted successfully"}
                )
            elif response.status_code == 404:
                return ToolCallResult(
                    result=None,
                    error=f"Book with ID {book_id} not found"
                )
            else:
                return ToolCallResult(
                    result=None,
                    error=f"API Error: {response.status_code} - {response.text}"
                )
                
        except requests.RequestException as e:
            return ToolCallResult(
                result=None,
                error=f"Failed to connect to Books API: {str(e)}"
            )
        except Exception as e:
            return ToolCallResult(
                result=None,
                error=f"Error deleting book: {str(e)}"
            )