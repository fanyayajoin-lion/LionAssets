---
document_type: knowledge_atom
version: 1.0.0
author: 業萱
created: 2026-07-09
updated: 2026-07-09
---
# 知識原子寫作規範模板

## Purpose
標準化知識原子的寫作格式，確保每個文件只講一件事、可獨立理解、可被 Skill 引用。

## Structure
```yaml
---
title: 知識原子名稱
type: knowledge_atom
domain: strategy/framework/tactics
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: [[來源文件]]
tags: [標籤1, 標籤2]
---
```

## Content Requirements
1. **核心命題**：一句話總結（用 > 引用格式）
2. **模型/框架**：結構化的知識內容（表格、條列、流程圖）
3. **應用場景**：什麼時候用、怎麼用
4. **常見陷阱**：容易犯的錯誤
5. **關聯頁面**：≥2 個雙向連結

## Quality Standard
- 字數：300-1500 字
- 一個文件只講一個概念
- 避免技術術語，用白話文
- 必须有關聯頁面

## Example
見：knowledge/ai-five-stages.md

## Common Mistakes
- 一個文件講太多概念
- 沒有核心命題
- 沒有關聯頁面
- 用技術術語代替白話解釋

## Related Knowledge
- [[knowledge/README]]
- [[wiki/concepts]]
