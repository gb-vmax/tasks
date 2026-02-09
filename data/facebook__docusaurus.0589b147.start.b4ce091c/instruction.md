# Bug Report

### Describe the bug

I'm encountering an issue with GFM table parsing where tables are not being recognized correctly in certain contexts. It seems like lazy continuation lines are being handled incorrectly, causing valid table rows to be skipped or not parsed as expected.

### Reproduction

```markdown
Some text before the table

| Header 1 | Header 2 |
| -------- | -------- |
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

When parsing the above markdown with GFM tables enabled, the table body rows are not being processed correctly. The table header is recognized, but subsequent rows in the table body are being treated as regular paragraph content instead of table rows.

This appears to happen specifically when there's content before the table and the parser needs to determine whether a line is a continuation of the table or not.

### Expected behavior

All table rows (both header and body) should be parsed and rendered as a proper table structure. The markdown above should produce a complete table with one header row and two body rows.

### System Info
- remark-gfm version: 4.0.0
- Parser: markdown-based

---
Repository: /testbed
