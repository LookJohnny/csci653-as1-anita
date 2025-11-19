# How to Restart Anita Server

## 🔄 Complete Server Restart Guide

### Step 1: Stop the Running Server

**Option A: If running in terminal**
- Press `Ctrl + C` in the terminal where the server is running
- Wait for the server to shut down completely

**Option B: If running in background**
```bash
# Find the process
ps aux | grep "python.*main_full.py"

# Kill the process (replace PID with the actual process ID)
kill <PID>

# Or kill all Python processes (use with caution!)
pkill -f "python.*main_full.py"
```

**Option C: On macOS (check Activity Monitor)**
- Open Activity Monitor (Applications → Utilities → Activity Monitor)
- Search for "python" or "main_full"
- Select the process and click "Force Quit"

### Step 2: Clear Browser Cache (Important!)

**Chrome/Edge:**
1. Open DevTools (F12 or Cmd+Option+I on Mac)
2. Right-click the refresh button
3. Select "Empty Cache and Hard Reload"

**Or use keyboard shortcut:**
- Windows: `Ctrl + Shift + R`
- Mac: `Cmd + Shift + R`

### Step 3: Start the Server

```bash
cd /Users/johnnyliu/Desktop/aiwaifu/AIWaifu
python3.12 main_full.py
```

### Step 4: Verify Voice Switching is Working

Look for these lines in the server startup:

```
[OK] Edge TTS initialized (voice: zh-CN-XiaomengNeural)
```

When you chat, you should see:
```
[TTS] ✅ Using English voice: en-US-SaraNeural
[TTS] ✅ Using Chinese voice: zh-CN-XiaomengNeural
```

### Step 5: Test in Browser

1. Open http://localhost:8000
2. Test English: "Hi Anita!"
   - Should use Sara voice (cheerful, expressive)
3. Test Chinese: "你好安妮塔！"
   - Should use Xiaomeng voice (cute loli)

## 🐛 Troubleshooting

### Problem: Still hearing the wrong voice

**Solution 1: Clear audio cache**
```bash
# Close browser completely
# Reopen and do hard refresh (Cmd+Shift+R or Ctrl+Shift+R)
```

**Solution 2: Check server logs**
Look for debug lines starting with `[TTS DEBUG]` or `[TTS]`
They should show which voice is being selected

**Solution 3: Run diagnostic test**
```bash
python3.12 test_voice_switching.py
```

Listen to the generated files:
- `diagnostic_english.wav` - Should sound cheerful and expressive
- `diagnostic_chinese.wav` - Should sound cute and high-pitched

### Problem: Server won't start

**Check if port 8000 is already in use:**
```bash
lsof -i :8000
```

**Kill the process using port 8000:**
```bash
kill -9 $(lsof -t -i :8000)
```

### Problem: Import errors

**Make sure all dependencies are installed:**
```bash
python3.12 -m pip install edge-tts anthropic fastapi uvicorn websockets
```

## ✅ Verification Checklist

Before reporting issues, verify:

- [ ] Server was completely stopped before restarting
- [ ] Browser cache was cleared (hard refresh)
- [ ] Server logs show correct voice selection
- [ ] `test_voice_switching.py` generates different audio files
- [ ] MD5 hashes of diagnostic files are different
- [ ] No error messages in server console

## 📋 Quick Start Commands

**One-line restart (macOS/Linux):**
```bash
pkill -f "python.*main_full.py" && sleep 2 && python3.12 main_full.py
```

**Start with output logging:**
```bash
python3.12 main_full.py 2>&1 | tee server.log
```

---

## 🎯 Expected Behavior

### English Input
```
User: "Hello Anita!"
[TTS DEBUG] Detected language: en
[TTS] ✅ Using English voice: en-US-SaraNeural
```

### Chinese Input
```
User: "你好安妮塔！"
[TTS DEBUG] Detected language: zh
[TTS] ✅ Using Chinese voice: zh-CN-XiaomengNeural
```

If you see these logs, **voice switching IS working correctly!**

The audio should sound noticeably different between languages.

---

*Last updated: 2025-10-19*
