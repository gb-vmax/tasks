# Bug Report

### Describe the bug

I'm experiencing an issue with GFM table parsing where table cells with content are not being parsed correctly. When I have a table with data in the cells, the parser seems to be consuming all characters without properly recognizing cell boundaries.

### Reproduction

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell A   | Cell B   |
```

When parsing the above table, the cell content doesn't get properly delimited. The parser appears to be treating the entire row as a single continuous data segment instead of recognizing the pipe (`|`) separators between cells.

### Expected behavior

The table should be parsed with each cell's content properly separated. Each pipe character should act as a delimiter between cells, and the cell content should be correctly extracted.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
