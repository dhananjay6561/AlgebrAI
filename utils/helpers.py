"""
Helper functions and utilities
"""

import re
from typing import Optional


def clean_math_input(text: str) -> str:
    """
    Clean and normalize math input text
    
    Args:
        text: Raw input text
    
    Returns:
        Cleaned text
    """
    # Remove excessive whitespace
    text = ' '.join(text.split())
    
    # Common replacements for better parsing
    replacements = {
        '×': '*',
        '÷': '/',
        '−': '-',
        '²': '^2',
        '³': '^3',
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text


def format_solution(solution: str) -> str:
    """
    Format the solution for better readability in Telegram
    
    Args:
        solution: Raw solution text
    
    Returns:
        Formatted solution
    """
    # Ensure proper spacing
    solution = solution.strip()
    
    # Add emojis for step indicators if not present
    if "Step" in solution and "📌" not in solution:
        solution = re.sub(r'Step (\d+)', r'📌 Step \1', solution)
    
    return solution


def is_math_problem(text: str) -> bool:
    """
    Detect if the text appears to be a math problem
    
    Args:
        text: Input text
    
    Returns:
        True if it looks like a math problem
    """
    # Math indicators
    math_keywords = [
        'solve', 'calculate', 'find', 'compute', 'simplify',
        'derivative', 'integral', 'equation', 'factor',
        '=', '+', '-', '*', '/', '^', 'x', 'y'
    ]
    
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in math_keywords)


def extract_equation(text: str) -> Optional[str]:
    """
    Try to extract a mathematical equation from text
    
    Args:
        text: Input text that may contain an equation
    
    Returns:
        Extracted equation or None
    """
    # Look for patterns like "solve: 2x + 5 = 15"
    equation_pattern = r'(?:solve:|equation:)?\s*([^.!?]+[=][^.!?]+)'
    match = re.search(equation_pattern, text, re.IGNORECASE)
    
    if match:
        return match.group(1).strip()
    
    return None


def truncate_text(text: str, max_length: int = 4000) -> str:
    """
    Truncate text to fit Telegram's message limit
    
    Args:
        text: Text to truncate
        max_length: Maximum length (Telegram limit is 4096)
    
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - 50] + "\n\n... (message truncated)"
