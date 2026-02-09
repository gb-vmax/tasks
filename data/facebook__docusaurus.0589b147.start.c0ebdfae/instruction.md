# Bug Report

### Describe the bug

I'm experiencing an issue with GitHub Flavored Markdown (GFM) table parsing. When trying to parse tables in certain contexts, the parser seems to be incorrectly identifying table continuation rows. Specifically, tables that should be parsed as body rows are being treated as header rows (or vice versa), causing the table structure to be completely wrong.

### Reproduction

```markdown
Some text before

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |

More text after
```

When parsing this markdown, the table rows after the delimiter row are not being recognized correctly. The parser appears to be making incorrect decisions about whether a row should be treated as part of the table head or table body.

### Expected behavior

The parser should correctly identify:
1. The first row as the table header
2. The delimiter row (with dashes)
3. Subsequent rows as table body rows

Each row should be properly categorized and the resulting table structure should reflect the markdown input accurately.

### Additional context

This seems to happen when the parser is examining previous events to determine the context of the current row. The logic for determining whether we're continuing a table head or starting/continuing a table body appears to be faulty.

---
Repository: /testbed
