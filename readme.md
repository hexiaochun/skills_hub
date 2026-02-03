# Skills Hub

> **让通用 AI 编辑器瞬间学会画图、做视频**
> 
> 无需写代码 · 不用记提示词 · 说话即创作

专为 AI Agent 打造的多模态扩展，将复杂的图像生成、视频制作、语音合成能力封装为 Agent 可理解的技能。

## 核心概念

| 概念 | 说明 |
|------|------|
| **MCP 协议** | 万能遥控器，让 AI 编辑器能"操控"各种画图、做视频的工具 |
| **Skills 技能书** | 预置专家级 Prompt，教 Agent "怎么用"这些工具，无需人工干预 |
| **一键安装** | 像安装 App 一样简单，复制一行命令，自动配置好一切环境 |

---

## 快速开始

### 第 1 步：获取 API Key

访问 [速推AI](https://www.51sux.com) 注册账号，免费获取你的专属密钥。

### 第 2 步：一键安装

**Mac / Linux**

```bash
curl -fsSL https://api.51sux.com/install-mcp.sh | bash -s -- YOUR_API_KEY
```

**Windows (PowerShell)**

```powershell
irm https://api.51sux.com/install-mcp.ps1 -OutFile install-mcp.ps1; powershell -ExecutionPolicy Bypass -File .\install-mcp.ps1 -ApiKey "YOUR_API_KEY"
```

> 将 `YOUR_API_KEY` 替换为你的实际 API Key

### 第 3 步：开始对话

重启 Cursor / Claude Desktop，直接用自然语言对话：

```
用户: 帮我画一只可爱的猫咪在花园里玩耍
AI: [自动调用 Flux 2 Flash 生成图片]

用户: 把这张图片做成 10 秒的视频，让猫咪跑起来
AI: [自动调用 Wan 2.6 生成视频]

用户: 帮我把这段文字转成语音
AI: [自动调用 MiniMax TTS 合成语音]
```

---

## 功能概览

| 分类 | Skills 数量 | 说明 |
|------|-------------|------|
| 🎨 图像生成 | 4 | 多模型文生图、图像编辑 |
| 🎬 视频生成 | 3 | 文生视频、图生视频、视频重混 |
| 🎤 语音合成 | 2 | TTS、多人对话、声音克隆 |
| 🔧 工具 | 4 | 视频解析、图片上传、积分充值 |
| 🛠️ 开发辅助 | 3 | 模型接入、测试、前端设计 |

---

## 🎨 图像生成

### Flux 2 Flash

**路径**: `flux2-flash`

使用 Black Forest Labs 的 FLUX.2 模型进行文生图和图像编辑。

| 功能 | 说明 |
|------|------|
| 文生图 | 根据提示词生成高质量图像 |
| 图像编辑 | 提供图片后自动切换为编辑模式 |

- **触发词**: flux 2、FLUX.2、文生图、图像编辑
- **计费**: 2 积分/张

---

### Nano Banana Pro

**路径**: `nano-banana-pro`

Google 最新的高质量图像生成模型，擅长写实风格和文字渲染。

| 功能 | 说明 |
|------|------|
| 文生图 | 写实风格图像生成 |
| 图像编辑 | 支持多图参考编辑 |
| 文字渲染 | 支持在图像中生成文字 |

- **触发词**: nano banana、Google 图像生成
- **计费**: 60 积分/张
- **分辨率**: 1K / 2K / 4K

---

### Seedream 4.5

**路径**: `seedream-image`

字节跳动 Seedream 4.5 模型，支持文生图和多图引用编辑。

| 功能 | 说明 |
|------|------|
| 文生图 | 支持自动 2K/4K 分辨率 |
| 图生图 | 使用 Figure 1/2/3 引用多张参考图 |

- **触发词**: seedream、字节跳动图像生成
- **特点**: 支持最多 10 张参考图

---

### 水浒传故事小人书

**路径**: `nano-pro-shuihu`

使用 Nano Banana Pro 生成手绘卡通风格的水浒传故事信息图。

| 功能 | 说明 |
|------|------|
| 故事信息图 | 输入故事内容，生成手绘风格信息图 |
| HTML 展示 | 自动生成精美的展示页面 |

- **触发词**: 水浒传、小人书、信息图

---

## 🎬 视频生成

### Sora 2

**路径**: `sora-2`

OpenAI Sora 2 视频生成模型，支持文生视频、图生视频和视频重混。

| 模型 | 分辨率 | 功能 |
|------|--------|------|
| text-to-video | 720p | 文生视频 |
| image-to-video | 720p | 图生视频 |
| text-to-video/pro | 1080p | 高清文生视频 |
| image-to-video/pro | 1080p | 高清图生视频 |
| video-to-video/remix | - | 视频风格重混 |

**计费**:
| 版本 | 单价 | 4秒 | 8秒 | 12秒 |
|------|------|-----|-----|------|
| 标准版 720p | 40积分/秒 | 160 | 320 | 480 |
| Pro 1080p | 200积分/秒 | 800 | 1600 | 2400 |

- **触发词**: sora、OpenAI 视频生成、文生视频、图生视频

---

### Wan 2.6

**路径**: `wan-video`

先进的视频生成模型，支持图生视频和参考视频生成（R2V）。

| 模型 | 功能 | 说明 |
|------|------|------|
| image-to-video | 图生视频 | 标准版，画质更优 |
| image-to-video/flash | 图生视频 | Flash 版，高性价比 |
| reference-to-video | R2V | 使用参考视频保持主体一致性 |

**特色功能**:
- 多镜头视频生成 (`multi_shots`)
- 主体一致性（使用 @Video1/@Video2 引用）
- 支持背景音乐

**计费**:
| 模型 | 720p | 1080p |
|------|------|-------|
| 标准版 | 40积分/秒 | 60积分/秒 |
| Flash | 20积分/秒 | 30积分/秒 |

- **触发词**: wan、Wan 2.6、图生视频、图片动起来

---

### 速推AI

**路径**: `sutui-ai`

统一的 AI 生成入口，支持多种模型。

| 功能 | 推荐模型 | 工具 |
|------|---------|------|
| 图像生成 | Flux 2 Flash | `submit_task` + `get_task` |
| 视频生成 | jimeng-video-3.5-pro | `sync_generate_video` |
| 快速图像 | jimeng-4.5 | `sync_generate_image` |

- **触发词**: 画图、生成图片、制作视频

---

## 🎤 语音合成

### 海螺语音合成

**路径**: `minimax-audio`

MiniMax（海螺）API 语音合成服务。

| 功能 | 工具 | 费用 |
|------|------|------|
| 语音合成 | `text_to_audio` | 1积分/千字符 |
| 语音设计 | `voice_design` | 5积分/次 |
| 声音克隆 | `voice_clone` | 10积分/次 |
| 音色列表 | `list_voices` | 免费 |

**常用音色**:
| voice_id | 名称 |
|----------|------|
| male-qn-qingse | 青涩男声 |
| female-shaonv | 少女音 |
| presenter_male | 男主播 |
| presenter_female | 女主播 |

- **触发词**: 语音合成、TTS、声音克隆、音色设计

---

### 多人对话语音合成

**路径**: `minimax-tts`

生成多人对话剧本，自动匹配音色合成语音，输出完整长音频和 HTML 展示页面。

| 功能 | 说明 |
|------|------|
| 剧本生成 | 根据场景自动创作对话 |
| 音色匹配 | 智能匹配角色音色 |
| 情绪增强 | 自动添加语气词 |
| 音频合并 | 输出完整长音频 |

- **触发词**: 多人对话、对话合成

---

## 🔧 工具

### 视频链接解析

**路径**: `parse-video`

解析各大平台视频分享链接，获取无水印下载地址。**免费使用**。

**支持平台**: 抖音、快手、小红书、B站、微博、TikTok、Instagram、YouTube 等

| 工具 | 说明 |
|------|------|
| `parse_video` | 解析视频链接 |
| `download.py` | 下载到本地 |

- **触发词**: 下载视频、解析链接、去水印

---

### 图片上传（云存储）

**路径**: `upload-image`

上传图片到云存储，获取 CDN 加速的 URL。**免费使用**。

| 方式 | 说明 |
|------|------|
| Base64 上传 | 本地图片 → URL |
| URL 转存 | 网络图片 → 稳定 URL |

- **CDN 域名**: `https://cdn-video.51sux.com`
- **触发词**: 上传图片、获取图片 URL

---

### Catbox 图床上传

**路径**: `upload-to-catbox`

上传图片到 catbox.moe 免费图床。

**自动触发场景**:
- 图像编辑任务但输入是本地图片
- AI 模型需要图片 URL 但输入是本地文件

```bash
curl -F'reqtype=fileupload' -F'fileToUpload=@/path/image.png' https://catbox.moe/user/api.php
```

- **特点**: 免费、永久存储、最大 200MB
- **触发词**: catbox、本地图片路径

---

### 积分充值

**路径**: `points-recharge`

积分充值助手，自动获取套餐列表并生成支付二维码。

| 步骤 | 工具 |
|------|------|
| 获取套餐 | `list_points_packages` |
| 生成二维码 | `create_payment_qrcode` |
| 查询余额 | `get_balance` |

- **积分比例**: 1元 = 100积分
- **触发词**: 余额不足、充值积分、查看套餐

---

## 🛠️ 开发辅助

### 添加 Fal 模型

**路径**: `add-fal-model`

指导如何将新的 Fal AI 模型集成到 V3 API 系统。

**添加流程**:
1. 模型注册（model_registry.py）
2. 创建执行器（executors/）
3. 注册执行器（factory.py）
4. 创建 Skill 文件
5. 测试验证

**价格换算**: 1 美元 = 400 积分

- **触发词**: 添加 fal 模型、配置新模型

---

### 模型价格测试

**路径**: `pricing-test`

测试和校验模型的定价信息和实际扣费。

| 测试项 | 说明 |
|--------|------|
| 定价展示 | 验证 API 返回的价格信息 |
| 实际扣费 | 验证任务创建时的扣费金额 |
| 批量测试 | 运行测试脚本验证 |

- **触发词**: 价格测试、扣费测试

---

### 图像模型效果评估

**路径**: `image-model-evaluation`

对图像生成模型进行全面的效果评估，生成 HTML 测试报告。

| 测试类型 | 测试项 | 耗时 |
|---------|--------|------|
| 快速测试 | 10 项 | 3-5 分钟 |
| 完整测试 | 31 项 | 15-20 分钟 |

**测试维度**: 文生图、图生图、尺寸、风格、人物一致性

- **触发词**: 测试模型、评估模型

---

### 前端设计

**路径**: `frontend-design`

创建高质量、有辨识度的前端界面，避免 AI 通用风格。

**设计原则**:
- 独特的字体选择（避免 Inter、Arial）
- 大胆的色彩方案
- 精心设计的动效和交互
- 创意布局和排版

- **触发词**: 创建网页、设计界面、美化 UI

---

## 使用方式

所有 Skills 通过 MCP 工具调用，主要使用以下模式：

### 异步任务模式（推荐）

```json
// 1. 提交任务
{
  "server": "user-速推AI",
  "toolName": "submit_task",
  "arguments": {
    "model_id": "模型ID",
    "parameters": { ... }
  }
}

// 2. 查询结果
{
  "server": "user-速推AI",
  "toolName": "get_task",
  "arguments": {
    "task_id": "任务ID"
  }
}
```

### 同步模式

部分工具支持同步调用，直接返回结果：
- `sync_generate_image` - 同步图像生成
- `sync_generate_video` - 同步视频生成
- `text_to_audio` - 语音合成
- `parse_video` - 视频解析

---

## 目录结构

```
.cursor/skills/
├── add-fal-model/          # 添加 Fal 模型
├── flux2-flash/            # Flux 2 图像生成
├── frontend-design/        # 前端设计
├── image-model-evaluation/ # 模型评估
├── minimax-audio/          # 语音合成
├── minimax-tts/            # 多人对话
├── nano-banana-pro/        # Nano Banana 图像
├── nano-pro-shuihu/        # 水浒传小人书
├── parse-video/            # 视频解析
├── points-recharge/        # 积分充值
├── pricing-test/           # 价格测试
├── seedream-image/         # Seedream 图像
├── sora-2/                 # Sora 视频
├── sutui-ai/               # 速推AI
├── upload-image/           # 图片上传
├── upload-to-catbox/       # Catbox 图床
└── wan-video/              # Wan 视频
```

---

## 许可

各 Skill 可能有不同的许可协议，请查看各 Skill 目录下的 LICENSE 文件。
