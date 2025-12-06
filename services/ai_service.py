"""AI Service - Groq API integration for math problem solving"""

import logging
from groq import Groq
import config

logger = logging.getLogger(__name__)

client = Groq(api_key=config.GROQ_API_KEY)


async def solve_math_problem(problem: str) -> str:
    """Solve math problem using Groq API"""
    try:
        logger.info(f"Using {config.GROQ_MODEL}")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": config.MATH_TEACHER_PROMPT},
                {"role": "user", "content": f"Solve this math problem:\n\n{problem}"}
            ],
            model=config.GROQ_MODEL,
            temperature=0.7,
            max_tokens=2000,
        )
        
        solution = chat_completion.choices[0].message.content
        
        # Clean for Telegram compatibility
        clean_solution = solution.replace('*', '').replace('_', '').replace('`', '')
        clean_solution = clean_solution.replace('[', '(').replace(']', ')')
        clean_solution = clean_solution.replace('~', '').replace('>', '')
        
        return f"📝 Solution:\n\n{clean_solution}"
        
    except Exception as e:
        logger.error(f"Groq API error: {str(e)}")
        raise Exception(f"Failed to solve: {str(e)}")


def test_ai_connection():
    """
    Test the connection to Groq API
    """
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": "Test"}],
            model=config.GROQ_MODEL,
            max_tokens=10
        )
        logger.info("AI service connection test successful")
        return True
    except Exception as e:
        logger.error(f"AI service connection test failed: {str(e)}")
        return False
