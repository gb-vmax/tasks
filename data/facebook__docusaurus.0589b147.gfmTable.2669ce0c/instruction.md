# Bug Report

### Describe the bug

After a recent update, GFM tables are not being parsed correctly. The markdown processor seems to fail when encountering table syntax, and tables are either not rendered at all or rendered as plain text instead of proper table structures.

### Reproduction

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

When processing this markdown with the GFM plugin, the table is not being recognized or tokenized properly. The output doesn't show a formatted table.

### Expected behavior

The markdown table should be parsed and converted into proper table tokens/nodes that can be rendered as HTML tables. The tokenizer should recognize the table structure and apply the appropriate transformations.

### System Info

- remark-gfm version: 4.0.0
- The issue appears to be related to table parsing specifically

---
Repository: /testbed
