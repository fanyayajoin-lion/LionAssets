---
title: Hermes Agent 深度解析
created: 2026-07-06
updated: 2026-07-06
type: concept
tags: [hermes, agent, nous-research, ai-framework, open-source, self-improving]
sources: [inbox/raw/20260706-hermes-agent-overview.md]
---

# Hermes Agent 深度解析

## 什麼是 Hermes Agent

Hermes Agent 是由 **Nous Research** 開發的開源、自改進（self-improving）AI Agent 框架，2026 年 3 月 12 日正式發布（v0.2.0），採用 MIT 授權。

它的核心理念是：**AI Agent 的價值不在於單次推理有多聰明，而在於隨著時間累積的記憶、技能與對使用者的了解會越來越深。**

與傳統聊天機器人或 IDE 助手不同，Hermes Agent 具備：
- 自主學習迴圈（learning loop）：完成複雜任務後自動生成可重複使用的技能（skills）
- 持久記憶（persistent memory）：跨會話記住用戶偏好、專案資訊與經驗教訓
- 多平台閘道器（gateway）：單一閘道器連接 15+ 通訊平台
- 子代理委派（delegation）：平行 spawns 獨立的子代理處理多個工作流

### 市場表現（截至 2026 年 7 月）
- GitHub 星數超過 210,000（從零到 100K+ 僅花約 10 週）
- 每日處理超過 2,240 億 tokens（OpenRouter 數據）
- 全球生產力、編碼、個人助手類別排名第一
- 社群技能註冊中心有 647 個技能（79 內建 + 521 社群貢獻）

## 核心架構

### 三層設計
1. **介面層**：CLI/TUI、訊息平台適配器、編輯器協定（ACP）
2. **核心 Agent 層**：協調、提示詞組裝、工具派遣、記憶、技能管理
3. **執行層**：終端後端（Local、Docker、SSH、Modal 等）

### 學習閉環
```
觀察 → 執行 → 反思 → 結晶 → 再利用
```
1. **觀察**：評估任務複雜度與所需工具
2. **執行**：呼叫 LLM 進行推理與工具使用
3. **反思**：任務完成後自動進入反思階段（5+ 工具呼叫觸發）
4. **結晶**：將可重複的模式寫入 SKILL.md 文件
5. **再利用**：未來任務自動載入相關技能

### 記憶體系統
Hermes 不使用向量資料庫，而是採用兩個小型文字檔案：

| 檔案 | 用途 | 限制 |
|------|------|------|
| `MEMORY.md` | 環境事實、工具特性、經驗教訓 | ~2,200 字元（約 800 tokens） |
| `USER.md` | 用戶偏好、溝通風格、專案背景 | ~1,375 字元（約 500 tokens） |

**重要限制**：會話中修改的記憶不會即時反映在系統提示詞中，必須等到下一次會話才會載入。這稱為「記憶延遲」。

## 主要功能模組

### 1. 閘道器（Gateway）
單一進程管理所有通訊平台的連線：
- Telegram、Discord、Slack、WhatsApp、Signal、Matrix、Email、SMS、DingTalk、飛書、企業微信、QQ Bot、元寶、BlueBubbles、Home Assistant、Microsoft Teams、Google Chat 等 15+ 平台
- 訊息路由、授權檢查、平台特定適配器

### 2. 技能系統（Skills）
- 自動生成：完成複雜任務後反思並寫入 SKILL.md
- 漸進式載入：Level 1（名稱/描述，~20 tokens）→ Level 2（詳細規格，~200 tokens）→ Level 3（完整執行步驟，~1,000+ tokens）
- 自我改進：透過 diff 修補既有技能而非完全重寫
- 遵循 agentskills.io 開放標準，技能可移植、可分享

### 3. 排程器（Cron）
- 自然語言排程：用白話文設定定時任務
- 獨立會話執行：每次 cron 運行在乾淨的上下文中
- 多平台送達：結果可發送到 Telegram、Discord 等
- 兩種模式：
  - **LLM 驅動**（no_agent: false）：派 AI 代理判讀腳本輸出
  - **腳本直跑**（no_agent: true）：只執行腳本，輸出直接送達

### 4. 子代理委派（Delegation）
- 平行 spawns 多個獨立子代理
- 每個子代理有自己的對話、終端會話與工具集
- 支援叢集管理模式（Kanban board）
- 心跳檢測、殭屍進程偵測、自動重試

### 5. 模型提供者（Providers）
支援 20+ 個模型提供者，可即時切換：
- Nous Portal（OAuth，內建每月額度）
- OpenRouter（200+ 模型）
- OpenAI、Anthropic、Google Gemini
- 本地模型（Ollama、vLLM、SGLang）
- 任何 OpenAI 相容端點

**限制**：模型上下文窗口至少需要 64K tokens。

### 6. 終端後端（Terminal Backends）
| 後端 | 用途 | 安全等級 |
|------|------|----------|
| `local` | 開發環境 | 低（完整主機存取） |
| `docker` | 安全隔離 | 高（唯讀檔案系統） |
| `ssh` | 遠端伺服器 | 高（無法接觸主機程式碼） |
| `daytona` | 雲端沙盒 | 中（持久化，閒置休眠） |
| `modal` | Serverless | 高（自動縮放，按用量付費） |
| `singularity` | HPC 叢集 | 高（無 root） |

