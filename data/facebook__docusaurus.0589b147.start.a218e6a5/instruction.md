# Bug Report

### Describe the bug
When parsing GFM tables, the table structure is not being recognized correctly. Tables that should be parsed as having a header row followed by body rows are instead being parsed with the header and body reversed or not recognized at all.

### Reproduction
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

When parsing this table, the header row and body rows are not being differentiated correctly. The parser seems to be confusing which row should be treated as the table head versus table body.

### Expected behavior
The first row should be recognized as `tableHead` and subsequent rows after the delimiter should be recognized as `tableRow` (body rows). The table structure should maintain the correct hierarchy.

### Additional context
This appears to be related to how the parser is traversing backwards through events to determine the current table state. The logic for identifying whether we're in a header or body context seems to be inverted.

---
Repository: /testbed
