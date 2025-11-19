#!/usr/bin/env python3.12
"""
Test script to verify voice switching is working correctly
Run this to diagnose voice switching issues
"""
import asyncio
import sys
from tts_pipeline import TTSPipeline, TTSConfig

async def test_voice_switching():
    print("=" * 70)
    print("VOICE SWITCHING DIAGNOSTIC TEST")
    print("=" * 70)

    # Create config exactly as in main_full.py
    config = TTSConfig(
        engine="edge",
        voice="zh-CN-XiaomengNeural",
        voice_cn="zh-CN-XiaomengNeural",
        voice_en="en-US-SaraNeural",
        rate="+5%",
        pitch="+10Hz",
        use_ssml=False
    )

    print("\n[Configuration Check]")
    print(f"Engine: {config.engine}")
    print(f"Default voice: {config.voice}")
    print(f"Chinese voice: {config.voice_cn}")
    print(f"English voice: {config.voice_en}")
    print(f"Rate: {config.rate}")
    print(f"Pitch: {config.pitch}")

    # Initialize pipeline
    pipeline = TTSPipeline(config)
    await pipeline.initialize()

    print("\n[Test 1: English Text]")
    print("Input: 'Hello! I am Anita!'")
    result = await pipeline.synthesize_with_phonemes("Hello! I am Anita!")
    print(f"Audio size: {len(result['audio'])} bytes")
    print(f"Duration: {result['duration_ms']:.0f}ms")

    # Save for verification
    with open("diagnostic_english.wav", "wb") as f:
        f.write(result['audio'])
    print("✅ Saved: diagnostic_english.wav")

    print("\n[Test 2: Chinese Text]")
    print("Input: '你好！我是安妮塔！'")
    result = await pipeline.synthesize_with_phonemes("你好！我是安妮塔！")
    print(f"Audio size: {len(result['audio'])} bytes")
    print(f"Duration: {result['duration_ms']:.0f}ms")

    # Save for verification
    with open("diagnostic_chinese.wav", "wb") as f:
        f.write(result['audio'])
    print("✅ Saved: diagnostic_chinese.wav")

    print("\n" + "=" * 70)
    print("DIAGNOSTIC COMPLETE")
    print("=" * 70)
    print("\nCheck the console output above:")
    print("- You should see '[TTS] Using English voice: en-US-SaraNeural'")
    print("- You should see '[TTS] Using Chinese voice: zh-CN-XiaomengNeural'")
    print("\nListen to the generated files:")
    print("- diagnostic_english.wav (should be Sara voice)")
    print("- diagnostic_chinese.wav (should be Xiaomeng voice)")
    print("\nIf voices sound the same, the switching is NOT working.")
    print("If voices sound different, the switching IS working!")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(test_voice_switching())
