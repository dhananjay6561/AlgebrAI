"""
Video Generation Service
Creates math explanation videos using FREE APIs!
Using simple image + audio approach (no complex video editing)
"""

import logging
import os
import asyncio
import tempfile
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
import textwrap

logger = logging.getLogger(__name__)

# Video settings
VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 720
VIDEO_FPS = 24
BG_COLOR = (15, 23, 42)  # Dark blue background
TEXT_COLOR = 'white'
FONT = 'Arial-Bold'
FONT_SIZE = 40


async def create_math_video(problem: str, solution: str) -> str:
    """
    Create an audio explanation with image for a math problem using FREE tools!
    Simplified approach - just creates an MP3 with solution
    
    Args:
        problem: The math problem text
        solution: The solution text
    
    Returns:
        Path to the generated audio file
    """
    logger.info("Creating audio explanation...")
    
    # Run in thread pool to avoid blocking
    loop = asyncio.get_event_loop()
    audio_path = await loop.run_in_executor(None, _generate_audio_sync, problem, solution)
    
    return audio_path


def _generate_audio_sync(problem: str, solution: str) -> str:
    """
    Synchronous audio generation (called in thread pool)
    Simple audio-only approach to avoid MoviePy issues
    """
    try:
        # Create temp directory
        temp_dir = tempfile.mkdtemp()
        audio_path = os.path.join(temp_dir, "math_solution.mp3")
        
        # Clean text for speech
        clean_text = solution.replace('📝', '').replace('Solution:', '')
        clean_text = clean_text.replace('*', '').replace('_', '').replace('`', '')
        
        # Add introduction
        full_script = f"Here is the solution to your math problem. {problem}. {clean_text}"
        
        # Generate speech using gTTS (FREE!)
        logger.info("Generating audio with gTTS...")
        tts = gTTS(text=full_script, lang='en', slow=False)
        tts.save(audio_path)
        
        logger.info(f"Audio generated successfully: {audio_path}")
        return audio_path
        
    except Exception as e:
        logger.error(f"Error in audio generation: {str(e)}")
        raise
