# Anita Documentation Index 📚

Complete guide to all documentation for the Anita AI Voice Companion project.

## 🚀 Getting Started

### For New Users

1. **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup guide
   - Installation steps
   - First conversation
   - Quick troubleshooting

2. **[README.md](README.md)** - Main documentation
   - Features overview
   - Detailed installation
   - Configuration guide
   - Full troubleshooting

## 🎵 Voice Configuration

### Understanding Voices

3. **[VOICE_SWITCHING.md](VOICE_SWITCHING.md)** - How voice switching works
   - Technical details
   - Language detection
   - Implementation guide
   - Performance metrics

4. **[CUTE_VOICE_OPTIONS.md](CUTE_VOICE_OPTIONS.md)** - All available cute voices
   - English voice comparison
   - Chinese voice options
   - Voice parameters (rate, pitch)
   - Customization guide

### Voice Samples

- `voice_samples/luoli_cn.wav` - Chinese voice reference
- `voice_samples/luoli_en.wav` - English voice reference
- Generated test files from `test_voice_switching.py`

## 👧 Character Configuration

5. **[CHARACTER_CONFIG.md](CHARACTER_CONFIG.md)** - Anita's personality
   - Character profile
   - Personality traits
   - Communication style
   - Available emotions & gestures
   - How to customize

## 🔧 Server Management

### Running the Server

6. **[RESTART_SERVER.md](RESTART_SERVER.md)** - Complete restart guide
   - How to stop the server
   - How to start the server
   - Clear browser cache
   - Verification steps

### Troubleshooting

7. **[VOICE_SWITCHING_TROUBLESHOOTING.md](VOICE_SWITCHING_TROUBLESHOOTING.md)** - Detailed troubleshooting
   - Voice switching issues
   - Configuration checks
   - Diagnostic tests
   - Common problems & solutions

## 🛠️ Tools & Scripts

### Configuration Tools

8. **check_config.py** - Configuration checker
   ```bash
   python3.12 check_config.py
   ```
   - Verifies voice_en and voice_cn are set
   - Checks language detection code
   - Shows all configuration status

9. **test_voice_switching.py** - Voice switching test
   ```bash
   python3.12 test_voice_switching.py
   ```
   - Generates test audio files
   - Verifies different voices
   - No server needed

### Voice Utilities

10. **convert_voice_samples.py** - Audio converter
    - Convert MP4 to WAV
    - Voice analysis
    - Audio processing

11. **download_voice_samples.py** - Download samples
    - Download Edge TTS voice samples
    - Test different voices
    - Generate preview audio

12. **list_edge_voices.py** - List available voices
    - Show all Edge TTS voices
    - Filter by language/gender
    - Voice characteristics

## 📁 Project Structure

```
Anita/
│
├── 📘 Documentation (Start Here!)
│   ├── QUICKSTART.md                 ⭐ New users start here
│   ├── README.md                     📖 Main documentation
│   ├── DOCUMENTATION_INDEX.md        📚 This file
│   │
│   ├── Voice Configuration
│   │   ├── VOICE_SWITCHING.md
│   │   └── CUTE_VOICE_OPTIONS.md
│   │
│   ├── Character Setup
│   │   └── CHARACTER_CONFIG.md
│   │
│   └── Server & Troubleshooting
│       ├── RESTART_SERVER.md
│       └── VOICE_SWITCHING_TROUBLESHOOTING.md
│
├── 🛠️ Tools
│   ├── check_config.py               ✅ Check configuration
│   ├── test_voice_switching.py       🎵 Test voices
│   ├── convert_voice_samples.py      🔄 Convert audio
│   ├── download_voice_samples.py     ⬇️ Download samples
│   └── list_edge_voices.py           📋 List voices
│
├── 🎵 Voice Samples
│   ├── luoli_cn.wav                  🇨🇳 Chinese reference
│   └── luoli_en.wav                  🇬🇧 English reference
│
├── 💻 Core Code
│   ├── main_full.py                  🚀 Main server
│   ├── llm_pipeline.py               🤖 LLM backend
│   ├── tts_pipeline.py               🎤 Voice synthesis
│   └── [other Python files]
│
└── 🌐 Frontend
    ├── complete_v2.html              🎨 Main UI
    └── [other frontend files]
```

## 🎯 Quick Reference by Task

### "I want to get started"
→ **[QUICKSTART.md](QUICKSTART.md)**

### "I want to understand how voice switching works"
→ **[VOICE_SWITCHING.md](VOICE_SWITCHING.md)**

### "I want to change Anita's English voice"
→ **[CUTE_VOICE_OPTIONS.md](CUTE_VOICE_OPTIONS.md)**

### "I want to customize Anita's personality"
→ **[CHARACTER_CONFIG.md](CHARACTER_CONFIG.md)**

