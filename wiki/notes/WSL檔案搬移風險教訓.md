---
title: "WSL 操作 Windows NTFS 磁碟區的檔案搬移風險教訓"
created: 2026-07-11
updated: 2026-07-11
type: note
tags: [技術教訓, WSL, NTFS, 檔案安全, shutil, 災難復原]
sources:
  - "黑獅每日萃取 — 20260710 CLI 對話"
lion_score:
  變現價值: 2
  可複製性: 3
  長期價值: 4
  顧問可用性: 3
  內容延展性: 3
---

# WSL 操作 Windows NTFS 磁碟區的檔案搬移風險教訓

## 摘要

在 DFP 過往資料分類任務中，使用 Python 的 `shutil.move()` 在 WSL 下操作 Windows NTFS 磁碟區（/mnt/c/），導致 3,267 個檔案被永久刪除。這是一個重要的技術教訓，值得記錄。

## 事故經過

1. 老闆要求整理 `~/Desktop/DFP過往` 目錄（3,267 個檔案）
2. 先建立了新目錄結構（01-業務系統、02-講師運營系統等）
3. 用 `shutil.move()` 搬移檔案
4. 結果：3,267 個檔案只剩 15 個
5. 目錄結構還在，但所有檔案都不見了

## 原因分析

`shutil.move()` 在 WSL 操作 NTFS 磁碟區時：
- 如果遇到目標路徑不存在（如 `01-業務系統/公司背景/` 目錄未建立），可能跳過
- 如果遇到同名檔案衝突或特殊字元，可能觸發異常
- 異常被 try/except 吞掉後，回滾機制失敗，檔案永久刪除
- **WSL 的刪除不經過 Windows 回收筒**

## 教訓

1. **絕對不要用 `shutil.move()` 操作 /mnt/c/ 路徑**
2. 正確做法：`cp` → 驗證 → `rm`
3. 大規模搬移前先做 dry run（模擬搬移但不執行）
4. 重要資料先做完整備份
5. 遇到 1000+ 檔案的搬移，分批執行，每批驗證

## 替代方案

```bash
# 安全做法：先複製再驗證再刪除
rsync -av --progress /mnt/c/source/ /mnt/c/target/
# 驗證後
rm -rf /mnt/c/source/*
```

或使用 `cp` + 手動驗證：
```python
shutil.copy2(src, dst)  # 先複製
# 驗證內容一致
os.remove(src)  # 再刪除
```

## 關鍵洞察

這個教訓的核心是**跨平台檔案操作的風險意識**。WSL 和 Windows 的檔案系統行為不完全一致，特别是在 NTFS 磁碟區上。對於重要資料，永遠採用「先複製、驗證、再刪除」的三段式操作。

## 關聯

- [[hermes-agent-overview]] — Hermes 運行環境中的 WSL 使用注意事項
- [[數據作證規則]] — AI 互動行為準則：操作前必須驗證
- [[GPT與Codex使用時機對比]] — 這類技術陷阱適合用 Codex 執行，但要加保護措施

## 來源

- 對話 session: 20260710_151004_6fc5ed (CLI)
- 時間: 2026-07-10 下午
