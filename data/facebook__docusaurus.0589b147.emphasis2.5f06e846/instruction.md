# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis/italic rendering in MDX content. When I use single asterisks or underscores for emphasis (italic text), the output is being rendered as bold (strong) instead of italic.

### Reproduction

```mdx
This text should be *italic* but appears bold.

This _should also be italic_ but is also bold.
```

When processing the above MDX content, both emphasis markers (`*text*` and `_text_`) are rendering as bold text instead of italic text.

### Expected behavior

Single asterisks or underscores should create italic/emphasis text (`<em>` tags), while double asterisks or underscores should create bold/strong text (`<strong>` tags).

Expected output:
- `*text*` → `<em>text</em>` (italic)
- `**text**` → `<strong>text</strong>` (bold)

Actual output:
- `*text*` → `<strong>text</strong>` (bold)

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