### "Voice switching isn't working!"
→ **[VOICE_SWITCHING_TROUBLESHOOTING.md](VOICE_SWITCHING_TROUBLESHOOTING.md)**

### "I need to restart the server"
→ **[RESTART_SERVER.md](RESTART_SERVER.md)**

### "I want to check if everything is configured correctly"
→ Run `python3.12 check_config.py`

### "I want to test voice switching without starting the server"
→ Run `python3.12 test_voice_switching.py`

## 📊 Documentation by Experience Level

### Beginner 🌱
1. [QUICKSTART.md](QUICKSTART.md) - Get up and running
2. [README.md](README.md) - Understand the basics
3. [RESTART_SERVER.md](RESTART_SERVER.md) - Learn server management

### Intermediate 🌿
4. [VOICE_SWITCHING.md](VOICE_SWITCHING.md) - Understand voice system
5. [CHARACTER_CONFIG.md](CHARACTER_CONFIG.md) - Customize personality
6. [CUTE_VOICE_OPTIONS.md](CUTE_VOICE_OPTIONS.md) - Explore voice options

### Advanced 🌳
7. [VOICE_SWITCHING_TROUBLESHOOTING.md](VOICE_SWITCHING_TROUBLESHOOTING.md) - Deep troubleshooting
8. Source code files (`*.py`) - Understand implementation
9. Tools and scripts - Extend functionality

## 🔍 Search by Topic

### Voice System
- Voice switching: [VOICE_SWITCHING.md](VOICE_SWITCHING.md)
- Voice options: [CUTE_VOICE_OPTIONS.md](CUTE_VOICE_OPTIONS.md)
- Voice troubleshooting: [VOICE_SWITCHING_TROUBLESHOOTING.md](VOICE_SWITCHING_TROUBLESHOOTING.md)
- Test voices: `test_voice_switching.py`

### Character & Personality
- Character setup: [CHARACTER_CONFIG.md](CHARACTER_CONFIG.md)
- Personality configuration: [README.md](README.md#character-personality)
- Emotions & gestures: [CHARACTER_CONFIG.md](CHARACTER_CONFIG.md#available-emotions)

### Server Management
- Quick start: [QUICKSTART.md](QUICKSTART.md)
- Restart guide: [RESTART_SERVER.md](RESTART_SERVER.md)
- Configuration: [README.md](README.md#configuration)
- Check config: `check_config.py`

### Troubleshooting
- General issues: [README.md](README.md#troubleshooting)
- Voice issues: [VOICE_SWITCHING_TROUBLESHOOTING.md](VOICE_SWITCHING_TROUBLESHOOTING.md)
- Quick fixes: [QUICKSTART.md](QUICKSTART.md#quick-fixes)

## 📞 Quick Help Commands

```bash
# Check everything is configured correctly
python3.12 check_config.py

# Test voice switching
python3.12 test_voice_switching.py

# Start server
python3.12 main_full.py

# Restart server cleanly
pkill -f "python.*main_full.py" && sleep 2 && python3.12 main_full.py
```

## 🆕 Recent Updates

### Latest Changes (2025-10-19)
- ✅ Added automatic voice switching between English and Chinese
- ✅ Updated to Sara voice for English (more cheerful and expressive)
- ✅ Created comprehensive troubleshooting guide
- ✅ Added diagnostic tools (check_config.py, test_voice_switching.py)
- ✅ Enhanced README with detailed server management section
- ✅ Added QUICKSTART guide for new users

### Documentation Added
- [VOICE_SWITCHING.md](VOICE_SWITCHING.md)
- [CUTE_VOICE_OPTIONS.md](CUTE_VOICE_OPTIONS.md)
- [RESTART_SERVER.md](RESTART_SERVER.md)
- [VOICE_SWITCHING_TROUBLESHOOTING.md](VOICE_SWITCHING_TROUBLESHOOTING.md)
- [QUICKSTART.md](QUICKSTART.md)
- [CHARACTER_CONFIG.md](CHARACTER_CONFIG.md)

## 🤝 Contributing to Documentation

Found an issue or want to improve documentation?

1. Check existing docs first
2. Create clear, concise documentation
3. Include code examples
4. Add to this index
5. Submit a Pull Request

## 📧 Support

### Self-Help Resources
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Check [VOICE_SWITCHING_TROUBLESHOOTING.md](VOICE_SWITCHING_TROUBLESHOOTING.md)
3. Run `python3.12 check_config.py`
4. Read [README.md](README.md)

### Still Stuck?
- Check server console logs
- Run diagnostic tests
- Review configuration files
- Check API key validity

---

**Last Updated:** 2025-10-19

🤖 Built with [Claude Code](https://claude.com/claude-code)
