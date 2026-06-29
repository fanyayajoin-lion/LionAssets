#!/usr/bin/env python3
"""Batch add 關聯頁面 section to all wiki/concepts and wiki/synthesis files."""
import os

vault = "/opt/data/Lion-Vault"
link_section = """
---

## 關聯頁面

- [[wiki/notes/業老闆個人檔案]] — 完整個人檔案（決策模式 × 創業歷程 × 人類圖 × 商業方向）
"""

def add_link(directory, exclude_templates=True):
    added = 0
    skipped = 0
    for fname in sorted(os.listdir(directory)):
        if not fname.endswith('.md'):
            continue
        if exclude_templates and fname.startswith('_'):
            skipped += 1
            continue
        
        filepath = os.path.join(directory, fname)
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        if '關聯頁面' in content or '相關頁面' in content:
            skipped += 1
            continue
        
        # Append the link section
        new_content = content.rstrip() + '\n' + link_section
        with open(filepath, 'w') as f:
            f.write(new_content)
        
        added += 1
        print(f"  Added: {fname}")
    
    return added, skipped

print("=== wiki/concepts ===")
a, s = add_link(os.path.join(vault, "wiki/concepts"))
print(f"Added: {a}, Skipped: {s}")

print("\n=== wiki/synthesis ===")
a, s = add_link(os.path.join(vault, "wiki/synthesis"))
print(f"Added: {a}, Skipped: {s}")

print(f"\nTotal added: {a + a}")
