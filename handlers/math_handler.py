"""
Math problem handler
Processes math problems and generates responses
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from services.ai_service import solve_math_problem
import config

logger = logging.getLogger(__name__)


async def handle_math_problem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle incoming math problems from users
    """
    user_message = update.message.text
    user_id = update.effective_user.id
    username = update.effective_user.username or "Unknown"
    
    logger.info(f"Received problem from {username} (ID: {user_id}): {user_message[:50]}...")
    
    # Send "typing" action to show bot is working
    await update.message.chat.send_action("typing")
    
    try:
        # Send acknowledgment
        processing_msg = await update.message.reply_text(
            "🤔 Let me solve that for you...\nProcessing your math problem..."
        )
        
        # Solve the problem using AI
        solution = await solve_math_problem(user_message)
        
        # Delete the processing message
        await processing_msg.delete()
        
        # Send the solution with video option
        if config.ENABLE_VIDEO:
            keyboard = [[InlineKeyboardButton("� Generate Audio Explanation", callback_data=f"video_{user_id}")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                solution,
                reply_markup=reply_markup
            )
            
            # Store the problem and solution for video generation
            context.user_data['last_problem'] = user_message
            context.user_data['last_solution'] = solution
        else:
            await update.message.reply_text(solution)
        
        logger.info(f"Successfully solved problem for {username}")
        
    except Exception as e:
        logger.error(f"Error solving problem: {str(e)}")
        await update.message.reply_text(
            "❌ Sorry, I encountered an error solving this problem. "
            "Please make sure your question is clear and try again.\n\n"
            f"Error details: {str(e)[:100]}"
        )
