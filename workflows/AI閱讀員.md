# AI 閱讀員 Workflow

## 使用時機

每天晚上 23:00 批次讀取 `inbox/raw/` 新增資料，將外部內容轉成老闆能用的理解。

## 核心原則

- 不把原文直接丟進正式知識庫。
- AI 閱讀員不是單純摘要器，要提取商業判斷。
- 沒有案例或數據時，標記「本文未提供」，不要硬編。
- 輸出寫入 `inbox/processed/`。

## 處理順序

```text
讀取 inbox/raw
↓
抓網頁正文 / YouTube transcript / OCR
↓
清洗成短材料
↓
AI 閱讀與提取
↓
輸出 processed markdown
↓
Discord #daily-digest 顯示整理結果
```

## 固定輸出格式

```markdown
# 文章名稱

來源：
日期：
類型：
原始位置：

## 核心觀點
1.
2.
3.

## 值得借鑑
1.
2.
3.

## 適合群獅應用
1.
2.
3.

## 案例
1.
2.
3.

## 數據
1.
2.
3.

## 可行動方法
1.
2.
3.

## 相關主題
- [[個人品牌]]
- [[顧問式銷售]]

## 相關人物 / 品牌 / 工具
- [[Justin Welsh]]
- [[Alex Hormozi]]

## 可延伸內容
- Threads：
- FB：
- IG 輪播：
```

## 省 token 規則

- 短文字不呼叫 AI。
- 重複網址不重跑 AI。
- 網頁只送標題、摘要與重點段落。
- YouTube 先抓 transcript，抓不到就 `needs-review`。
- 截圖先 OCR，再交給 AI。
