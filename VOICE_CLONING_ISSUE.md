# 语音克隆问题说明

## ❌ 问题：Coqui TTS 不兼容 Python 3.12

### 原因

您希望使用 `voice_samples` 文件夹中的真实声音样本进行语音克隆，这需要 **Coqui TTS** 引擎。

但是：
- **Coqui TTS 最高只支持 Python 3.11**
- 您的系统使用 **Python 3.12**
- 无法降级 Python 版本（会影响其他依赖）

### 错误信息
```
ERROR: Could not find a version that satisfies the requirement TTS
Requires-Python >=3.9.0,<3.12
```

---

## ✅ 当前解决方案

我已将 TTS 引擎切换到：
- **Engine**: Edge TTS (Microsoft)
- **Voice**: `en-US-JennyNeural`
- **特点**: 专业、自然的女声（比 Aria 更自然）
- **速度**: 正常速度（+0%）
- **音调**: 正常音调（+0Hz）

### 配置位置
[main_full.py:149-154](main_full.py#L149-L154)

---

## 🎤 如何获得更自然的声音

### 方案 1: 尝试其他 Edge TTS 声音（推荐）

编辑 [main_full.py:151](main_full.py#L151)，尝试这些声音：

```python
# 最自然的女声
voice="en-US-JennyNeural"    # ⭐ 当前 - 专业、自然
voice="en-US-SaraNeural"     # 温暖、友好
voice="en-US-NancyNeural"    # 成熟、自信
voice="en-US-MichelleNeural" # 温柔、平和

# 年轻女声
voice="en-US-AriaNeural"     # 活泼（之前使用的"机械音"）
voice="en-US-AshleyNeural"   # 充满活力

# 英式英语
voice="en-GB-SoniaNeural"    # 英国专业女声
voice="en-GB-LibbyNeural"    # 英国年轻女声
```

修改后重启服务器测试效果。

---

### 方案 2: 降级到 Python 3.11 使用 Coqui（不推荐）

如果一定要使用 voice_samples 的克隆声音：

1. **安装 Python 3.11**
   ```bash
   brew install python@3.11
   ```

2. **创建虚拟环境**
   ```bash
   python3.11 -m venv venv311
   source venv311/bin/activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   pip install TTS
   ```

4. **修改配置使用 Coqui**
   ```python
   tts_config = TTSConfig(
       engine="coqui",
       voice="tts_models/multilingual/multi-dataset/xtts_v2",
       speaker_wav="voice_samples/female_high_clear_1.wav",
       language="en"
   )
   ```

5. **运行**
   ```bash
   python main_full.py
   ```

**缺点**：
- 需要管理两个 Python 版本
- 依赖冲突风险
- Coqui TTS **非常慢**（5-7秒生成，vs Edge TTS 的 <1秒）

---

### 方案 3: 使用在线 TTS API（需付费）

一些支持语音克隆的服务：
- **ElevenLabs** - 最佳质量，但需付费
- **Play.ht** - 支持语音克隆
- **Resemble.ai** - 专业语音克隆

---

## 🎯 推荐做法

**短期方案（立即可用）：**
1. 刷新浏览器
2. 测试 `JennyNeural` 声音
3. 如果还是不满意，尝试 `SaraNeural` 或 `en-GB-SoniaNeural`

**长期方案（如需真实克隆）：**
- 考虑使用 Python 3.11 + Coqui TTS
- 或使用 ElevenLabs API（质量最高）

---

## 📝 当前服务器状态

- ✅ 服务器运行中: http://localhost:8000
- ✅ TTS 引擎: Edge TTS
- ✅ 声音: `en-US-JennyNeural`
- ✅ 语言: 英文
- ✅ 响应速度: <2秒

**请刷新浏览器并测试 Jenny 的声音是否比之前自然！**

---

## ❓ FAQ

**Q: 为什么 Edge TTS 听起来"机械"？**
A: `AriaNeural` 确实偏年轻化和活泼，可能显得不够自然。`JennyNeural` 更专业成熟。

**Q: 可以同时使用 Python 3.11 和 3.12 吗？**
A: 可以，但需要使用虚拟环境隔离，增加了复杂度。

**Q: Coqui TTS 有多慢？**
A: 生成 2 秒音频需要 5-7 秒，而 Edge TTS 只需 <1 秒。

**Q: voice_samples 文件是干什么用的？**
A: 这些是用于 Coqui TTS 语音克隆的参考音频样本。Edge TTS 不使用它们。

---

🤖 说明文档由 [Claude Code](https://claude.com/claude-code) 生成