### 7. 瀏覽器自動化
- 使用 Camofox 反探測瀏覽器（針對 bot 檢測優化）
- 支援截圖分析、動態內容渲染、表格提取

## 安全性

Hermes Agent 採用七層安全模型：

1. **命令核准**：危險命令需人工確認（可設為 smart 模式由輔助 LLM 自動判斷）
2. **硬線封鎖列表**：`rm -rf /`、fork bomb、格式化磁碟等命令永遠禁止
3. **授權檢查**：僅限 allowlist 中的使用者可下指令
4. **容器隔離**：Docker/Singularity 等後端限制存取範圍
5. **機密遮蔽**：工具輸出自動偵測並遮蔽 API Key、token 等敏感資訊
6. **PII 遮蔽**：可選啟用，雜湊使用者 ID、 stripping 電話號碼
7. **Shell Hook 白名單**：外掛 hook 需明確授權才執行

## 與 OpenClaw 的比較

| 維度 | Hermes Agent | OpenClaw |
|------|-------------|----------|
| **核心理念** | 自改進、學習型 Agent | 廣度整合、即插即用 |
| **語言** | Python 82% + TypeScript 14% | Node.js |
| **安全模型** | 設計時內建七層安全 | 事後修復（曾有多個 CVE） |
| **已知 CVE** | 無重大公開漏洞 | 多個（CVSS 7.5-9.1） |
| **供應鏈攻擊** | 無（無市場/插件商店） | ClawHub 遭 1,184 個惡意包攻擊 |
| **記憶體** | 小型文字檔案 + FTS5 搜尋 | 向量資料庫 + 插件 |
| **成本** | $15-50/月（模型費用） | $30-80/月 |
| **授權** | MIT（純開源，無商業 SaaS） | MIT + 商業 SaaS 選項 |
| **成熟度** | 較新（2026 年 3 月發布） | 較早（2025 年底開始） |

**結論**：Hermes 適合需要長期自我改進、重視隱私安全的場景；OpenClaw 適合需要快速大量工具整合的場景。

## 適用場景

1. **個人數位助理**：跨平台統一 AI 入口，記住你的偏好與工作習慣
2. **知識庫管理**：自動整理、分類、索引文件與網頁內容
3. **自動化工作流程**：排程報告、備份、監控、警報
4. **多代理協作**：平行處理複雜專案，每個子代理負責一部分
5. **開發工作流**：程式碼審查、除錯、文件生成、CI/CD 管理
6. **研究與情報蒐集**：持續監控部落格、RSS、社群，自動摘要重點
7. **家庭自動化**：Home Assistant 整合，語音控制智慧家電

## 最佳實踐

1. **定期更新**：Hermes 更新頻繁（v0.13.0 單週就有 864 次提交），建議定期 `hermes update`
2. **善用技能系統**：複雜任務完成後，要求 Agent 將流程存為 Skill
3. **使用 Docker 後端**：生產環境建議用 Docker 隔離，避免 Agent 誤操作主機
4. **監控記憶檔案**：MEMORY.md 和 USER.md 有字數限制，定期清理過時內容
5. **設定 Cron 警報**：用排程器監控系統健康狀態，有問題主動通知
6. **避免無效對話**：Hermes 會過濾寒暄、純問題等無意義對話，節省 token

## 已知限制與注意事項

1. **記憶延遲**：會話中修改的記憶不會即時生效，需等新會話
2. **64K 上下文限制**：小於 64K tokens 的模型無法使用
3. **Windows 相容性**：部分 Unix 特有功能（檔案權限、symlink）在 Windows 上行為不同
4. **技能衝突**：多個技能可能同時載入，需注意優先級
5. **Cron 無上下文**：cron job 每次在乾淨會話中執行，不包含之前的對話內容
6. **網路依賴**：web_search、browser 等工具需要網路連線

## 參考來源

- 官方文件：https://hermes-agent.nousresearch.com/docs/
- GitHub 原始碼：https://github.com/NousResearch/hermes-agent
- HackerNoon 比較分析：https://hackernoon.com/hermes-agent-vs-openclaw-which-ai-agent-framework-wins-in-2026
- Stackademic 深度評測：https://blog.stackademic.com/forget-chatbots-hermes-agent-is-an-ai-that-actually-learns-from-you-d8d517be7b88
- Utilo 完整回顧：https://utilo.io/en/home/blog/hermes-agent-review-2026
- innfactory 技術比較：https://innfactory.ai/en/blog/openclaw-vs-hermes-agent-comparison
- Medium 使用心得：https://medium.com/@creativeaininja/hermes-agent-the-open-source-ai-agent-that-actually-remembers-what-it-learned-yesterday-278441cd1870

## 關聯知識庫頁面

- [[wiki/synthesis/OpenClaw-vs-HermesAgent-競品分析]] — OpenClaw vs Hermes 市場對比（2026-07-22 新增）
- [[wiki/notes/OmniRoute開源免費AIGateway研究]] — AI Gateway 工具研究，與 Hermes 解耦理念互補（2026-07-22 新增）
