"""
Math Teacher AI Bot - Main Entry Point
A Telegram bot that solves math problems using AI
"""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

import config
from handlers.math_handler import handle_math_problem
from handlers.commands import start_command, help_command
from handlers.video_handler import handle_video_callback

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO if not config.DEBUG_MODE else logging.DEBUG
)
logger = logging.getLogger(__name__)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Update {update} caused error {context.error}")
    
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "Sorry, something went wrong while processing your request. Please try again."
        )


def main():
    """Start the bot"""
    # Validate configuration
    try:
        config.validate_config()
        logger.info("Configuration validated successfully")
    except ValueError as e:
        logger.error(str(e))
        return
    
    # Create application
    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    
    # Register callback handler for video generation
    application.add_handler(CallbackQueryHandler(handle_video_callback, pattern="^video_"))
    
    # Register message handler for math problems
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_math_problem
    ))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Starting Math Teacher AI Bot...")
    logger.info(f"Bot username: {config.BOT_USERNAME}")
    logger.info("Press Ctrl+C to stop")
    
    # Run the bot using polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
