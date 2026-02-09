# Bug Report

### Describe the bug

I'm experiencing an issue with table parsing in GFM (GitHub Flavored Markdown). When a table has an invalid delimiter row, the parser seems to hang or behave unexpectedly instead of properly rejecting the invalid table syntax.

### Reproduction

```markdown
| Header 1 | Header 2 |
| invalid delimiter row without proper dashes
| Cell 1 | Cell 2 |
```

When trying to parse this markdown, the parser doesn't handle the malformed table correctly. It seems like the rejection callback isn't being invoked with the proper code parameter.

### Expected behavior

The parser should properly reject invalid table syntax and continue parsing the rest of the document normally. Invalid tables should be treated as regular text rather than causing parsing issues.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
