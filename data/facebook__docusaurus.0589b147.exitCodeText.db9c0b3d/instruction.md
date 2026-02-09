# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in GFM (GitHub Flavored Markdown) tables. When using inline code with escaped pipe characters inside table cells, the escaping behavior seems incorrect - it's either being applied when it shouldn't be, or not being applied when it should be.

### Reproduction

```markdown
| Column 1 | Column 2 |
|----------|----------|
| `code with \| pipe` | normal text |
```

When parsing this markdown, the inline code block doesn't handle the escaped pipe character correctly. The escape sequences are being processed in the wrong context.

### Expected behavior

Escaped characters in inline code within tables should be handled consistently. The `\|` sequence should be properly escaped/unescaped depending on whether the code is inside or outside a table context.

### System Info
- remark-gfm version: 4.0.0
- Parser: micromark

This seems to have started happening recently. Not sure if this is a regression or if I'm misunderstanding how escaping should work in this context.

---
Repository: /testbed
