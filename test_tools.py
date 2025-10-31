#!/usr/bin/env python3
"""Test script to verify MCP server tools"""

from tools import get_tools_list, get_tool_implementations
from services import BookService
import json

def test_tool_definitions():
    """Test that all tools are properly defined"""
    print("=" * 60)
    print("Testing Tool Definitions")
    print("=" * 60)
    
    tools = get_tools_list()
    print(f"\n✓ Found {len(tools)} tools:\n")
    
    for tool in tools:
        print(f"  • {tool.name}")
        print(f"    Description: {tool.description}")
        print(f"    Required params: {tool.input_schema.get('required', [])}")
        print()
    
    return tools

def test_tool_implementations():
    """Test that all tools have implementations"""
    print("=" * 60)
    print("Testing Tool Implementations")
    print("=" * 60)
    
    implementations = get_tool_implementations()
    tools = get_tools_list()
    
    print(f"\n✓ Found {len(implementations)} implementations:\n")
    
    missing = []
    for tool in tools:
        if tool.name in implementations:
            print(f"  ✓ {tool.name} -> {implementations[tool.name].__name__}")
        else:
            print(f"  ✗ {tool.name} -> MISSING")
            missing.append(tool.name)
    
    if missing:
        print(f"\n✗ Missing implementations: {missing}")
        return False
    
    print("\n✓ All tools have implementations!")
    return True

def test_list_books():
    """Test the list_books tool"""
    print("\n" + "=" * 60)
    print("Testing list_books tool")
    print("=" * 60)
    
    try:
        result = BookService.list_books()
        if result.error:
            print(f"✗ Error: {result.error}")
            return False
        else:
            books = result.result
            print(f"✓ Successfully retrieved {len(books)} books")
            if books:
                print(f"  Sample book: {books[0].get('title', 'N/A')} by {books[0].get('author', 'N/A')}")
            return True
    except Exception as e:
        print(f"✗ Exception: {str(e)}")
        return False

def test_get_book():
    """Test the get_book tool"""
    print("\n" + "=" * 60)
    print("Testing get_book tool")
    print("=" * 60)
    
    try:
        result = BookService.get_book(1)
        if result.error:
            print(f"✗ Error: {result.error}")
            return False
        else:
            book = result.result
            print(f"✓ Successfully retrieved book:")
            print(f"  ID: {book.get('id', 'N/A')}")
            print(f"  Title: {book.get('title', 'N/A')}")
            print(f"  Author: {book.get('author', 'N/A')}")
            return True
    except Exception as e:
        print(f"✗ Exception: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("MCP Server Tools Test Suite")
    print("=" * 60)
    
    results = []
    
    # Test definitions
    tools = test_tool_definitions()
    results.append(("Tool Definitions", len(tools) > 0))
    
    # Test implementations
    results.append(("Tool Implementations", test_tool_implementations()))
    
    # Test API connectivity
    results.append(("list_books", test_list_books()))
    results.append(("get_book", test_get_book()))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    all_passed = all(result[1] for result in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit(main())

