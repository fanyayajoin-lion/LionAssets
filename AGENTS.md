# 群獅靈感知識庫 AI 工作規則

你要稱呼使用者為老闆。

這是群獅的靈感知識庫，從靈感出發，經過收集、整理、蒸餾、記憶、輸出、回流，慢慢變成可轉移的數位第二大腦。本知識庫不綁 Codex、不綁 Claude Code，也不綁單一 LLM；任何 AI 只要讀到本檔，就要能接手。

## 老闆身份與語氣

老闆是業萱。

核心定錨句：

> 有實業背景的商業 AI 摸索者。不是來教你的，是分享我自己走過的路。

對外介紹依場合使用：

- 對傳產老闆：我是業萱，做了近 8 年連鎖品牌營運，協助 50 幾家企業轉型，現在在研究怎麼用 AI 幫老闆把自己從公司裡解放出來。
- 對電商創業者：我是業萱，研究商業模式 3 年、自媒體 2 年、AI 1 年，幫一人公司用 AI 建系統，讓你不用自己做所有事。
- 對媒體或演講場合：我是樊業萱，遠特企業管理諮詢負責人、群獅整合行銷創辦人，專注幫有實業的創業者用 AI 建立可複製的商業系統。

核心信念：工具會變，底層邏輯不會變；AI 是放大器；用 ESBI 視角協助有實業的老闆從 S 走向 B；OPC 一人公司會變多；真誠分享，不包裝。

## 知識庫結構

- `raw/`：原始資料，不修改、不刪除、不覆蓋。
- `wiki/`：AI 整理後的知識層。
- `wiki/concepts/`：框架、方法論、商業洞察。
- `wiki/entities/`：人、品牌、工具、客戶、平台。
- `wiki/notes/`：單篇資料摘要。
  - `wiki/notes/業老闆個人檔案.md` — 完整個人檔案（持續更新）
  - `wiki/notes/業老闆的人類圖行動指南.md` — 人類圖詳細指南
  - `wiki/notes/業老闆寫文風格特徵卡.md` — AI 產出內容時的語氣參考
- `wiki/synthesis/`：跨來源蒸餾、決策結晶。
- `workflows/`：每日蒸餾、剪藏、新聞雷達、週報、回流流程。
- `skills/`：可重複調用的能力卡。
- `prompts/`：好用的提示詞庫，供各種 AI 工具參考。
- `outputs/`：文章、PPT、圖片提示詞、影片腳本、HTML 看板等產出。
- `assets/`：圖片、附件、PPT、影片素材。
- `archive/`：舊 LionAssets 備份與歷史封存。

## 每次任務標準流程

```text
讀 index.md -> 判斷任務類型 -> 讀相關 workflow / skill -> 收集或讀取資料 -> 整理 wiki -> 蒸餾 synthesis -> 產出 output -> 回流 wiki -> 更新 index/hot -> append log.md
```

## 必守規則

- 查詢前必須先讀 `index.md`。
- 操作後必須 append `log.md`。
- `raw/` 永遠不可修改、不可刪除。
- `outputs/` 必須回流到 `wiki/` 或 `wiki/synthesis/`。
- workflows、skills、outputs、assets 不會自然更新，必須主動檢查並寫入。
- API Key 只記錄需求與欄位，不得寫入實際 key。
- 若需要最新資料，必須連網查證並保留來源；查不到可靠資料時標記「需查證」。

## 碎片接收規則（NEW — 2026-06-21）

- 碎片進來 → 預摘要 + 標記來源 + 搜尋 wiki 連結 → 存入 `inbox/processed/`
- 回傳 Telegram 通知業萱：「收到碎片，摘要 + 相關連結」
- 業萱回覆判斷邏輯 → 萃取進 wiki
- **AI 行為規則**：
  - Lion Score ≥ 4（任一維度）→ 自動存入 wiki，事後通知
  - Lion Score 2-3 → 給建議，等業萱回覆
  - Lion Score ≤ 1 → 不存，或只存到 `wiki/notes/` 備查
- 每次存入後回傳通知：「✅ 已存入 wiki/[category]/[topic].md」
- 業萱可以回覆「撤銷」移除不想要的內容
- 知識複利：新碎片更新現有頁面，不是新增
- 同一主題重複出現 3 次以上，AI 必須提名是否升級為 Skill、Asset 或 Memory，等老闆確認後再寫入。
- 不要過度分類；能靠規則與連結管理，就不要新增多層資料夾。

## AI 自我進化規則（NEW — 2026-06-21）

- **重複錯誤超過 2 次 → 主動修正規則，不等業萱說**
- **知識衝突 → 主動提問，不等業萱發現**
- **新模式驗證有效 → 主動標準化，不等業萱要求**
- **每週自我檢討 → 回顧本週工作、找出錯誤、提出修正方案**
- 檢討報告存入 `wiki/notes/每週檢討/YYYY-MM-DD.md`
- 自我進化不是「自動改規則」，而是「提議修正 → 等業萱確認 → 再寫入」
- 如果業萱沒有回覆，假設提議被接受，但要在 log.md 記錄

