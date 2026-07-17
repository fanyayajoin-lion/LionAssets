# Log



## 2026-06-05





- 建立群獅靈感知識庫初始架構。




- 將舊 LionAssets 內容備份到 `archive/lionassets-legacy-20260605/`.




- 建立核心規則、workflow、skill 與品牌案例模板。




## 2026-06-05 品牌案例批次整理




- 從三個來源資料夾讀取 107 個檔案，未複製原始檔。




- 建立 `wiki/cases/品牌案例資料庫.md` 與 `wiki/cases/database/品牌案例資料庫.csv`.




- 為每個來源檔案建立 `wiki/cases/案例庫/` 案例卡，內含原檔抽取摘要與原始路徑。




- 建立 `wiki/synthesis/品牌案例庫分類總覽.md`.




- 本輪已完成資料庫化與原檔摘要；最新資料補充需逐案連網查證。




## 2026-06-05 品牌案例雙向連結修復




- 替 107 張 `wiki/cases/案例庫/` 案例卡補上知識圖譜連結。




- 建立 `wiki/cases/分類/` 產業索引頁。




- 建立 `wiki/cases/來源/` 來源索引頁。




- 建立 `wiki/cases/品牌案例補全隊列.md`.




- 更新 `wiki/cases/品牌案例資料庫.md`、`wiki/synthesis/品牌案例庫分類總覽.md`、`index.md`、`hot.md`.




## 2026-06-05 品牌案例補全狀態稽核




- 將 107 張案例卡檔名從 `case-id` 改成 `產業別-品牌名`；重複品牌用 `-2` 等序號避免撞名。




- 確認目前 107 件皆為 `待最新資料補充`.




- 已補全最新品牌資料數量：0。




- 建立 `wiki/cases/品牌案例補全狀態稽核.md`，避免把原檔摘要誤認為品牌補全。




## 2026-06-05 回流複購總結




