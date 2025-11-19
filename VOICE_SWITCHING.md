# Voice Switching Feature - Bilingual TTS

## Overview

Anita now supports automatic voice switching between Chinese and English based on the detected language in the text. This ensures natural pronunciation and accent for both languages.

## Features

- **Automatic Language Detection**: Detects if the text contains Chinese characters
- **Seamless Voice Switching**: Automatically switches between Chinese and English voices
- **No Configuration Needed**: Works automatically when you speak different languages

## Voice Profiles

### Chinese Voice (中文)
- **Voice**: `zh-CN-XiaomengNeural` (Microsoft Edge TTS)
- **Style**: Cute, youthful loli voice (萝莉音)
- **Characteristics**: Sweet, energetic, high-pitched
- **Sample**: [luoli_cn.wav](voice_samples/luoli_cn.wav)

### English Voice
- **Voice**: `en-US-SaraNeural` (Microsoft Edge TTS)
- **Style**: Friendly, cheerful, expressive
- **Characteristics**: Warm, upbeat, very expressive, perfect for bubbly anime character
- **Sample**: [luoli_en.wav](voice_samples/luoli_en.wav)

## Voice Settings

Both voices use the same settings for consistency:
- **Rate**: `+5%` (slightly faster than default)
- **Pitch**: `+10Hz` (higher pitch for anime character style)
- **SSML**: Disabled (prevents XML tags from being read aloud)

## How It Works

1. **Text Input**: User sends a message in Chinese or English
2. **Language Detection**: System detects language using Unicode ranges
   - Chinese: Contains characters in range `[\u4e00-\u9fff]`
   - English: No Chinese characters detected
3. **Voice Selection**: Appropriate voice is selected automatically
4. **Speech Synthesis**: Text is converted to speech with the selected voice

## Implementation

### Edge TTS (Default - Active)

```python
tts_config = TTSConfig(
    engine="edge",
    voice="zh-CN-XiaomengNeural",  # Default fallback
    voice_cn="zh-CN-XiaomengNeural",  # Chinese voice
    voice_en="en-US-SaraNeural",  # English voice
    rate="+5%",
    pitch="+10Hz",
    use_ssml=False
)
```

### Coqui XTTS-v2 (Alternative - Voice Cloning)

If using Coqui TTS with voice cloning (Python 3.9-3.11 only):

```python
tts_config = TTSConfig(
    engine="coqui",
    voice="tts_models/multilingual/multi-dataset/xtts_v2",
    speaker_wav_cn="voice_samples/luoli_cn.wav",
    speaker_wav_en="voice_samples/luoli_en.wav",
    language="auto"
)
```

## Examples

### Chinese Input
```
User: "你好呀！今天开心吗？"
Anita: Uses zh-CN-XiaomengNeural (cute Chinese voice)
```

### English Input
```
User: "Hi! How are you today?"
Anita: Uses en-US-JennyNeural (friendly English voice)
```

### Mixed Conversations
The system automatically switches voices based on each response's language:

```
User: "Hello Anita!"
Anita (English voice): "Hi there! Nice to see you!"

User: "你会说中文吗？"
Anita (Chinese voice): "当然会啦！我可以说中文和英文哦~"

User: "That's awesome!"
Anita (English voice): "Thank you! I love chatting in both languages!"
```

## Voice Sample Files

The following voice sample files are included:

- `voice_samples/luoli_cn.wav` - Chinese loli voice reference
- `voice_samples/luoli_en.wav` - English loli voice reference (newly generated)

## Technical Details

### Language Detection Function

```python
def _detect_language(self, text: str) -> str:
    """Detect if text is Chinese or English"""
    import re
    # If contains Chinese characters, it's Chinese
    if re.search(r'[\u4e00-\u9fff]', text):
        return "zh"
    return "en"
```

### Voice Selection Logic

For Edge TTS:
```python
language = self._detect_language(text)
voice = self.config.voice

if language == "zh" and self.config.voice_cn:
    voice = self.config.voice_cn
elif language == "en" and self.config.voice_en:
    voice = self.config.voice_en
```

For Coqui TTS:
```python
language = detect_language(text)  # Returns "zh-cn" or "en"
speaker_wav = self.config.speaker_wav

if language == "zh-cn" and self.config.speaker_wav_cn:
    speaker_wav = self.config.speaker_wav_cn
elif language == "en" and self.config.speaker_wav_en:
    speaker_wav = self.config.speaker_wav_en
```

## Testing

To test voice switching manually:

```bash
python3.12 -c "
import asyncio
from tts_pipeline import TTSPipeline, TTSConfig

async def test():
    config = TTSConfig(
        engine='edge',
        voice_cn='zh-CN-XiaomengNeural',
        voice_en='en-US-JennyNeural',
        rate='+5%',
        pitch='+10Hz'
    )

    pipeline = TTSPipeline(config)
    await pipeline.initialize()

    # Test Chinese
    result_cn = await pipeline.synthesize_with_phonemes('你好！')
    print(f'Chinese: {result_cn[\"duration_ms\"]:.0f}ms')

    # Test English
    result_en = await pipeline.synthesize_with_phonemes('Hello!')
    print(f'English: {result_en[\"duration_ms\"]:.0f}ms')

asyncio.run(test())
"
```

## Performance

Both voices maintain excellent performance:
- **Chinese**: ~500ms for typical response
- **English**: ~600ms for typical response
- **Latency**: Well within target (<700ms)

## Customization

To use different voices, modify the configuration in [main_full.py](main_full.py#L149-L157):

### Available Chinese Voices (Edge TTS)
- `zh-CN-XiaomengNeural` - Cute, youthful (current)
- `zh-CN-XiaoxiaoNeural` - Warm, friendly
- `zh-CN-XiaoyanNeural` - Professional, clear
- `zh-CN-YunxiNeural` - Energetic, lively

### Available English Voices (Edge TTS)
- `en-US-SaraNeural` - Friendly, cheerful, expressive (current ✨)
- `en-US-AnaNeural` - Sweet, young, gentle
- `en-US-SerenaMultilingualNeural` - Soft, shy, cute
- `en-US-JaneNeural` - Clear, versatile
- `en-US-JennyNeural` - Professional-friendly
- `en-US-AriaNeural` - Clear, professional
- `en-US-AshleyNeural` - Warm, conversational
- `en-US-CoraNeural` - Energetic, young

### Finding More Voices

List all available Edge TTS voices:
```bash
edge-tts --list-voices | grep -E "(zh-CN|en-US)" | grep Female
```

---

*Last updated: 2025-10-19*
