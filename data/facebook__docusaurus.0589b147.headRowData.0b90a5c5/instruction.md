# Bug Report

### Describe the bug

I'm experiencing issues with table parsing in GFM (GitHub Flavored Markdown). When parsing markdown tables, the pipe character (`|`) is not being properly recognized as a cell delimiter, causing the table structure to break.

### Reproduction

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

When parsing the above table, the cells are not being separated correctly. The pipe characters that should delimit table cells are being treated as regular data instead of delimiters.

### Expected behavior

The parser should recognize `|` (character code 124) as a table cell delimiter and properly separate the table into individual cells. Each cell's content should be extracted correctly.

### Additional context

This seems to affect the tokenization logic for table headers. The table structure becomes malformed and cells run together instead of being properly separated.

---
Repository: /testbed
