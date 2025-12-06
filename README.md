# 🤖 Math Teacher AI - Telegram Bot

<div align="center">

**AI-Powered Math Tutor on Telegram with Audio Explanations**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://telegram.org/)
[![Free AI](https://img.shields.io/badge/AI-Groq%20(FREE)-green.svg)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


[🔗 GitHub Repository](https://github.com/dhananjay6561/AlgebrAI)

Send any math problem → Get AI solution + Audio explanation!

</div>

---

## 📖 What is This Project?

This is a **fully functional Telegram bot** that acts as your personal math teacher. Send it any math problem, and it will:

1. ✅ **Solve the problem** using AI (Groq's LLaMA 3.1 - Super fast & FREE!)
2. ✅ **Explain step-by-step** how to solve it
3. ✅ **Generate audio explanation** (with voiceover!) completely FREE using gTTS

### Why This Project?

- 🆓 **100% FREE** - No paid APIs required!
- ⚡ **Blazing Fast** - Groq API is one of the fastest LLM providers
- � **Audio Explanations** - Voice explanations using Google Text-to-Speech
- 📱 **Easy to Use** - Just text your bot on Telegram
- 🚀 **Production Ready** - Properly structured, modular code
- 🎓 **Educational** - Great project to learn about AI agents and Telegram bots

---

## 🌟 Features

### Core Features
- **Math Problem Solving**: Algebra, Calculus, Geometry, Trigonometry, Statistics, etc.
- **Step-by-Step Explanations**: Detailed breakdown of solutions
- **Audio Explanations**: Voice explanations with text-to-speech
- **Fast Response**: Using Groq's infrastructure for quick responses
- **24/7 Availability**: Can be deployed to run continuously

### Technical Features
- Async/await for efficient operations
- Error handling and logging
- Modular architecture (easy to extend)
- Virtual environment setup
- Environment variable configuration
- Clean, well-documented code

---

## 🎯 How It Works

```
┌─────────────┐
│   User      │
│ (Telegram)  │
└──────┬──────┘
       │ "Solve: 2x + 5 = 15"
       ▼
┌─────────────────────┐
│  Telegram Bot API   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│   Your Bot Server   │
│  (This Project)     │
└──────┬──────────────┘
       │
       ├──► Groq AI API ──► Solves problem
       │                    Returns solution
       │
       └──► Video Service ─► Creates video
                             with voiceover
┌─────────────┐              (MoviePy + gTTS)
│   User      │
│ Receives:   │ ◄─────────────┘
│ • Text      │
│ • Video     │
└─────────────┘
```

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.9 or higher
- Telegram account
- 10 minutes of your time!

### Step 1: Clone/Download This Project

If you already have it, great! If not:
```bash
git clone https://github.com/dhananjay6561/AlgebrAI>
cd "AI Maths"
```

### Step 2: Get Your FREE API Keys

#### A) Telegram Bot Token (2 minutes)
1. Open Telegram
2. Search for `@BotFather`
3. Send command: `/newbot`
4. Follow the prompts:
   - Bot name: `My Math Teacher` (any name you like)
   - Username: `my_math_teacher_bot` (must end with 'bot')
5. **Copy the token** (looks like: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

#### B) Groq API Key (3 minutes) - 100% FREE!
1. Visit: https://console.groq.com/
2. Sign up with Google/GitHub (it's free!)
3. Go to: https://console.groq.com/keys
4. Click "Create API Key"
5. **Copy the key** (looks like: `gsk_abc123...`)

**Note**: Groq is FREE with generous limits (30 requests/minute)!

### Step 3: Configure Your Bot

1. Open the `.env` file in this folder
2. Replace the placeholder values:

```env
# Before:
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GROQ_API_KEY=your_groq_api_key_here

# After (example):
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
GROQ_API_KEY=gsk_abc123def456ghi789jkl012mno345pqr678
```

3. Save the file

### Step 4: Install Dependencies

The virtual environment is already created! Just install packages:

```bash
# Activate virtual environment (Linux/Mac)
source venv/bin/activate

# Install all required packages
pip install -r requirements.txt
```

**Note**: This will install:
- Telegram bot library
- Groq AI library
- MoviePy (video creation)
- gTTS (text-to-speech)
- Other utilities

### Step 5: Run Your Bot!

```bash
python bot.py
```

You should see:
```
Starting Math Teacher AI Bot...
Bot username: YourBotName
Press Ctrl+C to stop
```

### Step 6: Test It!

1. Open Telegram
2. Search for your bot username
3. Send `/start`
4. Try: `Solve: 2x + 5 = 15`
5. Click the video button to get a video explanation!

---

## 📱 Using the Bot

### Available Commands
- `/start` - Welcome message and instructions
- `/help` - Get help and examples

### Example Problems to Try

**Algebra:**
- `Solve: 2x + 5 = 15`
- `Factor: x² - 5x + 6`
- `Simplify: (x² - 9) / (x - 3)`

**Calculus:**
- `What is the derivative of x²?`
- `Integrate sin(x) from 0 to π`
- `Find the limit of (x² - 4)/(x - 2) as x approaches 2`

**Geometry:**
- `Calculate the area of a circle with radius 5`
- `What is the volume of a sphere with radius 3?`

**Basic Math:**
- `What is 15% of 280?`
- `Calculate: (45 × 12) + (88 ÷ 4)`

### Video Generation
After receiving a text solution, click the **"🎥 Generate Video Explanation"** button to create a video with voiceover! Videos take 30-60 seconds to generate.

---

## 📁 Project Structure

```
AI Maths/
├── bot.py                  # Main entry point - starts the bot
├── config.py               # Configuration & environment variables
├── requirements.txt        # Python dependencies
├── .env                    # Your API keys (DO NOT SHARE!)
├── .env.example           # Template for .env
├── .gitignore             # Git ignore rules
│
├── handlers/              # Request handlers
│   ├── __init__.py
│   ├── commands.py        # /start, /help commands
│   ├── math_handler.py    # Main math problem handler
│   └── video_handler.py   # Video generation callbacks
│
├── services/              # External services
│   ├── __init__.py
│   ├── ai_service.py      # Groq AI integration
│   └── video_service.py   # Video generation (MoviePy + gTTS)
│
├── utils/                 # Utility functions
│   ├── __init__.py
│   └── helpers.py         # Text processing helpers
│
└── venv/                  # Virtual environment (don't touch!)
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `bot.py` | Main file that starts the bot and registers handlers |
| `config.py` | Loads environment variables and validates configuration |
| `handlers/math_handler.py` | Processes math problems and calls AI service |
| `services/ai_service.py` | Communicates with Groq AI API |
| `services/video_service.py` | Creates videos using MoviePy and gTTS |
| `.env` | Stores your secret API keys (never commit to git!) |

---

## 🔧 Advanced Configuration

### Changing the AI Model

Edit `.env`:
```env
GROQ_MODEL=llama-3.1-70b-versatile  # Default (best)
# or
GROQ_MODEL=mixtral-8x7b-32768       # Alternative
# or
GROQ_MODEL=llama-3.1-8b-instant     # Faster but less accurate
```

### Disabling Video Generation

Edit `.env`:
```env
ENABLE_VIDEO=False
```

### Customizing the AI Teacher Personality

Edit `config.py` and modify `MATH_TEACHER_PROMPT`:
```python
MATH_TEACHER_PROMPT = """You are a friendly math tutor who explains things simply..."""
```

## 🛠️ Troubleshooting

### "Module not found" Error
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### "API key not set" Error
- Check `.env` file exists
- Make sure you pasted the actual keys (no quotes needed)
- No spaces before/after the keys

### Bot doesn't respond
- Make sure the bot is running (check terminal)
- Send `/start` first
- Check you're messaging the correct bot
- Look for errors in the terminal

### Video generation fails
```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt-get install ffmpeg

# For Mac
brew install ffmpeg
```

### Slow video generation
- Normal! Videos take 30-60 seconds
- MoviePy processes everything locally
- Faster with better CPU

---

## 🎓 Learning & Customization

### Want to modify the bot? Here's how:

**Change how problems are solved:**
- Edit `services/ai_service.py`
- Modify the prompt in `config.py`

**Add new commands:**
- Add functions in `handlers/commands.py`
- Register them in `bot.py`

**Customize videos:**
- Edit `services/video_service.py`
- Change colors, fonts, duration

**Add features:**
- Image recognition for handwritten math
- User history/statistics
- Multiple languages
- Math quiz mode

---

## 🤝 Contributing

Want to improve this project? Great! Here's how:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

Ideas for contributions:
- [ ] Add support for image input (handwritten math)
- [ ] Implement user statistics
- [ ] Add more languages
- [ ] Improve video quality
- [ ] Add quiz/practice mode
- [ ] Better error messages

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙏 Acknowledgments

- **Groq** for providing free, fast AI inference
- **Telegram** for the excellent Bot API
- **MoviePy** for video generation
- **gTTS** for text-to-speech

---

## 📧 Support

Having issues? Here are resources:

- **Groq Documentation**: https://console.groq.com/docs
- **Telegram Bot API**: https://core.telegram.org/bots/api
- **python-telegram-bot**: https://docs.python-telegram-bot.org/
- **MoviePy**: https://zulko.github.io/moviepy/

---

## 🎯 What's Next?

Once your bot is working:

1. ✅ Test with various math problems
2. ✅ Share with friends to get feedback
3. ✅ Deploy to cloud for 24/7 access
4. ✅ Add custom features
5. ✅ Use it to actually learn math!

---

<div align="center">

**Made with ❤️ for learning and teaching math**

⭐ Star this repo if you found it helpful!

</div>
