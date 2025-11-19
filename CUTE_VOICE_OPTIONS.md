# Cute English Voice Options for Anita

## Currently Active Voice

**en-US-SaraNeural** ✨ (Friendly, cheerful, expressive loli voice)

## Top Cute Voice Recommendations

### 1. en-US-SaraNeural ✨ (Current - Active)
- **Style**: Friendly, expressive, energetic
- **Best for**: Bubbly, cheerful anime character
- **Available Styles**: cheerful, excited, friendly, hopeful
- **Characteristics**: Warm, upbeat, very expressive
- **Rating**: ⭐⭐⭐⭐⭐
- **Why chosen**: Perfect for Anita's energetic and cheerful personality!

```python
voice_en="en-US-SaraNeural"
```

### 2. en-US-AnaNeural (Sweet Alternative)
- **Style**: Sweet, young, clear
- **Best for**: Cute anime character, gentle loli voice
- **Characteristics**: Natural, youthful, innocent tone
- **Rating**: ⭐⭐⭐⭐⭐

```python
voice_en="en-US-AnaNeural"
```

### 3. en-US-SerenaMultilingualNeural (Shy Cute)
- **Style**: Gentle, soft, shy
- **Best for**: Shy/timid anime character
- **Available Styles**: shy, friendly, excited, relieved
- **Characteristics**: Softer tone, very cute when shy
- **Rating**: ⭐⭐⭐⭐

```python
voice_en="en-US-SerenaMultilingualNeural"
```

### 4. en-US-JaneNeural (Versatile)
- **Style**: Clear, friendly, versatile
- **Best for**: All-around cute character
- **Available Styles**: cheerful, excited, friendly, hopeful
- **Characteristics**: Balanced, natural, expressive
- **Rating**: ⭐⭐⭐⭐

```python
voice_en="en-US-JaneNeural"
```

### 5. en-US-JennyNeural (Previous Default)
- **Style**: Professional-friendly
- **Best for**: Mature but friendly character
- **Available Styles**: chat, cheerful, excited, friendly
- **Characteristics**: Clear, natural, slightly more mature
- **Rating**: ⭐⭐⭐

```python
voice_en="en-US-JennyNeural"
```

## How to Change the Voice

Edit [main_full.py](main_full.py#L153) and change the `voice_en` parameter:

```python
tts_config = TTSConfig(
    engine="edge",
    voice="zh-CN-XiaomengNeural",
    voice_cn="zh-CN-XiaomengNeural",
    voice_en="en-US-AnaNeural",  # ← Change this line
    rate="+5%",
    pitch="+10Hz",
    use_ssml=False
)
```

## Voice Comparison Samples

Test samples are available in `voice_samples/`:

- `test_ana.wav` - AnaNeural (current)
- `test_sara.wav` - SaraNeural
- `test_serena.wav` - SerenaMultilingualNeural
- `test_jane.wav` - JaneNeural
- `test_jenny_(current).wav` - JennyNeural (previous)

## Advanced: Using Voice Styles

Some voices support different emotional styles. To use them with Edge TTS, you would need to use SSML (currently disabled to prevent XML tags being read aloud).

### Example with Styles (if SSML was enabled):

```xml
<speak>
    <mstts:express-as style="cheerful">
        Hi there! I'm so happy to see you!
    </mstts:express-as>
</speak>
```

Available styles for cute voices:
- **cheerful** - Happy, upbeat tone
- **excited** - Very energetic, enthusiastic
- **friendly** - Warm, welcoming
- **hopeful** - Optimistic, positive
- **shy** - Soft, timid (SerenaMultilingualNeural only)

## Fine-tuning Voice Parameters

### Current Settings
```python
rate="+5%"   # Slightly faster (more energetic)
pitch="+10Hz"  # Higher pitch (cuter, more anime-like)
```

### Adjustment Options

**For an even cuter voice:**
```python
rate="+8%"   # Faster = more energetic
pitch="+15Hz"  # Even higher pitch = more loli-like
```

**For a sweeter, slower voice:**
```python
rate="+0%"   # Normal speed = more gentle
pitch="+12Hz"  # Medium-high pitch = sweet but clear
```

**For maximum kawaii effect:**
```python
rate="+10%"  # Very energetic
pitch="+20Hz"  # Very high pitch (like anime lolis)
```

## Recommended Combinations

### Option A: Sweet and Gentle (Current ✨)
```python
voice_en="en-US-AnaNeural"
rate="+5%"
pitch="+10Hz"
```

### Option B: Bubbly and Energetic
```python
voice_en="en-US-SaraNeural"
rate="+8%"
pitch="+12Hz"
```

### Option C: Shy and Cute
```python
voice_en="en-US-SerenaMultilingualNeural"
rate="+3%"
pitch="+10Hz"
```

### Option D: Maximum Kawaii
```python
voice_en="en-US-AnaNeural"
rate="+10%"
pitch="+20Hz"
```

## Testing Different Voices

To quickly test a voice without starting the full server:

```bash
python3.12 -c "
import asyncio
from tts_pipeline import TTSPipeline, TTSConfig

async def test():
    config = TTSConfig(
        engine='edge',
        voice_en='en-US-AnaNeural',  # Change this
        rate='+5%',
        pitch='+10Hz'
    )

    pipeline = TTSPipeline(config)
    await pipeline.initialize()

    result = await pipeline.synthesize_with_phonemes('Hi! I am Anita!')
    print(f'Generated {len(result[\"audio\"])} bytes')

asyncio.run(test())
"
```

## Other Cute English Voices to Try

### American English
- `en-US-AmberNeural` - Warm, gentle
- `en-US-AshleyNeural` - Young, friendly
- `en-US-CoraNeural` - Clear, pleasant

### British English (Different Accent)
- `en-GB-MaisieNeural` - Young British accent
- `en-GB-SoniaNeural` - Cheerful British accent

### Australian English
- `en-AU-FreyaNeural` - Young Australian accent
- `en-AU-NatashaNeural` - Friendly Australian accent

---

**Current Configuration**: en-US-SaraNeural (Friendly, cheerful, expressive loli voice)

*Last updated: 2025-10-19*
