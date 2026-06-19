# 群獅靈感知識庫

這是群獅的 Codex + Obsidian 通用自生長知識庫，不綁單一 LLM。Codex、Claude Code 或其他 AI 只要讀到 `AGENTS.md` / `CLAUDE.md`，就能理解規則並接手。

## 四層使用邏輯

```text
Telegram / Hermes = 老闆隨手丟資料
Discord = 老闆看今天系統處理到哪
Obsidian = 老闆搜尋、判斷、沉澱知識
GitHub = 備份與跨 AI 接手
```

正式知識庫路徑固定為：`D:\pcsfanfan\LB群獅靈感知識`。

## 核心流程

```text
靈感收集 -> Hermes Inbox -> AI 閱讀員 -> Obsidian 知識庫 -> 商業蒸餾 -> 輸出 -> 回流 -> Skill / Asset / Memory
```

## 資料夾

- `inbox/raw/`：Hermes 收到但還沒整理的東西，全部不分類。
- `inbox/processed/`：AI 閱讀員整理後的「老闆理解版」。
- `inbox/needs-review/`：YT 讀不到、網頁抓不到、OCR 失敗、需要補充的資料。
- `raw/`：值得長期保存的原始資料，不修改、不刪除。
- `wiki/`：AI 整理後的正式知識層。
- `wiki/concepts/`：框架、方法論、商業洞察。
- `wiki/entities/`：人、品牌、工具、客戶、平台。
- `wiki/notes/`：單篇資料摘要與老闆理解。
- `wiki/synthesis/`：跨來源蒸餾、決策結晶。
- `workflows/`：Hermes 收件、AI 閱讀、Discord 顯示、知識入庫、內容工廠等流程。
- `skills/`：可重複調用的能力卡。
- `outputs/threads/`：Threads 草稿。
- `outputs/facebook/`：Facebook 長文草稿。
- `outputs/ig-carousel/`：IG 輪播大綱。
- `assets/`：圖片、附件、PPT、影片素材。
- `archive/`：舊 LionAssets 備份與歷史封存。

## AI 使用方式

1. 先讀 `AGENTS.md` 與 `index.md`。
2. 若任務來自 Hermes，先判斷是在 `inbox/raw/`、`inbox/processed/` 還是正式 `wiki/`。
3. 需要找資料時，依序查：`index.md -> hot.md -> wiki/synthesis -> wiki/concepts -> wiki/notes -> inbox/processed`。
4. 不要先查 `raw/`，除非要回查原始來源。
5. 產出內容後必須回流到 `wiki/notes/` 或 `wiki/synthesis/`。
6. 任務結束前更新需要的 `index.md`、`hot.md`，並 append `log.md`。

## GitHub

遠端：`https://github.com/fanyayajoin-lion/LionAssets`

覆蓋推送前，先把遠端舊內容備份到 `archive/`。
