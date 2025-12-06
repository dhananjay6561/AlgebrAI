"""
Command handlers for the Telegram bot.
Handles /start, /help, and other basic commands.
"""

from telegram import Update
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    user_name = update.effective_user.first_name

    welcome_message = f"""
👋 Hey {user_name}, welcome!

This is the **Math Teacher Bot** — your simple AI math tutor.  
You can send me any math question, and I’ll walk you through it step by step. 🙂

📘 What I can help with:
• Algebra & equations  
• Calculus (derivatives, integrals, limits)  
• Geometry & trigonometry  
• Statistics & probability  
• Basic arithmetic  
• Word problems  

💡 How to use:
Just send a math problem like:
- Solve 2x + 5 = 15  
- Derivative of x^2  
- 15% of 280  
- Area of a circle (radius 5)

🎧 Audio explanations:
You can also request an audio explanation after getting a solution.

📎 Commands:
/start – Show this message  
/help – More detailed help

Whenever you're ready, send your first problem.
"""
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /help command."""
    help_message = """
📚 Math Teacher Bot – Help

I can assist with:
• Algebra (equations, factoring, simplification)  
• Calculus (limits, derivatives, integrals)  
• Geometry (areas, volumes, angles)  
• Trigonometry (identities, solving triangles)  
• Statistics (mean, probability, distributions)  
• Basic math (fractions, percentages, ratios)

✨ Tips for best results:
• Write problems clearly  
• Use standard notation (x^2, sqrt(), etc.)  
• Provide complete information  
• One problem at a time is best

📝 Example questions:
- Solve 3x - 7 = 14  
- Derivative of sin(x)cos(x)  
- Simplify (x² - 9)/(x - 3)  
- Factor x² - 5x + 6

🎧 Audio:
You can request an audio explanation if needed.

Send your math question anytime — I’m ready to help.
"""
    await update.message.reply_text(help_message)
