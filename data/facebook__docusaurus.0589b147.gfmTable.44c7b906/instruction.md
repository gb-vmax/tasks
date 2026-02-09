# Bug Report

### Describe the bug

Tables are not being parsed correctly in markdown. When I try to use GFM (GitHub Flavored Markdown) tables in my content, they're just rendered as plain text instead of being converted to proper table elements.

### Reproduction

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

Expected this to be parsed as a table, but it's being treated as regular text. The table syntax is completely ignored.

### Steps to reproduce
1. Create a markdown file with a GFM table
2. Process it with the remark parser
3. The table is not recognized and remains as plain text

### Expected behavior
The markdown table should be parsed into proper table nodes in the AST and rendered as an HTML table.

### Additional context
This seems to have broken recently. Tables were working fine before. Not sure what changed but the GFM table plugin doesn't seem to be recognizing table syntax anymore.

---
Repository: /testbed
