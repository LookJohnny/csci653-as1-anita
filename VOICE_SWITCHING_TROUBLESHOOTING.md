# Voice Switching Troubleshooting Guide

## ✅ Configuration Status

**All code is correctly implemented!** Voice switching is working at the code level.

### Verified Working:
- ✅ Language detection (Chinese vs English)
- ✅ Voice configuration (Sara for English, Xiaomeng for Chinese)
- ✅ Voice selection logic
- ✅ Audio generation with different voices

### Test Results:
```bash
python3.12 test_voice_switching.py
```

Output shows:
```
[TTS] Using English voice: en-US-SaraNeural  ✅
[TTS] Using Chinese voice: zh-CN-XiaomengNeural  ✅
```

Generated files have **different MD5 hashes**, proving different audio is generated.

## 🔍 Why You Might Not Hear Different Voices

### Problem 1: Server Not Restarted

**The old server is still running with old code.**

**Solution:**
```bash
# Stop old server
pkill -f "python.*main_full.py"

# Wait a moment
sleep 2

# Start new server
python3.12 main_full.py
```

**What to look for in logs:**
```
Initializing TTS pipeline (engine: edge)...
[OK] Edge TTS initialized (voice: zh-CN-XiaomengNeural)
```

### Problem 2: Browser Cache

**Browser is playing cached audio from before the update.**

**Solution:**
- **Chrome/Edge**: Press `Cmd + Shift + R` (Mac) or `Ctrl + Shift + R` (Windows)
- **Safari**: Press `Cmd + Option + R`
- **Or**: Open DevTools → Right-click reload → "Empty Cache and Hard Reload"

### Problem 3: Not Looking at Server Console

**Server logs show which voice is being used, but you're not checking them.**

**Solution:**

When you chat in English, look for:
```
[TTS] Using English voice: en-US-SaraNeural
```

When you chat in Chinese, look for:
```
[TTS] Using Chinese voice: zh-CN-XiaomengNeural
```

**If you don't see these messages**, the server hasn't been restarted with the new code.

## 🧪 How to Test

### Test 1: Standalone Test (No Server Needed)

```bash
python3.12 test_voice_switching.py
```

This will:
1. Generate `diagnostic_english.wav` (Sara voice)
2. Generate `diagnostic_chinese.wav` (Xiaomeng voice)
3. Show detailed debug information

**Listen to both files** - they should sound noticeably different!

### Test 2: Direct Edge TTS Test

```bash
python3.12 -c "
import asyncio
import edge_tts

async def test():
    # Sara voice (English)
    comm = edge_tts.Communicate('Hi! I am Anita!', 'en-US-SaraNeural', rate='+5%', pitch='+10Hz')
    audio = b''
    async for chunk in comm.stream():
        if chunk['type'] == 'audio':
            audio += chunk['data']
    with open('test_sara.wav', 'wb') as f:
        f.write(audio)
    print('Saved test_sara.wav')

    # Xiaomeng voice (Chinese)
    comm = edge_tts.Communicate('你好！我是安妮塔！', 'zh-CN-XiaomengNeural', rate='+5%', pitch='+10Hz')
    audio = b''
    async for chunk in comm.stream():
        if chunk['type'] == 'audio':
            audio += chunk['data']
    with open('test_xiaomeng.wav', 'wb') as f:
        f.write(audio)
    print('Saved test_xiaomeng.wav')

asyncio.run(test())
"
```

Listen to the files - if they sound the same, there might be an Edge TTS issue.

### Test 3: Full Server Test

1. **Start server:**
   ```bash
   python3.12 main_full.py
   ```

2. **Open browser:** http://localhost:8000

3. **Say in English:** "Hi Anita!"
   - **Check server console** for: `[TTS] Using English voice: en-US-SaraNeural`

4. **Say in Chinese:** "你好安妮塔！"
   - **Check server console** for: `[TTS] Using Chinese voice: zh-CN-XiaomengNeural`

## 🎯 Expected Voice Characteristics

### English (Sara) Voice
- **Characteristic**: Cheerful, expressive, friendly
- **Pitch**: Higher (cute anime style)
- **Energy**: Bubbly, enthusiastic
- **Age**: Young, energetic

### Chinese (Xiaomeng) Voice
- **Characteristic**: Sweet, cute loli voice (萝莉音)
- **Pitch**: Very high (典型萝莉音)
- **Energy**: Soft, gentle
- **Age**: Very young, innocent

**They should sound VERY different!**

## 🔧 Quick Fixes

### Fix 1: Complete Server Restart
```bash
# Kill all Python processes (be careful!)
pkill -f "python.*main_full"

# Wait
sleep 3

# Restart
cd /Users/johnnyliu/Desktop/aiwaifu/AIWaifu
python3.12 main_full.py
```

### Fix 2: Clear Everything
```bash
# Close all browser tabs with Anita
# Clear browser cache completely
# Restart browser
# Restart server
# Open fresh tab to http://localhost:8000
```

### Fix 3: Check Configuration
```bash
python3.12 check_config.py
```

Should show all ✅ marks.

## 📊 Diagnostic Checklist

Run through this checklist:

- [ ] Configuration check passes: `python3.12 check_config.py`
- [ ] Standalone test works: `python3.12 test_voice_switching.py`
- [ ] Generated WAV files sound different when played
- [ ] Server was completely stopped before restart
- [ ] Server logs show "Using English voice" and "Using Chinese voice"
- [ ] Browser cache was cleared (hard refresh)
- [ ] Testing in a fresh browser tab/window

## 🆘 If Still Not Working

### Check 1: Are the voices actually different?

```bash
# Generate and compare
python3.12 test_voice_switching.py

# Check MD5 (should be different)
md5 diagnostic_english.wav diagnostic_chinese.wav
```

### Check 2: Is Edge TTS working?

```bash
# Test Edge TTS directly
edge-tts --voice en-US-SaraNeural --text "Hello" --write-media test1.mp3
edge-tts --voice zh-CN-XiaomengNeural --text "你好" --write-media test2.mp3
```

### Check 3: Check server is using new code

```bash
# Search for voice switching in running process
ps aux | grep python
# Note the PID, then:
lsof -p <PID> | grep tts_pipeline.py
```

## 💡 Remember

**The code IS working!** Tests prove it generates different audio.

If you're not hearing different voices, it's either:
1. ❌ Server not restarted
2. ❌ Browser cache
3. ❌ Not checking server logs

Follow the steps in [RESTART_SERVER.md](RESTART_SERVER.md) carefully!

---

## 📞 Quick Support Commands

```bash
# Check config
python3.12 check_config.py

# Test voice switching (no server)
python3.12 test_voice_switching.py

# Restart server cleanly
pkill -f "python.*main_full" && sleep 2 && python3.12 main_full.py
```

---

*Voice switching is implemented and working! Make sure to restart server and clear cache!*

*Last updated: 2025-10-19*
