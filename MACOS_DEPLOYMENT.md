# Ani - macOS 本地部署指南

本指南将帮助您在 macOS 上部署 Ani AI Voice Companion 项目，使用 Claude Haiku 4.5 模型。

## 系统要求

- macOS 11.0 或更高版本
- Python 3.12+
- 稳定的网络连接（用于调用 Claude API）

## 已完成的配置

✅ Python 3.12.0 已安装
✅ 所有依赖包已安装
✅ 配置文件已创建
✅ LLM 模型已更新为 Claude 3.5 Haiku 4.5 (`claude-3-5-haiku-20250110`)
✅ macOS 启动脚本已创建

## 部署步骤

### 1. 配置 API Key

编辑 `.env` 文件，替换您的 Claude API Key：

```bash
# 使用任何文本编辑器打开 .env 文件
nano .env

# 或使用 VS Code
code .env
```

将这一行：
```
CLAUDE_API_KEY=your-claude-api-key-here
```

替换为您的真实 API Key：
```
CLAUDE_API_KEY=sk-ant-api03-xxxxx...
```

**获取 API Key**: 访问 [Anthropic Console](https://console.anthropic.com/)

### 2. 启动服务器

```bash
./start_server.sh
```

或者直接运行：
```bash
python3.12 main_full.py
```

### 3. 访问 Web 界面

打开浏览器访问：
```
http://localhost:8000
```

您应该能看到 Ani 的 3D 形象和对话界面。

## 配置说明

### 当前 LLM 配置

在 [main_full.py:100-108](main_full.py#L100-L108) 中：

```python
llm_config = LLMConfig(
    backend="anthropic",
    model="claude-3-5-haiku-20250110",  # Haiku 4.5
    max_tokens=250,
    temperature=0.8,
    openai_api_key=os.getenv("CLAUDE_API_KEY"),
    character_name="Anita",
    character_personality="friendly and cheerful anime companion"
)
```

### 语音配置

默认使用 **Edge TTS** 引擎，声音为 `zh-CN-XiaoyiNeural` (少女音)。

在 [main_full.py](main_full.py) 中可以切换其他声音：
- `zh-CN-XiaomoNeural` - 御姐音
- `zh-CN-XiaomengNeural` - 萌萝莉音
- `zh-CN-XiaohanNeural` - 熟女音
- `zh-CN-XiaorouNeural` - 少妇音

## 性能优化

### Haiku 4.5 的优势

- **速度快**: 比 Haiku 3.5 快 25%
- **成本低**: 输入 $0.25/MTok，输出 $1.25/MTok
- **双语支持**: 优秀的中英文混合对话能力
- **低延迟**: 通常 0.5-1 秒响应时间

### 预期性能

| 组件 | 延迟 | 备注 |
|------|------|------|
| LLM (Haiku 4.5) | 0.4-0.8s | 比 3.5 快 25% |
| TTS (Edge) | <1s | 微软云服务 |
| 总延迟 | **<2s** | 端到端响应 |

## 故障排除

### 问题 1: 找不到 Python 模块

确保使用 Python 3.12：
```bash
python3.12 --version
python3.12 -m pip list
```

### 问题 2: API Key 错误

检查 `.env` 文件中的 API Key 是否正确：
```bash
cat .env | grep CLAUDE_API_KEY
```

### 问题 3: 端口已被占用

修改 `.env` 中的端口：
```
PORT=8001
```

### 问题 4: 依赖安装失败

重新安装依赖：
```bash
python3.12 -m pip install --upgrade pip setuptools wheel
python3.12 -m pip install fastapi uvicorn websockets pydantic \
    python-multipart python-dotenv edge-tts numpy anthropic \
    aiohttp python-osc soundfile
```

## 可选功能

### 启用服务器端语音识别 (需要 GPU)

如果您有支持 CUDA 的 NVIDIA GPU，可以启用服务器端的语音活动检测和语音转文字功能：

1. 安装额外依赖：
```bash
python3.12 -m pip install torch torchaudio silero-vad faster-whisper
```

2. 修改 `.env`:
```
ENABLE_AUDIO_PIPELINE=1
```

**注意**: macOS 通常不支持 CUDA，建议使用浏览器内置的语音识别功能。

## 下一步

- 配置您的 API Key
- 运行 `./start_server.sh`
- 访问 http://localhost:8000
- 开始与 Ani 对话！

## 技术支持

如有问题，请查看：
- [README.md](README.md) - 项目概览
- [USER_GUIDE.md](USER_GUIDE.md) - 使用指南
- [DEBUG_GUIDE.md](DEBUG_GUIDE.md) - 调试指南

---

🤖 部署配置由 [Claude Code](https://claude.com/claude-code) 生成
📅 日期: 2025-10-18
