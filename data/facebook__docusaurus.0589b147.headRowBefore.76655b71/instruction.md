# Bug Report

### Describe the bug

I'm encountering an issue with GFM table parsing where the table structure appears to be malformed. When parsing markdown tables, the resulting AST seems to have incorrect nesting - the table head and table row elements are in the wrong order.

### Reproduction

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

When this table is parsed, the AST structure shows `tableRow` being entered before `tableHead`, which doesn't match the expected hierarchy. This causes downstream processing that relies on proper nesting order to fail or produce incorrect results.

### Expected behavior

The parser should enter `tableHead` first, then `tableRow` as a child element. The current behavior has them reversed, breaking the expected parent-child relationship in the AST.

Additionally, the `headRowStart` function should return its result properly instead of being called without a return statement.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
