---
title: "LINE Bot 關鍵字飛輪架構 — 可複製設計模式"
created: 2026-07-23
updated: 2026-07-23
type: concept
tags: [[標籤/Bot架構], [標籤/LINE-Bot], [標籤/飛輪設計]]
sources:
  - "黑獅每日萃取 — Telegram 對話 + LionAIBOT-hermes 實作 2026-07-21"
lion_score:
  變現價值: 5
  可複製性: 5
  長期價值: 4
  顧問可用性: 4
  內容延展性: 4
---

# LINE Bot 關鍵字飛輪架構 — 可複製設計模式

## 核心洞察

LINE Bot 的請求處理應該走「飛輪式」分流，不是全部丟給 AI。這樣可以：
1. 節省 API 成本（直接回覆的不走 AI）
2. 保證一致性（固定文案不會跑版）
3. 提高速度（JSON 比 LLM 快得多）

## 四層飛輪架構

```
使用者輸入
    ↓
1. /問答、/排行          → 直接處理，不走 AI
2. 管理指令              → 只有 admin 能用
3. 關鍵字匹配（挑戰、手冊…）→ 從 JSON 讀固定回覆，代入變數 ←【核心創新】
4. 以上都沒有            → 丟給 Hermes AI 自由回答
```

## 關鍵技術實現

### 關鍵字匹配 JSON 結構

```json
{
  "挑戰": {
    "template": "你的挑戰是：{challenge_text}\n建議解法：{solution}",
    "variables": ["challenge_text", "solution"]
  },
  "手冊": {
    "template": "操作手冊內容...",
    "variables": []
  }
}
```

### Python 實作邏輯

```python
flywheel_replied = False
kw_path = os.environ.get("KEYWORD_REPLIES_FILE", "/app/keyword_replies.json")

if user_message in keywords:
    reply = load_and_fill_template(kw_path, user_message, variables)
    send_reply(reply)
    flywheel_replied = True

if not flywheel_replied:
    # 丟給 Hermes AI
    ai_response = hermes_chat(user_message)
    send_reply(ai_response)
```

## 部署與備份流程

1. Patch line_adapter.py → 套上 flywheel 程式碼（line 600+ 有 flywheel 關鍵字匹配）
2. Docker 重啟容器 → `docker restart lineGroup-BOT-AIclass`
3. 備份到 GitHub → `LionAIBOT-hermes` repo
4. SSH 拉取最新檔案確認 patch 生效 → `grep -c 'flywheel_replied' line_adapter.py`

## 已知問題與修復

| 問題 | 原因 | 解法 |
|------|------|------|
| Patch marker 找不到 | 原始檔案與預期格式不符 | 先 grep 確認現有程式碼再 patch |
| SCP 跨機器失敗 | SSH host key 未記錄 | 改用 `ssh cat > local_file` 替代 |
| Git force push 被拒 | 安全檢查 | 需老闆 approval 後執行 |

## 對群獅的價值

這個架構可以複製到所有 LINE Bot 專案：
- 命理 AI Bot
- 香料大叔客服 Bot
- 任何需要「部分固定回覆 + 部分 AI 自由回答」的場景

**關鍵原則：能不用 AI 就不用 AI，省錢又快速。**

## 雙向連結

- [[wiki/concepts/Bot後台系統架構設計]] — Bot 後台多 Profile 管理架構
- [[wiki/entities/電腦王阿達]] — 自動化引流案例中的 Bot 應用
- [[skills/業萱文風]] — Bot 固定回覆的語氣參考
