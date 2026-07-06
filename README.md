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
你丟碎片（Telegram）→ AI 預摘要 + 連結 → 回傳 Telegram
     ↓
你補充判斷邏輯（故事/想法/策略）
     ↓
AI 萃取進 wiki（包含你的判斷 = 思維模型）
     ↓
知識複利（新碎片更新現有頁面，不是新增）
     ↓
每週提取靈感 → 同步 Notion 展示
```

## 資料夾

- `inbox/raw/`：Hermes 收到但還沒整理的東西，全部不分類。
- `inbox/processed/`：AI 閱讀員整理後的「老闆理解版」。
- `raw/`：值得長期保存的原始資料，不修改、不刪除。
- `wiki/`：AI 整理後的正式知識層。
- `wiki/concepts/`：框架、方法論、商業洞察。
- `wiki/entities/`：人、品牌、工具、客戶、平台。
- `wiki/notes/`：單篇資料摘要與老闆理解。
  - `wiki/notes/業老闆個人檔案.md` — 完整個人檔案（持續更新）
  - `wiki/notes/業老闆的人類圖行動指南.md` — 人類圖詳細指南
  - `wiki/notes/業老闆寫文風格特徵卡.md` — AI 產出內容時的語氣參考
- `wiki/synthesis/`：跨來源蒸餾、決策結晶。
- `wiki/inspiration/`：每週從 wiki 提取的靈感素材（長文素材庫）。
- `workflows/`：碎片接收、知識萃取、每日提問、每週總整理、靈感提取、Notion 同步等流程。
- `skills/`：可重複調用的能力卡。
- `prompts/`：好用的提示詞庫，供各種 AI 工具參考。
- `outputs/`：文章、PPT、圖片提示詞、影片腳本、HTML 看板等產出。
- `assets/`：圖片、附件、PPT、影片素材。
- `archive/`：舊 LionAssets 備份與歷史封存。

## AI 使用方式

1. 先讀 `AGENTS.md` 與 `index.md`。
2. 若任務來自 Hermes，先判斷是在 `inbox/raw/`、`inbox/processed/` 還是正式 `wiki/`。
3. 需要找資料時，依序查：`index.md -> hot.md -> wiki/synthesis -> wiki/concepts -> wiki/notes -> inbox/processed`。
4. 不要先查 `raw/`，除非要回查原始來源。
5. 產出內容後必須回流到 `wiki/notes/` 或 `wiki/synthesis/`。
6. 任務結束前更新需要的 `index.md`、`hot.md`，並 append `log.md`。
7. 碎片接收：碎片進來 → 預摘要 + 標記來源 + 搜尋 wiki 連結 → 存入 `inbox/processed/` → 回傳 Telegram 通知。
8. 知識複利：新碎片更新現有 wiki 頁面，不是新增。每個頁面必須包含「業萱的判斷邏輯」。
9. AI 行為規則：Lion Score ≥ 4 自動存入 wiki 並通知；≤ 1 不存或只存 notes 備查。

## 其他 AI 如何補充資料進知識庫

如果你是一個 AI（H蝦趴獅、Codex、Claude Code、或其他工具），要往本知識庫丟資料，請遵守以下規則：

### 你要丟到哪？

| 你做的事情 | 丟到哪裡 | 說明 |
|-----------|---------|------|
| 收到網址、文章、YT 影片 | `inbox/raw/` | 建立 Markdown 中繼資料檔 |
| 收到截圖、圖片 | `inbox/raw/` + `assets/` | 中繼資料放 raw，圖檔放 assets |
| 收到文件（PDF、DOC） | `inbox/raw/` + `assets/` | 同上 |
| 收到社群貼文（Threads、IG、FB） | `inbox/raw/` | 貼文內容 + 原始連結 |
| 收到零散想法 | `inbox/raw/` | 用碎片接收格式 |
| 整理後的摘要、分類 | **不要寫** | 這是管理獅的職責 |
| 更新 wiki 頁面 | **不要寫** | 這是管理獅的職責 |

### 原始檔命名規則

```
inbox/raw/YYYYMMDD-HHMMSS-<短識別>.md
```

範例：
```
inbox/raw/20260706-143000-hermes-agent.md
```

### Markdown 中繼資料格式

每筆來源必須包含 YAML frontmatter：

```yaml
---
source_id: "YYYYMMDD-HHMMSS-<short-id>"
source_type: "web|social|image|document|video|note"
source_url: "原始網址"
captured_at: "ISO-8601 時間"
sha256: "檔案 SHA-256（如有附件）"
status: "received"
title: "標題"
excerpt: "一段話摘要（≤200字）"
---

## 原始內容

這裡放截取的正文、貼文內容、或附件引用說明。
```

### 附件處理

- 圖片、PDF 等附件放在 `assets/` 目錄
- 附件命名規則：`assets/YYYYMMDD-HHMMSS-<short-id>-<描述>.<副檔名>`
- 中繼資料檔中用 `attachment` 欄位引用附件路徑

### 絕對不要做的事

- ❌ 不要修改 `inbox/raw/` 裡的原始檔
- ❌ 不要直接寫入 `wiki/` 目錄
- ❌ 不要更新 `index.md`、`log.md`
- ❌ 不要執行 Git 操作
- ❌ 不要刪除任何檔案

### 簡單來說

> **你的任務：把資料原封不動丟進 `inbox/raw/`**
> **管理獅的任務：讀取、摘要、分類、寫入 wiki、更新索引**

你不需要判斷資料有沒有價值、要不要分類、怎麼連結。那些都是管理獅的工作。你只需要確保：
1. 資料完整（原文不修改）
2. 來源可追溯（網址、時間、作者）
3. 命名符合規則

### 參考文件

- 詳細規則：`AGENTS.md`
- 工作流程：`workflows/碎片接收.md`
- 收件流程：`workflows/Hermes收件.md`

## GitHub

遠端：`https://github.com/fanyayajoin-lion/LionAssets`

覆蓋推送前，先把遠端舊內容備份到 `archive/`。
