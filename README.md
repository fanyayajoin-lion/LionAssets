# 群獅靈感知識庫

這是群獅的 Codex + Obsidian 通用自生長知識庫，不綁單一 LLM。Codex、Claude Code 或其他 AI 只要讀到 `AGENTS.md` / `CLAUDE.md`，就能理解規則並接手。

## 為什麼需要它

老闆常遇到這些問題：

- 靈感碎片散落在 Telegram、Discord、對話紀錄裡，找不到、記不住
- 換一個 AI 工具（ChatGPT → Claude → Gemini），所有知識要重新教一遍
- 知識沒結構，累積越多越亂，變成垃圾場

LionAssets 就是解決這個問題的第二大腦：碎片自動整理、跨 AI 通用、越用越聰明。

## 快速開始

### 1. 讓 AI 接手你的知識庫

打開 ChatGPT / Claude / Gemini，貼上這段話：

```
請讀這個 repo：https://github.com/fanyayajoin-lion/LionAssets
幫我管理我的靈感知識庫。
```

AI 會自動讀取 `AGENTS.md`，了解規則並開始工作。

### 2. 從 Telegram 丟資料進來

把網址、文章、截圖、想法丟到 Telegram 給黑獅，它會自動整理進 `inbox/raw/`。

### 3. 搜尋知識庫

```
@黑獅 @session:default/<id> 找一下關於 XX 的資料
```

或直接到 Obsidian 搜尋。

## 架構

```
Telegram / Hermes = 老闆隨手丟資料
Discord = 老闆看今天系統處理到哪
Obsidian = 老闆搜尋、判斷、沉澱知識
GitHub = 備份與跨 AI 接手
```

正式知識庫路徑固定為：`D:\pcsfanfan\LB群獅靈感知識`。

## 專案結構

```
LionAssets/
├── README.md                    ← 你正在看的檔案
├── AGENTS.md                    ← AI 工作規則（必讀）
├── index.md                     ← 知識庫索引
├── hot.md                       ← 熱門主題
├── log.md                       ← 操作紀錄
├── inbox/                       ← 收件匣
│   ├── raw/                     ← 原始資料（不修改）
│   └── processed/               ← AI 整理後的版本
├── wiki/                        ← 正式知識層
│   ├── concepts/                ← 框架、方法論
│   ├── entities/                ← 人、品牌、工具
│   ├── notes/                   ← 單篇摘要
│   └── synthesis/               ← 跨來源洞察
├── workflows/                   ← 每日蒸餾、剪藏、週報流程
├── skills/                      ← 可重複調用的能力卡
├── prompts/                     ← 提示詞庫
├── outputs/                     ← 產出（文章、PPT、圖片）
├── assets/                      ← 附件素材
└── archive/                     ← 歷史封存
```

## 部署

本 repo 是純 Markdown 知識庫，不需要特別部署。

1. 克隆到本地：`git clone git@github.com:fanyayajoin-lion/LionAssets.git`
2. 安裝 Obsidian，開啟該目錄
3. 設定黑獅 cron job 自動同步

## 常見問題

**Q：AI 可以自動整理嗎？**
A：可以。Hermes Agent 會自動讀 `inbox/raw/`、分類、連結、寫入 `wiki/`。

**Q：我可以商用嗎？**
A：可以。這套知識庫的設計初衷就是讓一人創業者用 AI 管理知識。

**Q：換 AI 工具要重設嗎？**
A：不用。所有規則寫在 `AGENTS.md`，任何 AI 讀到就能接手。

## 授權

MIT

---

*群獅整合行銷 — 傳產翻譯機*