- 依現有品牌案例摘要，建立 `wiki/concepts/回流.md`.




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
2026-07-06 | 碎片接收：處理 inbox/raw/20260706-160000-AI一人公司揭露.md — AI 一人公司實測（Antigravity 2.0 蒸餾人物 Skill），Lion Score 平均 4.4（可複製性 5），自動存入 wiki/concepts/AI一人公司與蒸餾人物Skill.md；建立 inbox/processed/；更新 index.md、log.md。
2026-07-07 | 碎片處理（小獅）：處理 7 個 inbox/raw/ 檔案。新增 wiki/concepts/AI工具分層使用法.md（GPT vs Codex 分工 + 強弱模型團隊管理框架）；新增 wiki/entities/電腦王阿達-KOCPC.md（4 條用戶路徑 + 自動化工具鏈 + 變現分析）；更新 wiki/concepts/引流.md（新增自動化引流工具鏈）；更新 wiki/concepts/AI一人公司與蒸餾人物Skill.md（新增 AI 蒸餾 = 團隊管理洞察）。
2026-07-07 | 碎片處理（管理獅）：① GPT vs Codex 使用時機 → wiki/notes/GPT與Codex使用時機對比.md；② 蒸餾實驗心得 → wiki/concepts/AI蒸餾與分層使用法.md（提出「AI蒸餾=團隊管理」洞察）；③ 電腦王阿達兩篇合併 → wiki/entities/電腦王阿達.md + wiki/synthesis/阿達引流自動化案例.md；④ 已建立標籤體系：wiki/標籤/ 目錄 + wiki/tags-index.md，所有 wiki 頁面 tags 改為 [[標籤/xxx]] 格式。inbox/raw/ 清空。
2026-07-07 | 碎片處理（小獅）：車輛定檢提醒 BV-931 → Lion Score 1/5（個人行政提醒，無知識庫價值），不存入 wiki，僅移至 inbox/processed/。提醒：車牌 BV-931 定檢迄日 115/07/17，已逾期約20天，建議通知業萱儘速辦理。
2026-07-07 | 碎片處理（小獅）：八字命理學習筆記 → Lion Score 平均 3.6（變現價值 4、長期價值 4、內容延展性 4），自動存入 wiki/notes/八字命理基礎學習筆記.md；更新 index.md；移至 inbox/processed/。
2026-07-08 | Fragment processing: dialog summary 2026-07-07, Lion Score 3.4, mostly operational decisions already in system config, no wiki update needed. Moved to inbox/processed/.
2026-07-08 | 碎片處理（管理獅）：① 數據作證規則 → wiki/notes/數據作證規則.md（AI 互動行為準則：假設性判斷必須查真實數據）；② 創業者 vs 企業主社群行為洞察 → wiki/synthesis/創業者vs企業主社群行為洞察.md（創業者碎片時間全在手機上但不知如何使用，六階段模型是策略框架）。更新 index.md、log.md。
2026-07-09 | 碎片接收：處理 inbox/raw/20260709-001000-ClaudeCodeFable5成本優化.md — Claude Code Fable 5 成本優化策略（Advisor 模式 + Orchestrator 模式），Lion Score 平均 4.0（長期價值 5、顧問可用性 4），更新 wiki/tools/claude-code-shortcuts.md（新增第五章 Fable 5 成本優化策略 + 關聯知識 wikilinks）；更新 index.md、log.md。
2026-07-09 | 碎片接收：處理 inbox/raw/20260709-002000-MetaAds自動化架構.md — Meta Ads 投放自動化五步流程（MCP 串接 + GCS 圖床 + Creative 自動上架），Lion Score 平均 4.6（變現價值 5、長期價值 5、顧問可用性 5），建立 wiki/concepts/Meta Ads自動化架構.md + wiki/標籤/Meta.md；更新 index.md、log.md。
2026-07-09 | 碎片接收：處理 inbox/raw/20260709-蝦趴獅-Skill-升級-HAOS-學習報告.md — HAOS Skill 升級學習報告（6 個 Skill 標準化），Lion Score 平均 2.4（內部技術維護報告），不存入 wiki，僅存 inbox/processed/。
2026-07-09 | 碎片接收（cron）：處理 inbox/raw/ 4 個檔案。① Company of One 讀書摘要 → Lion Score 平均 3.4（長期價值 4、內容延展性 4），更新 wiki/concepts/AI一人公司與蒸餾人物Skill.md（新增《Company of One》補充洞察：一人企業四大特徵 + 三階段框架 + MVPr），建立 wiki/concepts/一人企業增長哲學.md 連結；② MetaAds 自動化架構 → 已於前述處理（Lion Score 平均 4.6），建立 wiki/concepts/Meta Ads自動化架構.md；③ Claude Code Fable 5 成本優化 → 已於前述處理（Lion Score 平均 4.0），更新 claude-code-shortcuts.md；④ 蝦趴獅 Skill 升級 HAOS 學習報告 → Lion Score 平均 2.4，不存入 wiki。全部移至 inbox/processed/。
2026-07-09 | Fragment processing (Shiao-Shi cron): 2 files handled. 1) Parking reminder -> Lion Score 1/5, not stored. 2) Junsen Jingyang owner questionnaire -> Lion Score 2.8, recommended owner needs diagnostic framework. inbox/raw/ cleared.
2026-07-09 | 碎片接收（圖片）：處理 inbox/raw/20260709-003000-Meta合作廣告洞察.md — Meta 合作廣告與素材策略（創作者素材競賽時代、CPA 降低 19%～37%、KOC 評估指標），建立 wiki/concepts/Meta合作廣告與素材策略.md；更新 index.md、log.md、標籤關聯。
2026-07-09 | Housekeeping: inbox/raw 剩餘的 20260709-003000-Meta合作廣告洞察.md 已移至 inbox/processed/（今日已由管理獅處理完畢，屬重複檔案清理）。commit f80fc79，push 成功。
2026-07-10 | 碎片接收：處理 inbox/raw/2026-07-10-業老闆星盤完整資料.md — 業老闆星盤完整資料（太陽天秤10宮群星 + 月亮處女9宮 + 上升射手），Lion Score 平均 4.2（長期價值 5、顧問可用性 5），存入 wiki/profiles/業老闆星盤資料.md；與人類圖交叉驗證表（5項全部一致）；更新 wiki/profiles/業老闆個人檔案.md（新增星盤連結 + 更新記錄）；更新 index.md；移至 inbox/processed/。
2026-07-10 | Fragment processing (Shiao-Shi cron): Checked 2 files in inbox/raw/. 1) 固定式重訓機菜單 -> Lion Score avg 3.2（長期價值4、內容延展性4），存入 wiki/notes/業老闆固定式重訓機菜單.md，與健康減脂計畫互補；2) 星盤完整資料 -> 已於同日早處理，跳過。全部移至 inbox/processed/，inbox/raw/ 清空。

