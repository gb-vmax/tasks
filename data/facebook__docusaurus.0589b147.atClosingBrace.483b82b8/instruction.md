# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where the label closing sequence doesn't properly exit the string type token. This causes the parser state to become inconsistent when processing directive labels.

### Reproduction

```js
// Parse a directive with a label
const input = ':directive[label text]'

// The parser processes the label but doesn't properly close the string type
// This leads to incorrect token structure in the AST
```

When parsing directives with labels, the closing brace handler is not exiting the `stringType` token before exiting the `type` token. This breaks the expected token hierarchy and can cause downstream parsing issues.

### Expected behavior

The parser should properly exit all token types in the correct order:
1. Exit `stringType` when encountering the closing brace
2. Enter and exit the closing `markerType` 
3. Exit the parent `type`

The token structure should be well-formed with all opened tokens properly closed.

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-extension-directive

---
Repository: /testbed
