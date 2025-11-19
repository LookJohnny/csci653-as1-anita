# 音频播放问题解决指南

## 🔊 问题现象

- ✅ Ani 有动作和表情
- ✅ 服务器显示 TTS 成功
- ❌ **但听不到声音**

## 💡 原因

这是**浏览器自动播放策略**导致的。Chrome、Safari 等现代浏览器会阻止自动播放音频，除非：
1. 用户先与页面交互过
2. 网站被加入白名单

## ✅ 解决方法（3 步）

### 方法 1: 刷新页面 + 点击激活（最简单）

1. **刷新浏览器页面**
   ```
   Command + R (或 F5)
   ```

2. **点击页面任意位置**
   - 可以点击页面背景
   - 或点击 "Start Listening" 按钮
   - 甚至按任意键盘按键

3. **开始对话**
   - 点击 "Start Listening"
   - 说话
   - 现在应该能听到 Ani 的声音了！

---

### 方法 2: Chrome 设置允许自动播放

1. 在 Chrome 地址栏输入：
   ```
   chrome://settings/content/sound
   ```

2. 找到 **"允许网站播放声音"**

3. 点击 **"添加"**，输入：
   ```
   http://localhost:8000
   ```

4. **刷新页面**

---

### 方法 3: Safari（推荐，macOS 最佳）

Safari 对音频自动播放的限制相对宽松：

1. **打开 Safari**

2. 访问：
   ```
   http://localhost:8000
   ```

3. 如果弹出权限请求，选择：
   - ☑ **允许播放声音**
   - ☑ **允许使用麦克风**

4. **点击页面一次激活音频**

5. 开始对话

---

## 🔍 调试方法

### 打开控制台查看日志

按 `Command + Option + I` 打开开发者工具，切换到 **Console**。

**正常的音频播放日志：**
```
[AUDIO] Received audio data, length: 123456
[AUDIO] Created blob URL: blob:http://...
[AUDIO] Audio loaded, duration: 2.5
[AUDIO] Attempting to play...
[OK] Play initiated successfully
[OK] Audio playing
[AUDIO] Audio ended
```

**如果被阻止，会显示：**
```
[ERROR] Audio playback failed: NotAllowedError
[ERROR] Error name: NotAllowedError
```
然后会弹出提示框告诉您解决方法。

---

## 🎯 测试音频是否激活

在控制台输入并执行：
```javascript
const testAudio = new Audio('data:audio/wav;base64,UklGRigAAABXQVZFZm10IBIAAAABAAEARKwAAIhYAQACABAAAABkYXRhAgAAAAEA');
testAudio.play().then(() => console.log('✅ 音频已激活')).catch(() => console.log('❌ 音频被阻止'));
```

---

## 📱 不同浏览器的建议

| 浏览器 | 音频支持 | 建议 |
|--------|---------|------|
| **Safari** | ⭐⭐⭐⭐⭐ | 最推荐，限制最少 |
| **Chrome** | ⭐⭐⭐⭐ | 需要先点击页面 |
| **Edge** | ⭐⭐⭐⭐ | 同 Chrome |
| **Firefox** | ⭐⭐⭐ | 较严格 |

---

## ✨ 现在的改进

我已经添加了：

1. **自动音频激活**
   - 用户点击页面任意位置时自动激活音频
   - 无需手动设置

2. **详细的调试日志**
   - 控制台会显示音频播放的每一步
   - 如果失败会显示具体原因

3. **友好的错误提示**
   - 如果音频被阻止，会弹出中文提示
   - 告诉您具体的解决方法

---

## 🚀 最佳实践

**推荐流程：**

1. 使用 **Safari** 浏览器
2. 访问 `http://localhost:8000`
3. **点击页面背景一次**（激活音频）
4. 点击 "🎤 Start Listening"
5. 说 "你好" 或 "Hello"
6. 享受完整的语音对话体验！

---

## 📞 还是没声音？

如果以上方法都不行，请检查：

1. **系统音量**
   - macOS 系统音量是否开启
   - 静音模式是否关闭

2. **浏览器音量**
   - 浏览器标签页是否被静音
   - 右键点击标签页，确保未选中"静音网站"

3. **音频输出设备**
   - 系统设置 → 声音 → 输出
   - 确认选择了正确的扬声器/耳机

4. **控制台错误**
   - 打开开发者工具
   - 查看是否有 `[ERROR]` 相关的音频错误
   - 将错误信息截图反馈

---

🤖 故障排除指南由 [Claude Code](https://claude.com/claude-code) 生成
