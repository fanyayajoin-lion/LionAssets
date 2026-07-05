---
title: AI 個人作業系統架構
created: 2026-07-05
updated: 2026-07-05
type: concept
tags: [AI-OS, Skill-Architecture, 語音驅動, 本地端運行, 換皮部署]
sources: [inbox/raw/20260705-175932-fable5os.md]
---
# AI 個人作業系統架構

> 來源：Equality Blog, Jul 4 — Fable 5 五步驟建構法
> 處理日期：2026-07-05

## 概念定義

一套在本地電腦上建構「語音驅動的 AI 個人作業系統」的架構框架。目標是建立一個具備長期記憶、可為客戶或團隊客製化的專屬 AI 助手（類似 Jarvis），核心設計原則是不綁定特定 LLM、100% 本地端運行、完全可客製化與換皮部署。

## 五大步驟

### 1. 大腦（The Brain）— 技能架構
- 將工作流程拆為「分支」→ 細分為「技能」
- 每個任務對應一個資料夾，內含 SKILL.md
- SKILL.md 定義：Role、Inputs、Outputs、Tools
- 目的：避免 Context Window 浪費，按需載入

### 2. 記憶（The Memory）— Obsidian 知識庫
- 用純文本 Markdown 作為長期記憶
- 每篇筆記可連結成知識圖譜（Graph）
- AI 生成的報告自動存回 Obsidian
- 規定使用 [[雙向連結]] 標籤

### 3. 聲音（The Voice）— 100% 本地化語音驅動
- STT: faster-whisper 本地語音轉文字
- 路由: Regex 捕捉簡單指令，複雜問題丟給 LLM
- TTS: Kokoro / Edge-TTS / VITS 本地文字轉語音
- 喚醒詞機制（如 "Hey Jarvis"）

### 4. 介面（The Face）— 單一 HUD 儀表板
- 前端: HTML/CSS + Vue/React 或 Streamlit/Gradio
- API 橋樑: FastAPI / Flask
- 即時狀態: WebSocket 顯示語音進度
- 串接社群 API 自動更新 Metrics

### 5. 交付與部署（The Handoff）— 打包、發布、換皮
- Git 版本控制，.env.example 管理金鑰
- setup.sh / setup.bat 一鍵安裝
- 換皮邏輯: CSS 變數抽離到 config.json
- Fork 給不同客戶/團隊，改 JSON 即可換品牌視覺

## 核心優勢
- **不綁定特定 LLM 模型**：可替換底層推理引擎
- **100% 本地端運行**：保障隱私與低延遲
- **100% 可客製化**：可 Fork + Reskin，直接對應 S2B2C 模式

## 與群獅知識庫的關聯

這個架構與群獅現有的雙 Agent 設計高度吻合：
- 「大腦」對應 Hermes 的 skills/ 系統與 AGENTS.md 規則
- 「記憶」對應 Obsidian Vault + wiki/ 知識層
- 「交付與部署」對應群獅的「換皮給不同客戶」商業模式
- 「不綁定 LLM」對應 AGENTS.md 中「不綁 Codex、不綁 Claude Code」的原則

## Lion Score
- 變現價值: 4
- 可複製性: 4
- 長期價值: 4
- 顧問可用性: 5
- 內容延展性: 4

## 業老闆的判斷
[待補充 — 業萱可在此寫下對這個架構的看法、與現有用法的比較、是否值得進一步探索]

## 關聯頁面

- [[wiki/concepts/跨產業AI變現藍圖]] — 雙 Agent 架構與一人公司 IT 兵工廠
- [[wiki/notes/OpenClaw與Hermes商業搭配方案]] — OpenClaw 前台 + Hermes 後台的商業搭配
- [[wiki/inspiration/2026-06-23-靈感素材-AI團隊]] — AI 讓公司脫離老闆也能跑的靈感素材
- [[workflows/管理獅]] — 管理獅的收件與 wiki 更新流程
- [[index.md]] — 群獅靈感知識庫索引