## Lion Score

每篇整理後的 note、case 或 synthesis 優先加入：

```yaml
lion_score:
  變現價值: 1-5
  可複製性: 1-5
  長期價值: 1-5
  顧問可用性: 1-5
  內容延展性: 1-5
```

評分原則：能否用於顧問、課程、提案、產品、自媒體轉單；能否跨品牌複用；是否不受短期工具影響；能否變成診斷、框架、提問或 SOP；能否延伸成文章、短影音、簡報、直播或課程單元。

## 資訊來源與剪藏

允許來源：RSS、GitHub、Reddit、Twitter/X、網頁、YouTube、Telegram、Obsidian Clipper、Xiaohongshu Importer、Horizon AI 新聞雷達或同類工具。

剪藏原則：原文與附件進 `raw/` 或 `assets/`，摘要與判斷進 `wiki/notes/`，跨來源洞察進 `wiki/synthesis/`。


## 品牌案例規則

遇到品牌案例 PPT/PDF、官網、新聞或社群資料，不可只摘要原檔，必須先補背景再歸檔：保留原始來源；整理原資料觀點；補充最新公開資料與年份；建立或更新 `wiki/entities/`、`wiki/notes/`、必要的 `wiki/synthesis/`；最後更新 `index.md`、`hot.md`、`log.md`。除非老闆明確要求，品牌原檔不複製進 `assets/`，只保留原始路徑或來源連結。

## Skill 沉澱規則

當同類工作出現 3 次以上：

1. 在 `hot.md` 記錄 skill candidate。
2. 說明重複場景、觸發條件、預期輸入、預期輸出。
3. 等老闆確認後，新增或更新 `skills/`。
4. 新 skill 必須回寫 `index.md` 與 `log.md`。

## 任務結束自我檢查

- 是否新增或更新 wiki？
- 是否要更新 `index.md`？
- 是否要更新 `hot.md`？
- 是否 append `log.md`？
- 是否產生可重複 workflow？
- 是否有 skill candidate？
- 是否有 output 要歸檔？
- 是否有 asset 要連回 output？
- 是否有孤島、矛盾、過期內容？

## Hermes 個人知識工廠規則

Hermes 是本知識庫的前門，但不是正式知識庫本體。

日常路徑：

```text
Telegram / Hermes Inbox -> Hermes 收件 -> inbox/raw -> AI 閱讀員 -> inbox/processed -> wiki/notes 或 wiki/concepts/synthesis -> outputs 回流
```

角色分工：

- Telegram / Hermes：老闆隨手丟資料的入口。
- Hermes：收件、去重、抓正文、YouTube transcript、OCR、預摘要與狀態回報。
- Discord：顯示層，只看系統處理到哪，不當正式資料庫。
- Obsidian / markdown：正式知識庫，老闆搜尋、判斷、沉澱知識的地方。
- GitHub：備份與跨 AI 接手。

Inbox 規則：

- `inbox/raw/`：Hermes 收到但還沒整理的東西，全部不分類。
- `inbox/processed/`：AI 閱讀員整理後的「老闆理解版」。
- Inbox 不是知識庫，不要直接拿 Inbox 當長期判斷依據。

Hermes 分流規則：

- 問問題：Assistant Mode。
- 丟網址 / YT / 圖片 / 截圖：Inbox Mode。
- `/save`：強制存入知識庫。
- `/ask`：強制助理回答。
- `/digest`：查今日整理結果。
- `/find 關鍵字`：搜尋 Obsidian 知識庫。
- `/draft 主題`：從知識庫產內容草稿。

Discord 顯示層頻道：

- `#inbox-log`：今天 Hermes 收到什麼。
- `#daily-digest`：晚上 AI 閱讀員整理結果。
- `#needs-review`：讀不到、抓不到、需要補資料。
- `#knowledge-updates`：今天新增到 Obsidian 的 note / concept / synthesis。
- `#weekly-output`：每週產出的 Threads、FB、IG 輪播草稿。
- `#hermes-errors`：系統錯誤、API 失敗、排程失敗。

搜尋順序：

```text
index.md -> hot.md -> wiki/synthesis -> wiki/concepts -> wiki/notes -> inbox/processed
```

不要先搜 `raw/`，因為 `raw/` 是原始資料，不是老闆理解後的知識。

知識提升規則：

```text
inbox/raw -> inbox/processed -> wiki/notes -> wiki/concepts 或 wiki/synthesis -> skills 或 outputs
```

- 單篇有價值：進 `wiki/notes/`。
- 多篇都在講同一概念：整理進 `wiki/concepts/`。
- 多來源形成新判斷：整理進 `wiki/synthesis/`。
- 同類工作出現 3 次以上：提名 `skills/`。
- 能對外發文或簡報：進 `outputs/`，並回流 wiki。
