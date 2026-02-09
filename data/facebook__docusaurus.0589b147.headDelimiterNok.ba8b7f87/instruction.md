# Bug Report

### Describe the bug

I'm experiencing an issue with GFM table parsing where malformed tables are not being rejected properly. When a table has an invalid delimiter row, the parser seems to be returning incorrect values instead of properly handling the error case.

### Reproduction

```markdown
| Header |
| not a valid delimiter |
| cell |
```

When parsing the above markdown with an invalid table delimiter row (missing colons and dashes), the parser doesn't reject it as expected. The tokenizer appears to be returning unexpected values from the error handling path.

### Expected behavior

Tables with invalid delimiter rows should be properly rejected by the parser, and the tokenizer should handle the error case correctly by calling the nok callback and returning its result.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
