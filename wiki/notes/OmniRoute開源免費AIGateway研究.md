---
title: "OmniRoute 開源免費 AI 閘道工具研究"
created: 2026-07-22
updated: 2026-07-22
type: notes
tags: [[標籤/AI-Gateway]]
sources: [黑獅每日萃取, Telegram-2026-07-21]
lion_score:
  變現價值: 3
  可複製性: 3
  長期價值: 3
  顧問可用性: 3
  內容延展性: 3
---

# OmniRoute 開源免費 AI 閘道工具研究

## 快速摘要

**一個 endpoint 串接 250+ AI 供應商**的開源免費 AI 閘道。GitHub: `diegosouzapw/OmniRoute`

## 核心功能

### 供應商與成本
- **90+ 免費層級**供應商
- **11 個永久 $0 供應商**：Kiro、Qoder、LongCat、Pollinations、Qwen、Cloudflare、Groq、NVIDIA、Scaleway、Cerebras 等
- Token 壓縮可省 15-95%

### 路由策略（18 種）
優先權路由、輪詢路由、成本優化路由、自動智能路由、延遲最低路由、成功率最高路由、混合策略路由等。

### 相容性
支援 Claude Code、Codex、Cursor、OpenClaw 等 14+ CLI 工具，內建 MCP 伺服器（25 種工具），支援 A2A 協議。

## 對群獅的價值評估

### 直接應用
1. **省 API 成本**：多個 Agent（蝦趴獅、管理獅、彩綺）用不同供應商時，OmniRoute 可統一路由、自動選最便宜/最快的
2. **免費層級足夠日常使用**：Groq、Qwen、Cloudflare 都有免費額度
3. **Token 壓縮**：長對話場景可顯著降低成本

### 風險 / 待確認
- 需要實際部署測試，確認穩定性
- 250+ 供應商的真實可用性待驗證
- 與現有 Hermes Agent 的整合方式需研究
- 安全考量：API Key 集中管理，一旦 OmniRoute 出問題會影響所有供應商

## 行動建議

**優先級：中**。對我們有實際省錢價值，但不急。建議先在小規模場景（如儀表板 API 呼叫）試用。

## 雙向連結

- [[wiki/concepts/hermes-agent-overview]] — Hermes Agent 架構與模型解耦
- [[wiki/BOSS/AI 工具鏈與基礎設施]] — AI 工具清單與基礎設施
- [[wiki/synthesis/OpenClaw-vs-HermesAgent-競品分析]] — OpenClaw 也有類似 Gateway 定位
