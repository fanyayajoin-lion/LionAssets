# 30 分鐘建好你的 Hermes

## 一句話理解
跟着這篇一步一步做，30 分鐘內你就能擁有一個 24 小時工作的 AI 助理。

## 這是什麼
這篇教你從零開始，在電腦上安裝並設定 Hermes。完成後，你可以隨時跟你的 AI 助理對話，他會記住你說過的話。

## 為什麼需要
一般 AI（ChatGPT、Claude）關掉就忘了你。Hermes 讓你：
- 關掉電腦後 AI 還在跑（裝在雲端）
- 隨時透過手機跟 AI 對話（Telegram Bot）
- AI 會記住你的喜好和歷史對話

## 生活比喻
就像**安裝手機 App**：
1. 下載 App
2. 註冊帳號
3. 設定偏好
4. 開始使用

Hermes 的安裝也差不多，只是多了一兩個步驟。

## 安裝前準備

### 你需要什麼
1. **一台電腦**（Windows、Mac、Linux 都可以）
2. **穩定的網路連線**
3. **一個 AI 模型的 API Key**（見下方說明）

### 選 AI 模型（大腦）
Hermes 需要一個「大腦」來思考。你選一個就好：

| 模型 | 費用 | 優點 | 適合誰 |
|------|------|------|--------|
| **GPT-4o**（OpenAI） | 約 NT$1,200/月 | 最多人用，功能最全 | 新手首選 |
| **Claude Sonnet**（Anthropic） | 約 NT$1,200/月 | 寫文案很強 | 內容創作者 |
| **Gemini Pro**（Google） | 免費額度 | 便宜 | 預算有限 |
| **DeepSeek** | 約 NT$300/月 | 超便宜 | 省錢首選 |

**建議**：如果你是新手，先用 **GPT-4o** 或 **Claude Sonnet**。

### 取得 API Key
以 GPT-4o 為例：
1. 打開 https://platform.openai.com
2. 註冊帳號
3. 進入 API Keys 頁面
4. 建立一個新的 Key
5. **複製 Key 並存在安全的地方**（不要告訴別人）

其他模型的 API Key 取得方式類似，都在他們的官方網站上。

## 安裝步驟

### 步驟 1：安裝 Hermes

打開終端機（Terminal）：

**Windows 用戶：**
1. 打開 PowerShell 或 Windows Terminal
2. 貼上這行指令並按 Enter：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

**Mac / Linux 用戶：**
1. 打開 Terminal
2. 貼上同樣的指令：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安裝過程大約需要 2-5 分鐘，請耐心等待。

### 步驟 2：初始設定

安裝完成後，輸入：

```bash
hermes setup
```

系統會問你幾個問題：

**問題 1：你想用哪個 AI 模型？**
- 輸入 `openai`（如果你用 GPT-4o）
- 或輸入 `anthropic`（如果你用 Claude）

**問題 2：你的 API Key 是什麼？**
- 貼上你剛才複製的 API Key
- 系統不會顯示你輸入的內容（這是正常的）

**問題 3：你想用哪個通訊平台？**
- 如果只是想在本機用，選 `cli`（終端機模式）
- 如果想用手機，選 `telegram`（需要額外設定，見進階篇）

### 步驟 3：測試

輸入：

```bash
hermes
```

如果看到歡迎畫面，表示安裝成功！

試著輸入：

```
你好，請自我介紹
```

如果 AI 回答了，恭喜！你的 Hermes 已經可以用了。

## 常見錯誤

### 錯誤 1：curl 指令找不到
**原因**：Windows 的 PowerShell 可能沒有 curl。

**解法**：改用 wget：
```bash
wget -qO- https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### 錯誤 2：API Key 錯誤
**原因**：Key 輸錯或過期。

**解法**：
1. 回到 AI 模型的官方網站，重新產生一個 Key
2. 輸入 `hermes setup model` 重新設定

### 錯誤 3：安裝過程中斷
**原因**：網路不穩。

**解法**：重新執行安裝指令即可，Hermes 會自動跳過已完成的步驟。

## 壞掉會怎樣
如果 Hermes 壞了：
1. 你的 AI 模型（ChatGPT、Claude）還是正常的
2. 重新安裝 Hermes 就好
3. 你的設定檔在 `~/.hermes/` 目錄，重新安裝後會自動讀取

## 技術補充
- 安裝路徑：`~/.hermes/`
- 設定檔：`~/.hermes/config.yaml`
- API Key：`~/.hermes/.env`
- 日誌：`~/.hermes/logs/`
- 更新 Hermes：`hermes update`
