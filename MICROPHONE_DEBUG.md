# 麦克风调试指南 (macOS)

## 🔍 调试步骤

### 1. 刷新浏览器页面
```
Command + R (或 F5)
```

### 2. 打开浏览器开发者工具
```
Command + Option + I (Chrome/Edge)
或
Command + Option + C (Safari)
```

### 3. 查看控制台 (Console)
点击 "🎤 Start Listening" 按钮后，观察控制台输出：

**正常情况应该看到：**
```
[DEBUG] Button clicked, isListening: false
[DEBUG] WebSocket state: 1
[DEBUG] Starting mic streaming...
[DEBUG] startMicStreaming called
[DEBUG] Requesting microphone access...
[OK] Microphone access granted
```

**如果出现错误，会显示具体错误信息**

## 🛠️ macOS 麦克风权限设置

### Safari 浏览器
1. 打开 **系统设置** (System Settings)
2. 点击 **隐私与安全性** (Privacy & Security)
3. 点击 **麦克风** (Microphone)
4. 确保 **Safari** 已勾选

### Chrome/Edge 浏览器
1. 打开 **系统设置** (System Settings)
2. 点击 **隐私与安全性** (Privacy & Security)
3. 点击 **麦克风** (Microphone)
4. 确保 **Google Chrome** 或 **Microsoft Edge** 已勾选

### 浏览器内权限
当点击按钮时，浏览器地址栏会弹出权限请求：
```
localhost 想要使用您的麦克风
[阻止] [允许]
```
**务必点击 [允许]**

## 🚨 常见错误及解决方案

### 错误 1: NotAllowedError
```
麦克风访问失败: Permission denied
```
**解决方案：**
- 检查浏览器地址栏是否有麦克风图标（被禁止）
- 点击图标，选择"允许访问麦克风"
- 刷新页面重试

### 错误 2: NotFoundError
```
麦克风访问失败: Requested device not found
```
**解决方案：**
- 检查 MacBook 内置麦克风是否正常工作
- 打开"系统设置 → 声音 → 输入"，确认有可用麦克风
- 尝试在其他应用（如语音备忘录）测试麦克风

### 错误 3: NotReadableError
```
麦克风访问失败: Could not start audio source
```
**解决方案：**
- 其他应用可能正在使用麦克风
- 关闭 Zoom、Teams、Discord 等语音应用
- 重启浏览器

### 错误 4: WebSocket not connected
```
[ERROR] WebSocket not connected: null
```
**解决方案：**
- 服务器未运行，执行 `./start_server.sh`
- 检查是否访问 `http://localhost:8000`

## 🧪 测试麦克风

### 方法 1: 浏览器内置测试
在控制台执行：
```javascript
navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    console.log('✅ 麦克风工作正常');
    stream.getTracks().forEach(t => t.stop());
  })
  .catch(err => console.error('❌ 麦克风错误:', err));
```

### 方法 2: 系统录音测试
1. 打开 **QuickTime Player**
2. 选择 **文件 → 新建音频录制**
3. 测试是否能录音

## 📊 浏览器兼容性

| 浏览器 | macOS 支持 | 推荐 |
|--------|-----------|------|
| Safari | ✅ 最佳 | ⭐⭐⭐⭐⭐ |
| Chrome | ✅ 很好 | ⭐⭐⭐⭐ |
| Edge | ✅ 很好 | ⭐⭐⭐⭐ |
| Firefox | ✅ 良好 | ⭐⭐⭐ |

**推荐使用 Safari**，因为它是 macOS 原生浏览器，麦克风权限管理最流畅。

## 🔧 高级诊断

### 检查可用设备
在控制台执行：
```javascript
navigator.mediaDevices.enumerateDevices()
  .then(devices => {
    console.log('可用设备:');
    devices.forEach(d => console.log(d.kind, d.label));
  });
```

### 检查 WebSocket 连接
在控制台执行：
```javascript
console.log('WebSocket 状态:', window.ani ? 'Ready' : 'Not loaded');
```

## 📝 报告问题

如果以上方法都无法解决，请提供：
1. macOS 版本
2. 浏览器名称和版本
3. 控制台完整错误日志
4. 系统麦克风权限截图

---

🤖 调试指南由 [Claude Code](https://claude.com/claude-code) 生成