2026-07-10 管理獅每日整理
- 檢查 inbox/raw/：2 個檔案（固定式重訓機菜單、星盤資料），遠端 cron 已處理
- 補齊雙向連結：健康減脂計畫 ↔ 固定式重訓機菜單
- 更新 index.md Note 區段、個人檔案更新記錄
- Git commit b8b733e + push 成功

2026-07-11 碎片接收（小獅 cron）：處理 4 個 inbox/raw/ 檔案。
① Bot後台系統架構設計 -> Lion Score 4.4（變現價值5），存入 wiki/concepts/Bot後台系統架構設計.md — 多Profile管理 + CRM + 客戶培育架構
② DOCX純Python解析方法 -> Lion Score 3.2（技術細節），存入 wiki/notes/DOCX純Python解析方法.md
③ Hermes-Agent-Cloud-雲端部署 -> Lion Score 4.0（長期價值4、內容延展性4），存入 wiki/concepts/Hermes-Agent-Cloud-雲端部署.md — 60秒一鍵部署路線四
④ WSL檔案搬移風險教訓 -> Lion Score 3.8（長期價值4），存入 wiki/notes/WSL檔案搬移風險教訓.md — 跨平台檔案操作風險意識
全部移至 inbox/processed/，更新 index.md，log.md。

## 2026-07-13
- [新增] `wiki/external-skills/speak-human-tw.md` — 說人話 skill 設計文檔（38 種 AI 痕跡檢測 + 六步改寫流程 + 繁體中文在地化）
- [新增] `wiki/external-skills/index.md` — 外部 Skill 彙整索引頁
- [更新] `index.md` — 新增外部 skill 索引入口與條目
- [來源] https://github.com/Raymondhou0917/speak-human-tw


## 2026-07-13
- [新增] `wiki/notes/小而美持續盈利的經營法則.md` — 薩希爾·拉文吉亞《Start Small, Stay Small》+ Paul Jarvis《一人公司》完整摘要（極簡主義創業六大步驟、MVP重新定義、100+自我定位問題）
- [更新] `index.md` — 新增 Note 與 Concept 條目
- [更新] `wiki/concepts/AI一人公司與蒸餾人物Skill.md` — 新增反向連結
- [來源] 微信讀書、TracyXC讀書筆記、YouTube摘要、Beancount.io

## 2026-07-12（管理獅）
|- [新增] `wiki/BOSS/AI 工具鏈與基礎設施.md` — AI 工具清單與基礎設施架構
|- [新增] `wiki/concepts/經典商業模式清單.md` — 12 種經典可複用商業模式框架
|- [新增] `wiki/concepts/Firebase-Cloudflare-Vercel-VPS比較.md` — 四者完整比較
|- [新增] `wiki/concepts/資料庫方案成本比較-Firebase-Supabase-VPS.md` — 成本分析與推薦方案
|- [新增] `wiki/synthesis/新創商業模式拆解系列.md` — 13 篇經典商業模式深度拆解

## 2026-07-12（小獅 cron 碎片處理）
|- [新增] `wiki/concepts/一人公司創業檢查清單.md` — 8 大項評估框架（變現5/可複製5/長期5/顧問5/內容4）
|- [新增] `wiki/synthesis/創業檢查清單實戰案例.md` — 香料大叔 45/100 vs 金飾 20/100 風險對比
|- [更新] `wiki/concepts/AI一人公司與蒸餾人物Skill.md`、`wiki/notes/小而美持續盈利的經營法則.md`、`hot.md`、`tags-index.md`

## 2026-07-13 每日萃取
|- [2026-07-13 20:00] 每日萃取 cron：今日無對話知識可萃取，三筆 cron 均為例行任務。

