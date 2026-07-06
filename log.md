# Log







## 2026-06-05







- 建立群獅靈感知識庫初始架構。



- 將舊 LionAssets 內容備份到 `archive/lionassets-legacy-20260605/`。



- 建立核心規則、workflow、skill 與品牌案例模板。















## 2026-06-05 品牌案例批次整理







- 從三個來源資料夾讀取 107 個檔案，未複製原始檔。



- 建立 `wiki/cases/品牌案例資料庫.md` 與 `wiki/cases/database/品牌案例資料庫.csv`。



- 為每個來源檔案建立 `wiki/cases/案例庫/` 案例卡，內含原檔抽取摘要與原始路徑。



- 建立 `wiki/synthesis/品牌案例庫分類總覽.md`。



- 本輪已完成資料庫化與原檔摘要；最新資料補充需逐案連網查證。







## 2026-06-05 品牌案例雙向連結修復







- 替 107 張 `wiki/cases/案例庫/` 案例卡補上知識圖譜連結。



- 建立 `wiki/cases/分類/` 產業索引頁。



- 建立 `wiki/cases/來源/` 來源索引頁。



- 建立 `wiki/cases/品牌案例補全隊列.md`。



- 更新 `wiki/cases/品牌案例資料庫.md`、`wiki/synthesis/品牌案例庫分類總覽.md`、`index.md`、`hot.md`。







## 2026-06-05 品牌案例補全狀態稽核







- 將 107 張案例卡檔名從 `case-id` 改成 `產業別-品牌名`；重複品牌用 `-2` 等序號避免撞名。



- 確認目前 107 件皆為 `待最新資料補充`。



- 已補全最新品牌資料數量：0。



- 建立 `wiki/cases/品牌案例補全狀態稽核.md`，避免把原檔摘要誤認為品牌補全。







## 2026-06-05 回流複購總結







- 依現有品牌案例摘要，建立 `wiki/concepts/回流.md`。



- 建立 `wiki/synthesis/回流複購案例總結.md`，用可用總結取代新增複雜分類。



- 本頁尚未補各品牌最新公開資料，後續需依優先品牌逐案查證。







## 2026-06-05 商業框架總結補齊







- 依照品牌案例資料庫，補齊 12 個 business_framework 的概念頁與案例總結頁。



- 新增 [[wiki/synthesis/商業模式框架總覽]]，作為顧問診斷與自媒體選題入口。



- 原則：不新增複雜分類，讓同一品牌可同時連到多個底層框架。



- 狀態：基於既有 PPT 摘要整理，可直接使用；最新品牌資料仍需逐案補全。

## 2026-06-05 案例庫命名修正

- 將 `wiki/cases/待補全/` 改為 `wiki/cases/案例庫/`，避免正式案例看起來像半成品。
- 將 20 個 `待分類-品牌名` 改為 `產業別-品牌名`。
- 重建品牌案例資料庫、產業索引、來源索引與補全隊列。
- 保留 `research_status` 管理最新資料查證，不再用資料夾名稱表示補全狀態。

## 2026-06-11 群獅靈感知識庫 v1 建置

- 建立 / 補齊必要資料夾：`raw/`、`wiki/`、`wiki/concepts/`、`wiki/entities/`、`wiki/notes/`、`wiki/synthesis/`、`workflows/`、`skills/`、`outputs/`、`assets/`、`archive/`。
- 覆蓋推送前，已將 GitHub 遠端 `LionAssets/main` 備份到 `archive/lionassets-remote-backup-20260611/`。
- 更新 `AGENTS.md`、`CLAUDE.md`、`README.md`，補上通用 LLM 規則、raw 不可改、outputs 必回流、Skill 候選、API Key 不落檔、任務結束自檢。
- 更新 workflows：資訊搜集、隨時剪藏、每日蒸餾、每週復盤、每月整理、output 回流、API 與工具需求。
- 更新 skills：選題價值判斷、業萱文風、去 AI 味、傳產案例拆解、文章配圖、文檔轉 PPT、影片摘要、品牌案例拆解、商業模式延伸。
- 更新 `index.md` 與 `hot.md`，讓 AI 查詢、熱點、候選 Skill、備份狀態有清楚入口。
- 下一步：設定手機 Telegram 剪藏入口、新聞雷達資料源、每日蒸餾自動化。

## 2026-06-11 Hermes 個人知識工廠路徑與顯示層落地

