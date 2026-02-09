# Bug Report

### Describe the bug

I'm encountering an issue with table parsing in remark-gfm where certain malformed tables cause the parser to hang or not properly reject invalid table syntax. The parser seems to get stuck when it encounters specific edge cases in table delimiters.

### Reproduction

```markdown
| Header |
|--------|
```

When parsing tables with this structure, the parser doesn't handle the delimiter row validation correctly in certain scenarios. The issue appears to be related to how the parser handles the end of delimiter rows.

This seems to have started happening recently and affects table parsing reliability.

### Expected behavior

The parser should either properly parse valid tables or cleanly reject invalid table syntax without hanging or causing unexpected behavior.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
