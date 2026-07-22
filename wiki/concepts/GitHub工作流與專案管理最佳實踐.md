---
title: "GitHub 工作流與專案管理最佳實踐"
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [[標籤/GitHub]]
sources: [hermes-agent-skill-review, web-research-2026-07-22]
lion_score:
  變現價值: 4
  可複製性: 5
  長期價值: 5
  顧問可用性: 4
  內容延展性: 4
---

# GitHub 工作流與專案管理最佳實踐

## 結論

GitHub 對專業開發者不是「雲端硬碟」，而是**「專案操作系統」**。核心 5 件事：結構標準化、分支策略清晰、自動化取代手動、文件即程式碼、安全控管。

## 一、GitHub 功能地圖

| 功能 | 用途 | 大神怎麼用 |
|------|------|-----------|
| Repositories | 專案倉庫 | 一專案一 repo，命名統一 |
| Issues | 任務/問題追蹤 | 當看板 + 工單系統 |
| Projects | 專案管理 | 拖曳式看 milestone、排期 |
| Actions | 自動化工作流 | CI/CD、自動測試、自動發版 |
| Wiki | 官方文件 | 架構圖、API 文件、SOP |
| Secrets | 金鑰管理 | API Key 永不外洩到程式碼 |

## 二、大神管理 5 大黃金法則

### 法則 1：結構標準化
根目錄固定放 README.md、.gitignore、LICENSE、CHANGELOG.md、CONTRIBUTING.md、docs/、src/、tests/、scripts/。

### 法則 2：分支策略
小團隊推薦 **GitHub Flow**：只有 main + feature/*。分支命名：feat/fix/refactor/docs/ci/chore/perf。

### 法則 3：自動化取代手動
必開工具：Dependabot（依賴漏洞）、GitHub Actions（CI/CD）、Projects（看板）、Pages（靜態網站）。

### 法則 4：文件即程式碼
README 必須包含：What / Why / How to start / Architecture / Deployment / Troubleshooting。

### 法則 5：安全與權限控管
金鑰不外洩（GitHub Secrets）、Private Repo 保護商業邏輯、Branch Protection 禁止直接 push main、Audit Log 留痕。

## 三、實戰速查

- Commit 規範：Conventional Commits（feat/fix/refactor/docs/test/ci/chore/perf）
- PR Review 檢查：正確性、安全性、程式品質、測試、效能、文件
- 倉庫命名：[領域]-[專案名]，如 lionbot-hermes、lionassets

## 四、對群獅的應用

1. **LionAssets 知識庫**：已採用 GitHub Flow（main + feature/*），建議補上 Dependabot 與 CHANGELOG.md
2. **顧問服務**：可作為 AI 課或顧問方案中的「專案管理」單元
3. **客戶交付**：所有 client repo 統一標準結構，降低交接成本

## 雙向連結

- [[wiki/notes/小而美持續盈利的經營法則]] — 一人公司也需基本專案管理
- [[wiki/concepts/AI一人公司與蒸餾人物Skill]] — AI 工具鏈中 GitHub 是核心協作平台
- [[wiki/BOSS/AI 工具鏈與基礎設施]] — Hermes 知識庫部署在 GitHub
