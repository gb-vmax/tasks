# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where `export` statements without a space after the keyword are being incorrectly accepted. The parser seems to be consuming characters even when they shouldn't form a valid export statement.

### Reproduction

```js
// This should NOT be valid but is being parsed:
exportSomething

// Only this should be valid:
export Something
```

When parsing MDX content, the tokenizer appears to accept `export` followed immediately by any character (without the required space), which leads to invalid syntax being treated as valid ESM exports.

### Expected behavior

The parser should only recognize `export` when it's followed by a space (code 32). Currently it seems to be accepting `export` followed by any character and treating it as a valid export statement, which breaks proper MDX validation.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
