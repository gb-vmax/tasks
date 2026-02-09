# Bug Report

### Describe the bug

I'm encountering an issue with GFM table parsing where table cells with backslash escapes are not being processed correctly. The parser seems to be handling escape sequences in table headers improperly, causing the table structure to break.

### Reproduction

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell with \| pipe | Normal cell |
```

When parsing the above table, the escaped pipe character (`\|`) in the first cell is not handled correctly, and the table structure becomes malformed. The cell content after the escaped pipe is treated as a separate column instead of being part of the same cell.

### Expected behavior

The parser should recognize `\|` as an escaped pipe character and treat it as literal text within the cell, not as a column delimiter. The table should render with two columns as defined in the header row.

### Additional context

This seems to affect any table cell that contains backslash escape sequences in the header or data rows. The issue appears to be related to how the tokenizer processes escape characters within table data.

---
Repository: /testbed
