# Hermes Agent 版本檢查報告

**檢查日期：** 2026-07-15  
**執行者：** 蝦趴獅（小獅）

---

## 📊 版本比對

| 項目 | 數值 |
|------|------|
| **當前版本** | `v0.17.0`（2026.6.19，The Reach Release） |
| **最新版本** | `v0.18.2`（2026.7.7.2） |
| **版本差距** | 跨 2 個主版本（0.17→0.18），含 v0.18.0 + v0.18.1 + v0.18.2 |
| **更新狀態** | 系統提示：1 commit behind |

---

## 🚀 主要變更項目

### 🔹 v0.18.0（2026.7.1）— The Judgment Release
**規模：** ~1,720 commits · 998 PRs · 949 issues closed · 370+ contributors

**核心新功能：**
1. **Mixture-of-Agents (MoA)** — 可選模型預設值，渲染每個參考模型的推理區塊 + 串流聚合器回答
2. **Self-Verification & `/goal`** — 完成合約以證據/測試而非模型自信判斷「完成」，含 `pre_verify` hook
3. **`/learn` & `/journey`** — 從任何工作流提煉可重用的 skills；透過 CLI/TUI 時間軸或桌面徑向圖檢視/編輯/刪除 accumulated memories/skills
4. **Background Fan-Out** — `delegate_task` 可並行執行多個 subagents，完成後回傳整合結果
5. **Desktop Coding Projects** — `project → repo → lane` 模型，含 sidebar、coding rail、review pane、git worktree 管理
6. **Gateway Scale-to-Zero** — 閒置時自動休眠；drain coordination 防止重啟/遷移中斷對話
7. **Cheaper Self-Improvement** — 將 post-turn review 路由到輔助模型，降低主模型成本
8. **`/prompt`** — 開啟 `$EDITOR` 進行多行 markdown prompt 草稿
9. **Google Vertex AI** — 一階 Gemini provider，自動 OAuth2 token minting/refresh（無需靜態金鑰）
10. **安全強化** — Credential-exfil hardening、interrupt-protected compression sibling-fork bug fix

### 🔹 v0.18.1（2026.7.7）— Infrastructure Patch
**規模：** ~660 PRs since v0.18.0

- Windows installer/updater self-healing
- Dashboard & gateway fixes
- WhatsApp dashboard pairing
- MCP/provider stability work

### 🔹 v0.18.2（2026.7.7.2）— Same-day Patch
- **關鍵修復：** 解除 WhatsApp Baileys 未綁定依賴，改用發布版 `7.0.0-rc13`，確保 npm/Docker 建構可靠

---

## ⚠️ Breaking Changes 與注意事項

從 v0.17.0 → v0.18.x 的干預性變更：

1. **Gateway Scale-to-Zero** — 閘道器行為改變（閒置休眠），可能影響長期運行的部署架構
2. **Dependency 大更新** — uv pip dry-run 顯示 47 個 packages 會更新/替換，包括：
   - `fastapi 0.139.0`、`pydantic 2.13.4`、`openai 2.24.0`
   - `cryptography 46.0.7`、`anyio 4.14.2`、`rich 14.3.3`
   - 移除 `rich==15.0.0` → 降級回 `rich==14.3.3`
3. **Mixture-of-Agents** — 新的模型預設值設定方式
4. **Gateway 行為改變** — scale-to-zero 可能影響現有排程/cron 的穩定性

---

## ✅ 建議更新時機

**評估：🟡 可等待，建議先測試後更新**

理由：
1. **功能價值高** — MoA、Self-Verification、Background Fan-out、Vertex AI 都是重大功能提升
2. **但跨度大** — 跨 2 個主版本，dependency 變動 47 個包，風險中等
3. **Gateway Scale-to-Zero** 可能影響現有 cron/jobs 的穩定性，建議先在測試環境驗證
4. **v0.18.2 是 same-day patch**，代表 v0.18.0 剛出就有問題被修了，說明 0.18.x 還在快速穩定期

**建議行動：**
- 短期：保持 v0.17.0 不變，繼續使用
- 中期（1-2 週內）：在測試環境執行 `uv pip install --upgrade hermes-agent` 驗證無誤後再更新
- 更新後確認：cron jobs、gateway 連線、WhatsApp/Telegram 通道是否正常

---

*此報告僅供檢查，未執行實際更新。*
