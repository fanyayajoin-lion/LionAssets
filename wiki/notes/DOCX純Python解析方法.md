---
title: "從 DOCX 提取塔羅牌內容的純 Python 方法"
created: 2026-07-11
updated: 2026-07-11
type: note
tags: [DOCX解析, 純Python, 塔羅專案, 檔案處理]
sources:
  - "黑獅每日萃取 — 20260709-20260710 CLI 對話"
lion_score:
  變現價值: 2
  可複製性: 3
  長期價值: 2
  顧問可用性: 2
  內容延展性: 2
---

# 從 DOCX 提取塔羅牌內容的純 Python 方法

## 摘要

在塔羅靈數專案中，需要從 DOCX 檔案提取 22 張塔羅牌的完整內容。由於 pip 安裝受阻，改用純 Python 標準庫直接解析 DOCX 內部 XML 結構。

## 技術要點

DOCX 本質上是 ZIP 壓縮的 XML 檔案：

1. 用 `zipfile` 模組打開 .docx
2. 讀取 `word/document.xml`
3. 用 `xml.etree.ElementTree` 解析
4. 提取段落內容

## 關鍵程式碼模式

```python
import zipfile
import xml.etree.ElementTree as ET

with zipfile.ZipFile('file.docx') as z:
    xml_content = z.read('word/document.xml')
    root = ET.fromstring(xml_content)
    # 提取所有 <w:p> 段落元素
```

## 分割策略

用 `$499N` 模式（價格標記）作為分割點，將 22 張牌內容分開。

## 寫入 JS 的注意事項

- Python f-string 中的 `}` 會被解釋為格式化字元
- 寫 JS template literal 時要用字符串拼接而非 f-string
- 或用 `write_file` 工具直接寫，避開 Python 字串問題

## 部署驗證

- `npm run build` 成功：20.49s, 1813 modules, 5 chunks
- Firebase 部署到 `https://liontarot22-web.web.app`
- 所有頁面（Home、Report、Match、Course）正常運作

## 關聯

- [[塔羅靈數專案]] — 塔羅 v5 專案記錄（待建立）
- [[GPT與Codex使用時機對比]] — 純 Python 解析是 Codex 執行層面的技巧

## 來源

- 對話 session: 20260709_114058_1ac455 (CLI)
- 時間: 2026-07-09 至 2026-07-10
