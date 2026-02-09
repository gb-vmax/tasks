# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where the token structure seems to be malformed. When processing directive containers (the `:::` syntax), the parser appears to be creating duplicate or incorrectly ordered token entries.

### Reproduction

```markdown
::: note
This is a directive container
:::
```

When parsing the above markdown with remark-directive, the token tree structure doesn't match the expected format. The `directiveContainer` and `directiveContainerFence` tokens appear to be entered in the wrong order or duplicated.

### Expected behavior

The parser should create a proper token hierarchy:
1. Enter `directiveContainer`
2. Enter `directiveContainerFence`
3. Enter `directiveContainerSequence`
4. Process the opening sequence

Instead, it seems like tokens are being entered in an unexpected order, which could break downstream processing or cause issues with AST generation.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