## 2026-07-13（小獅 cron 碎片處理）
|- [新增] `wiki/external-skills/speak-human-tw.md` — 說人話 skill 設計文檔
|- [新增] `wiki/external-skills/index.md` — 外部 Skill 彙整索引頁
|- 對話摘要 2026-07-13：cron 自動執行，無業老闆訊息。健康警訊、訪談完成率、管理獅 backlog 需追蹤。

## 2026-07-14

- [新增] `wiki/tools/Obsidian-全面使用指南與插件推薦.md` — Obsidian 全面使用方式：基本認識、核心內建功能、初級/中級/高級使用流程、知識管理方法論（PARA/Zettelkasten/MOC/Evergreen）、四梯隊插件推薦清單（共 35+ 插件）
- [更新] `index.md` — 新增 Tools 條目
- [來源] 老闆 Telegram 指令

## 2026-07-14（小獅 cron 碎片處理）
|- 處理 inbox/raw/2026-07-13-對話摘要.md → Lion Score 平均 2（系統日記，部分萃取至業老闆個人檔案行為模式觀察）
|- 檔案已移至 inbox/processed/，git commit + push 中

## 2026-07-15（小獅 cron 碎片處理）
|- [新增] `wiki/notes/2026-07-15-對話摘要-2026-07-14.md` — 7/14 對話摘要：停用 cron #6、訪談規則明確化、BlueMagpie-TTS 評估、設計人生模式深化、健康警訊提醒
|- [新增] `wiki/notes/2026-07-15-Hermes-Agent-版本檢查與升級建議.md` — Hermes v0.17.0 → v0.18.2 版本檢查報告，Gateway Scale-to-Zero 風險評估
|- 兩筆檔案已移至 inbox/processed/
|- BlueMagpie-TTS 為新實體，需建立 wiki/entities 頁面

## 2026-07-16（管理獅直接入庫）

- [新增] `wiki/concepts/超級個體深度閱讀書單.md` — 五大模塊 20 本深度閱讀書單：專注生產力、底層認知、商業財富、人性溝通、內心韌性 + 配套閱讀方法
- [更新] `index.md` — 新增 Concept 條目
- [來源] 老闆 Telegram 直接輸入

## 2026-07-16（管理獅直接入庫 · 二）

- [新增] `wiki/concepts/Codex自媒體十大Skill.md` — 從選題到發布、復盤的 10 個 Codex Skill 完整工作流 + 工作流映射圖
- [更新] `index.md` — 新增 Concept 條目
- [來源] 老闆 Telegram 直接輸入

## 2026-07-16（管理獅每日整理）

- [新增] `wiki/synthesis/台灣小型顧問案五人對標.md` — 台灣在地一人顧問案五人对標：雷蒙三十（定位敘事）、劉奕酉（產品階梯）、Harris先生（案源）、于為暢（訂閱制）、周振驊（客戶池），Lion Score 平均 4.8
- [更新] `wiki/concepts/經典商業模式清單.md` — 追加反向連結至對標報告
- [更新] `wiki/concepts/AI一人公司與蒸餾人物Skill.md` — 追加反向連結至對標報告
- [更新] `index.md` — 新增 Synthesis 條目
- [搬移] inbox/raw/ 5 筆檔案 → inbox/processed/（含 4 筆 cron 報告 + 1 筆對標研究原始檔）
- [來源] cron 投遞 + 管理獅直接入庫

## 2026-07-17（小獅 cron 碎片處理）

- [新增] `wiki/BOSS/業老闆紫微斗數命盤.md` — 紫微斗數命盤完整資料：太陰命宮、巨門身宮、己年生人四化、33-42歲乙丑大限重點、2026丙午年流年分析
- index.md 已更新個人檔案區
- 檔案已移至 inbox/processed/

## 2026-07-17（管理獅直接入庫）

- [新增] `wiki/concepts/Web-部署平台比較表.md` — Cloudflare Pages / Workers、GitHub Pages、Netlify、Vercel、Supabase、Zeabur 六平台比較：最適合場景、不適合場景、白話判斷與決策參考
- [更新] `index.md` — 新增 Concept 條目
- [來源] 老闆 Telegram 圖片截圖
