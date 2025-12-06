"""
Video generation handler
Handles video explanation generation using FREE tools!
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from services.video_service import create_math_video

logger = logging.getLogger(__name__)


async def handle_video_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle video generation button callback
    """
    query = update.callback_query
    await query.answer()
    
    # Get stored problem and solution
    problem = context.user_data.get('last_problem')
    solution = context.user_data.get('last_solution')
    
    if not problem or not solution:
        await query.edit_message_text(
            "❌ Sorry, I couldn't find the problem. Please send it again."
        )
        return
    
    try:
        # Show processing message
        await query.edit_message_text(
            "� Creating audio explanation...\n"
            "⏳ This will take about 10-15 seconds..."
        )
        
        # Generate audio
        audio_path = await create_math_video(problem, solution)
        
        # Send audio
        await query.message.chat.send_action("upload_voice")
        
        with open(audio_path, 'rb') as audio:
            await query.message.reply_voice(
                voice=audio,
                caption="🎓 Here's your math explanation audio!"
            )
        
        # Delete processing message
        await query.message.delete()
        
        logger.info(f"Audio sent successfully to user {query.from_user.id}")
        
    except Exception as e:
        logger.error(f"Error generating audio: {str(e)}")
        await query.edit_message_text(
            f"❌ Sorry, there was an error creating the audio.\n\n"
            f"Error: {str(e)[:100]}"
        )
