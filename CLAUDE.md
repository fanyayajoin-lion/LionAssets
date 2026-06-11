# 群獅靈感知識庫 Claude Code 規則

請先讀 `AGENTS.md`，並完全遵守其中的通用 AI 工作規則。本檔只補充 Claude Code 使用時的提醒。

## 必做

- 稱呼使用者為老闆。
- 任務前先讀 `index.md`。
- 依任務類型讀取相關 `workflows/` 與 `skills/`。
- `raw/` 不修改、不刪除、不覆蓋。
- 產出內容後必須回流到 `wiki/notes/` 或 `wiki/synthesis/`。
- 任務後更新需要的 `index.md`、`hot.md`，並 append `log.md`。
- 同一類工作出現 3 次以上，必須提名 skill candidate，等老闆確認後再寫入 `skills/`。

## 不做

- 不把 API Key、密碼、token 寫進檔案。
- 不為了分類新增過深資料夾。
- 不只摘要資料；要補上商業判斷、可複用框架與下一步。
- 不把 `outputs/` 當終點，輸出必須回流。

## Hermes / Discord / Obsidian 分工

- Hermes 是知識庫前門，負責收件、預處理、狀態回報。
- Discord 是顯示層，只顯示收件、整理、待補資料、入庫與輸出狀態，不當正式知識庫。
- Obsidian markdown 是正式知識庫，搜尋與判斷以 `index.md`、`hot.md`、`wiki/synthesis/`、`wiki/concepts/`、`wiki/notes/` 為主。
- `inbox/raw/` 完全不分類，只放 Hermes 收到但尚未整理的資料。
- `inbox/processed/` 放 AI 閱讀員整理出的老闆理解版。
- `inbox/needs-review/` 放讀不到、抓不到、OCR 失敗、需要補充的資料。
- 搜尋順序固定為：`index.md -> hot.md -> wiki/synthesis -> wiki/concepts -> wiki/notes -> inbox/processed`。
- 不要先搜 `raw/`，除非需要回查原始來源。
