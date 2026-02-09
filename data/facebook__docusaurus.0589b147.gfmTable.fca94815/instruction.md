# Bug Report

### Describe the bug

I'm encountering an issue with GFM (GitHub Flavored Markdown) table parsing. Tables in markdown are not being recognized or parsed correctly. The parser seems to completely ignore table syntax and treats it as regular text instead.

### Reproduction

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

When parsing this markdown with the GFM plugin, the table structure is not being detected. The content just gets treated as plain text rather than being converted into a proper table structure.

### Expected behavior

The parser should recognize the table syntax and generate the appropriate AST nodes for the table, including table rows, cells, and alignment information. Tables should be properly tokenized and resolved.

### Additional context

This appears to have started happening recently. Previously, GFM tables were working fine. Simple tables with headers and data rows are not being parsed at all.

---
Repository: /testbed
