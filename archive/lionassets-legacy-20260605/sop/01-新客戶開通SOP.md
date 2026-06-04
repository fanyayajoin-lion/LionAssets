# 新客戶開通 SOP

預計時間：15-20 分鐘
客戶不需要做任何技術設定，全由你操作。

---

## 前置作業（客戶端，5分鐘）

請客戶：
1. 下載 Telegram，申請帳號
2. 在 @BotFather 建立新 Bot，把 Token 傳給你
3. 傳任意訊息給新 Bot，然後傳 `/myid`，把 Chat ID 傳給你

---

## 步驟 1：Fork Repo（3 分鐘）

1. 進入 `https://github.com/fanyayajoin-lion/LionBrain`
2. 點右上角 **Fork**
3. Repo 名稱改為 `[客戶代號]-brain`（例：caiqibrain）

---

## 步驟 2：Zeabur 新服務（5 分鐘）

1. Zeabur → 新增 Service → GitHub → 選剛 fork 的 repo
2. 填入以下 4 個環境變數：

```
TELEGRAM_TOKEN      = 客戶的 Bot Token
TELEGRAM_CHAT_ID    = 客戶的 Chat ID
GEMINI_API_KEY      = （你的共用 key）
GITHUB_TOKEN        = （你的 GitHub Token）
GITHUB_OWNER        = fanyayajoin-lion
GITHUB_REPO         = caiqibrain（剛才的 repo 名稱）
ANTHROPIC_API_KEY   = （你的 Claude key）
```

3. Deploy，等部署完成（約 2 分鐘）

---

## 步驟 3：驗收（2 分鐘）

請客戶傳以下訊息給 Bot，確認正常：
- 傳一句文字 → 應收到「✅ 已存入」
- 傳 `/test` → 應收到早報
- 傳 `/myid` → 應顯示 Chat ID

---

## 步驟 4：如有加購 CRM 模組（2 分鐘）

在 fork 的 repo 新增一個檔案：
- 路徑：`clients/README.md`
- 內容：`# 客戶資料庫`

重新部署後 CRM 自動啟用。
傳給客戶 CRM 使用說明（見 `sop/03-CRM模組.md`）。

---

## 交付訊息範本（複製傳給客戶）

```
🦁 你的管家 Bot 已就緒！

每天早上 8 點會推送早報。

【平時怎麼用】
直接傳文字/語音/圖片/連結 → 自動記錄整理
問問題 → 它查你的資料庫回答你

【指令】
/status → 案子狀態 + 代辦事項
/test   → 立即收一份早報
```
