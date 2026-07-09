# 選你的 AI 大腦（Provider 設定）

## 一句話理解
Hermes 本身不會思考，他需要請一個「AI 大腦」來幫忙。這篇教你選最適合你的 AI 模型。

## 這是什麼
**Provider** 就是 Hermes 請來思考的 AI 模型。Hermes 像總經理，Provider 像專家廚師。

你可以隨時更換 Provider，就像換廚師一樣。

## 為什麼需要選
不同的 AI 模型有不同專長：
- **GPT-4o**：綜合能力最強，適合大多數人
- **Claude Sonnet**：寫文案、分析很強
- **Gemini Pro**：便宜，適合預算有限
- **DeepSeek**：超便宜，適合測試

## 生活比喻
想像你在選**外送平台**：

- **GPT-4o** = 高級餐廳（好吃但貴）
- **Claude Sonnet** = 精緻餐飲（適合特殊場合）
- **Gemini Pro** = 平價美食（便宜又好吃）
- **DeepSeek** = 便利商店（最便宜，基本需求滿足）

你可以同時訂多家外送，Hermes 會幫你選最合適的那家。

## 如何更換 Provider

### 方法 1：使用指令（推薦）

輸入：
```bash
hermes model
```

系統會列出所有可用的模型，你選一個就好。

### 方法 2：編輯設定檔

輸入：
```bash
hermes config edit
```

找到 `model:` 區塊，修改 `provider` 和 `api_key`。

## 常用 Provider 比較

| Provider | 代表模型 | 費用 | 優點 | 缺點 |
|----------|----------|------|------|------|
| **OpenAI** | GPT-4o | 中高 | 功能最全，文檔最多 | 費用較高 |
| **Anthropic** | Claude Sonnet | 中高 | 寫文案強，上下文長 | 台灣用戶較少 |
| **Google** | Gemini Pro | 低 | 免費額度多 | 功能較少 |
| **DeepSeek** | DeepSeek V3 | 很低 | 超便宜 | 中文能力較弱 |
| **xAI** | Grok | 中 | 即時新聞 | 中文能力弱 |

## 常見錯誤

### 錯誤 1：API Key 過期
**症狀**：Hermes 回應「API Key 錯誤」

**解法**：
1. 回到 Provider 的官方網站
2. 重新產生 API Key
3. 輸入 `hermes setup` 更新 Key

### 錯誤 2：模型選錯了
**症狀**：Hermes 回應很慢或答非所問

**解法**：
```bash
hermes model
```
選一個不同的模型。

### 錯誤 3：免費額度用完了
**症狀**：Hermes 回應「速率限制」

**解法**：
1. 等待下一個月（很多 Provider 按月重置額度）
2. 或換一個 Provider

## 壞掉會怎樣
如果 Provider 壞了（例如 OpenAI 伺服器當機）：
1. Hermes 會自動嘗試其他你設定的備用模型
2. 或者你可以手動切換：`hermes model` 選另一個

## 技術補充
- 支援 20+ 家 Provider
- 可以在 config.yaml 設定多個 Provider，Hermes 會自動輪詢
- 更換 Provider 不需要重新安裝 Hermes
