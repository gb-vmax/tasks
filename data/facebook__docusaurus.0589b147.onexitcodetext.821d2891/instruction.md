# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in markdown. When using backticks for inline code, the text content appears to be getting duplicated or incorrectly assigned.

### Reproduction

```js
const markdown = "This is `inline code` in text";
// Process the markdown
// Expected: code node should contain "inline code"
// Actual: the value seems to be assigned incorrectly
```

When parsing markdown with inline code blocks (text wrapped in backticks), the resulting AST node structure doesn't match what's expected. The code text value appears to be handled incorrectly during the parsing phase.

### Expected behavior

Inline code blocks should be parsed correctly with the proper text content assigned to the code node. The value should reflect exactly what's between the backticks.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
