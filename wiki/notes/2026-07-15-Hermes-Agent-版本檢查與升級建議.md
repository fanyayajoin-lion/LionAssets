---
title: "Hermes Agent 版本檢查與升級建議"
created: 2026-07-15
updated: 2026-07-15
type: note
tags: [Hermes, 系統維護, 版本管理, 基礎設施]
sources: ["蝦趴獅 cron"]
lion_score:
  變現價值: 4
  可複製性: 3
  長期價值: 4
  顧問可用性: 3
  內容延展性: 3
---

# Hermes Agent 版本檢查與升級建議

**檢查日期：** 2026-07-15

## 版本現況

| 項目 | 數值 |
|------|------|
| **當前版本** | `v0.17.0`（2026.6.19，The Reach Release） |
| **最新版本** | `v0.18.2`（2026.7.7.2） |
| **版本差距** | 跨 2 個主版本（0.17→0.18），含 v0.18.0 + v0.18.1 + v0.18.2 |
| **更新狀態** | 系統提示：1 commit behind |

## 主要變更項目

### v0.18.0（The Judgment Release）— ~1,720 commits

1. **Mixture-of-Agents (MoA)** — 可選模型預設值，渲染每個參考模型的推理區塊 + 串流聚合器回答
2. **Self-Verification & `/goal`** — 完成合約以證據/測試而非模型自信判斷「完成」
3. **`/learn` & `/journey`** — 從工作流提煉可重用 skills；檢視 accumulated memories/skills
4. **Background Fan-Out** — `delegate_task` 可並行執行多個 subagents
5. **Desktop Coding Projects** — `project → repo → lane` 模型
6. **Gateway Scale-to-Zero** — 閒置時自動休眠
7. **Cheaper Self-Improvement** — post-turn review 路由到輔助模型
8. **Google Vertex AI** — 一階 Gemini provider，自動 OAuth2 token minting
9. **安全強化** — Credential-exfil hardening

### v0.18.1 / v0.18.2 — 基礎設施補丁

- Windows installer/updater self-healing
- Dashboard & gateway fixes
- WhatsApp dashboard pairing
- MCP/provider stability work
- 關鍵修復：解除 WhatsApp Baileys 未綁定依賴

## Breaking Changes 風險

1. **Gateway Scale-to-Zero** — 閘道器行為改變，可能影響長期運行的部署架構與 cron/jobs
2. **Dependency 大更新** — uv pip dry-run 顯示 47 個 packages 會更新/替換
   - `fastapi 0.139.0`、`pydantic 2.13.4`、`openai 2.24.0`
   - `cryptography 46.0.7`、`anyio 4.14.2`、`rich 14.3.3`

## 建議行動

**評估：🟡 可等待，建議先測試後更新**

- 短期：保持 v0.17.0 不變
- 中期（1-2 週內）：在測試環境執行 `uv pip install --upgrade hermes-agent` 驗證無誤後再更新
- 更新後確認：cron jobs、gateway 連線、WhatsApp/Telegram 通道是否正常
