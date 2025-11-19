# Anita Quick Start Guide 🚀

Get Anita up and running in 5 minutes!

## ⚡ 5-Minute Setup

### Step 1: Install Python 3.12

**macOS:**
```bash
# Using Homebrew
brew install python@3.12

# Verify
python3.12 --version
```

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- Check "Add Python to PATH" during installation
- Verify: `py --version`

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.12

# Verify
python3.12 --version
```

### Step 2: Clone & Install

```bash
# Clone repository
cd ~/Desktop
git clone https://github.com/yourusername/Anita.git
cd Anita

# Install dependencies
python3.12 -m pip install -r requirements.txt
```

### Step 3: Configure API Key

Create `.env` file:
```bash
# Create file
touch .env

# Edit with your favorite editor
nano .env
```

Add this line:
```
CLAUDE_API_KEY=sk-ant-your-api-key-here
```

**Don't have a key?** Get one from [console.anthropic.com](https://console.anthropic.com/)

### Step 4: Start Server

```bash
python3.12 main_full.py
```

Wait for:
```
[OK] Anthropic Claude backend initialized
[OK] Edge TTS initialized
[OK] Ani v0 Server Ready!
```

### Step 5: Open Browser

Open: **http://localhost:8000**

That's it! 🎉

## 🎤 First Conversation

1. **Click the microphone button** or **type a message**
2. **Say/Type:** "Hi Anita!"
3. **Watch her respond** with voice and animation!

### Try These:

**English:**
- "Hi Anita! How are you?"
- "Tell me a joke!"
- "What do you like to do?"

**Chinese:**
- "你好安妮塔！"
- "今天天气怎么样？"
- "你喜欢做什么？"

## 🔧 Quick Checks

### Is It Working?

Look for these in the server console:

**When you speak English:**
```
[TTS] Using English voice: en-US-SaraNeural
```

**When you speak Chinese:**
```
[TTS] Using Chinese voice: zh-CN-XiaomengNeural
```

**If you don't see these**, run:
```bash
python3.12 check_config.py
```

### Test Voice Switching

```bash
# Generate test audio files
python3.12 test_voice_switching.py

# Listen to the files
open diagnostic_english.wav  # macOS
open diagnostic_chinese.wav  # macOS

# Windows: double-click the files in Explorer
```

They should sound **noticeably different!**

## 🐛 Quick Fixes

### "Module not found"
```bash
python3.12 -m pip install -r requirements.txt
```

### "Port 8000 already in use"
```bash
# macOS/Linux
lsof -i :8000
kill -9 <PID>

# Windows
netstat -ano | findstr :8000
taskkill /F /PID <PID>
```

### "API key not working"
- Make sure `.env` file exists in project root
- Check no extra spaces: `CLAUDE_API_KEY=sk-ant-...` (no spaces!)
- Verify key is valid at [console.anthropic.com](https://console.anthropic.com/)

### Voices sound the same
1. **Restart server** (Ctrl+C, then start again)
2. **Clear browser cache** (Cmd+Shift+R or Ctrl+Shift+R)
3. Check server logs for voice switching messages

## 🎯 Configuration

### Change English Voice

Edit `main_full.py` line 153:

```python
voice_en="en-US-SaraNeural",  # Change this
```

**Options:**
- `en-US-SaraNeural` - Cheerful, expressive (current)
- `en-US-AnaNeural` - Sweet, gentle
- `en-US-SerenaMultilingualNeural` - Soft, shy
- `en-US-JaneNeural` - Clear, versatile

**After changing:** Restart server + clear browser cache!

### Change Personality

Edit `main_full.py` line 107:

```python
character_personality="""Your custom personality here"""
```

**After changing:** Restart server!

## 📚 Next Steps

- **[README.md](README.md)** - Full documentation
- **[CHARACTER_CONFIG.md](CHARACTER_CONFIG.md)** - Customize personality
- **[CUTE_VOICE_OPTIONS.md](CUTE_VOICE_OPTIONS.md)** - Explore voice options
- **[VOICE_SWITCHING_TROUBLESHOOTING.md](VOICE_SWITCHING_TROUBLESHOOTING.md)** - Fix issues

## 🆘 Need Help?

### Check Configuration
```bash
python3.12 check_config.py
```

### Test Without Server
```bash
python3.12 test_voice_switching.py
```

### View Detailed Logs
```bash
python3.12 main_full.py 2>&1 | tee server.log
```

### Common Issues

| Symptom | Solution |
|---------|----------|
| No response | Check API key in `.env` |
| Same voice for all languages | Restart server + clear cache |
| Slow responses | Normal for Claude API (2-4s) |
| No audio | Check browser audio permissions |

## 💡 Tips

### Speed Up Development

**Auto-restart on file changes:**
```bash
# Install watchdog
pip install watchdog

# Auto-restart (macOS/Linux)
watchmedo auto-restart --pattern="*.py" --recursive -- python3.12 main_full.py
```

### Keep Server Running

**Use screen/tmux (Linux/macOS):**
```bash
# Start screen
screen -S anita

# Run server
python3.12 main_full.py

# Detach: Ctrl+A, then D
# Reattach: screen -r anita
```

**Use nohup:**
```bash
nohup python3.12 main_full.py > server.log 2>&1 &
```

### Save Conversations

Server logs are displayed in console. To save:
```bash
python3.12 main_full.py 2>&1 | tee conversation.log
```

## 🎉 You're Ready!

Enjoy chatting with Anita! She's:
- ✅ Bilingual (English + Chinese)
- ✅ Sweet and energetic personality
- ✅ Fast responses (<5s)
- ✅ Automatic voice switching
- ✅ Context-aware conversation

**Have fun!** 💕

---

*For detailed documentation, see [README.md](README.md)*