- 新增 Hermes Inbox 路徑：`inbox/raw/`、`inbox/processed/`、`inbox/needs-review/`。
- 新增內容輸出路徑：`outputs/threads/`、`outputs/facebook/`、`outputs/ig-carousel/`。
- 更新 `AGENTS.md`、`CLAUDE.md`、`README.md`、`index.md`、`hot.md`，明確寫入 Telegram / Hermes 是入口、Discord 是顯示層、Obsidian 是正式知識庫、GitHub 是備份與跨 AI 接手。
- 新增 workflows：`Hermes收件.md`、`AI閱讀員.md`、`Discord顯示層.md`、`知識入庫.md`、`每週內容工廠.md`、`知識搜尋.md`。
- 搜尋順序固定為：`index.md -> hot.md -> wiki/synthesis -> wiki/concepts -> wiki/notes -> inbox/processed`，不先搜 `raw/`。
- 知識提升邏輯固定為：`inbox/raw -> inbox/processed -> wiki/notes -> wiki/concepts 或 wiki/synthesis -> skills 或 outputs`。
- 下一步：改造 Zeabur 上既有 Hermes，先讓 Telegram / Hermes Inbox 能穩定寫入 `inbox/raw/`，並同步顯示到 Discord `#inbox-log`。
- `wiki/synthesis/AI數位團隊建置方案.md` — 310行，四階段操作流程 + 4堂課程大綱 + 定價模型
## 2026-06-21
- 重構知識庫結構：清理 00_Inbox/10_Wiki/20/30/40 舊目錄
- 新增 workflows/碎片接收.md + workflows/知識萃取.md
- 新增 wiki/inspiration/ 靈感庫
- 更新 AGENTS.md 加入碎片接收規則
- 更新 index.md 反映新結構
- 更新 obsidian-vault-setup skill 加入 AI 行為規則
- Git commit + push 完成
- 2026-06-21: 存入 OpenClaw + Hermes 商業搭配方案到 wiki/notes/
2026-06-23 04:39:16 | 新增 skills/Claude Code實用提示詞.md — 5個Claude Code協作提示詞：大白話解釋、需求訪談、網頁計畫、技能固化、對話記憶
2026-06-29 14:30 | 新增 wiki/notes/業老闆個人檔案.md — 完整個人檔案（決策模式 × 創業歷程 × 人類圖 × 商業方向 × 內容偏好 × 系統使用），人類圖獨立為子頁面
2026-06-29 14:30 | 知識庫中等簡化完成：砍掉 inbox/needs-review/、wiki/cases/分類/、wiki/cases/來源/、outputs/ 三個空子目錄、archive 重複備份；hot.md 表格改 bullet list；更新 AGENTS.md + README.md + index.md
2026-06-29 14:30 | 建立碎片自動入庫 cron job（f1b7ac5a614c），每 2 小時自動檢查 inbox/raw/ → 預摘要 → 存入 wiki → git push
2026-06-29 14:35 | Fragment check: inbox/raw/ has 2 files. AI數位團隊建置方案 already exists in wiki/synthesis/ (duplicate, skipped). _template-碎片.md is a template, not meaningful content, only copied to processed/.
2026-07-01 | 新增 wiki/projects/tarot-v5.md — 塔羅靈數第 5 版專案記錄（老婆業務：21K IG 追蹤、7 年塔羅、5000+ 客戶，專攻感情復合），待評估 Skill 化範圍
2026-06-29 15:00 | Fragment check: inbox/raw/ has 1 new file. AI數位團隊建置×課程架構整合方案.md — duplicate of wiki/synthesis/AI數位團隊建置方案.md (already processed), moved to processed/. No new wiki content added.
2026-07-03 | 建立管理獅行動管理入口：新增 workflows/管理獅.md，定義 Telegram 私訊路由、來源追蹤、圖片／網站收件、Wiki 更新、Git 提交與刪除審批規則。
2026-07-05 | 碎片接收：處理 inbox/raw/20260705-175932-fable5os.md — Fable 5 AI 個人作業系統五步驟建構，Lion Score 平均 4.2（顧問可用性 5），自動存入 wiki/concepts/AI個人作業系統架構.md；更新 3 個既有頁面的關聯；建立 inbox/processed/20260705-AI個人作業系統架構.md；更新 index.md、hot.md、log.md。
2026-07-06 | 新增 wiki/concepts/hermes-agent-overview.md — Hermes Agent 深度解析：架構、學習閉環、功能模組、安全模型、與 OpenClaw 比較；更新 index.md。
2026-07-06 | 碎片接收：處理 inbox/raw/20260706-160000-AI一人公司實測.md — AI 一人公司實測（Antigravity 2.0 蒸餾人物 Skill），Lion Score 平均 4.4（可複製性 5），自動存入 wiki/concepts/AI一人公司與蒸餾人物Skill.md；建立 inbox/processed/；更新 index.md、log.md。
2026-07-06 | 修正每日知識整理 cron job：no_agent 從 true 改為 false，解決 120 秒超時問題。
2026-07-07 | 碎片處理（小獅）：處理 7 個 inbox/raw/ 檔案。新增 wiki/concepts/AI工具分層使用法.md（GPT vs Codex 分工 + 強弱模型團隊管理框架）；新增 wiki/entities/電腦王阿達-KOCPC.md（4 條用戶路徑 + 自動化工具鏈 + 變現分析）；更新 wiki/concepts/引流.md（新增自動化引流工具鏈）；更新 wiki/concepts/AI一人公司與蒸餾人物Skill.md（新增 AI 蒸餾 = 團隊管理洞察）。
2026-07-07 | 碎片處理（管理獅）：① GPT vs Codex 使用時機 → wiki/notes/GPT與Codex使用時機對比.md；② 蒸餾實驗心得 → wiki/concepts/AI蒸餾與分層使用法.md（提出「AI蒸餾=團隊管理」洞察）；③ 電腦王阿達兩篇合併 → wiki/entities/電腦王阿達.md + wiki/synthesis/阿達引流自動化案例.md；④ 已建立標籤體系：wiki/標籤/ 目錄 + wiki/tags-index.md，所有 wiki 頁面 tags 改為 [[標籤/xxx]] 格式。inbox/raw/ 清空。
