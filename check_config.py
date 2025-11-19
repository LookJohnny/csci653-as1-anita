#!/usr/bin/env python3.12
"""
Quick configuration check - verify TTS voice switching is properly configured
"""
import sys
import os

print("=" * 70)
print("ANITA CONFIGURATION CHECK")
print("=" * 70)

# Check main_full.py configuration
print("\n[1] Checking main_full.py configuration...")
try:
    with open("main_full.py", "r", encoding="utf-8") as f:
        content = f.read()

    # Check if voice_en is configured
    if "voice_en" in content:
        print("✅ voice_en parameter found")
        # Extract the value
        for line in content.split("\n"):
            if "voice_en" in line and not line.strip().startswith("#"):
                print(f"   {line.strip()}")
    else:
        print("❌ voice_en parameter NOT found!")

    # Check if voice_cn is configured
    if "voice_cn" in content:
        print("✅ voice_cn parameter found")
        for line in content.split("\n"):
            if "voice_cn" in line and not line.strip().startswith("#"):
                print(f"   {line.strip()}")
    else:
        print("❌ voice_cn parameter NOT found!")

except FileNotFoundError:
    print("❌ main_full.py not found!")
    sys.exit(1)

# Check tts_pipeline.py has voice switching code
print("\n[2] Checking tts_pipeline.py voice switching logic...")
try:
    with open("tts_pipeline.py", "r", encoding="utf-8") as f:
        content = f.read()

    if "_detect_language" in content:
        print("✅ Language detection function found")
    else:
        print("❌ Language detection function NOT found!")

    if "Using English voice:" in content:
        print("✅ English voice selection code found")
    else:
        print("❌ English voice selection code NOT found!")

    if "Using Chinese voice:" in content:
        print("✅ Chinese voice selection code found")
    else:
        print("❌ Chinese voice selection code NOT found!")

except FileNotFoundError:
    print("❌ tts_pipeline.py not found!")
    sys.exit(1)

# Check if test files exist
print("\n[3] Checking test scripts...")
if os.path.exists("test_voice_switching.py"):
    print("✅ test_voice_switching.py exists")
else:
    print("⚠️  test_voice_switching.py not found")

# Summary
print("\n" + "=" * 70)
print("CONFIGURATION CHECK COMPLETE")
print("=" * 70)
print("\nNext steps:")
print("1. Make sure server is stopped: pkill -f 'python.*main_full.py'")
print("2. Start server: python3.12 main_full.py")
print("3. Check server logs for '[TTS] Using English voice' messages")
print("4. Clear browser cache and hard reload (Cmd+Shift+R)")
print("5. Test with English and Chinese inputs")
print("\nTo test without server:")
print("  python3.12 test_voice_switching.py")
print("=" * 70)
