# Bug Report

### Describe the bug

String parsing is producing incorrect output when reading string literals. The parsed string includes the opening quote character at the beginning, which shouldn't be part of the final string value.

### Reproduction

```js
// When parsing a string literal like:
const input = '"hello"'

// The parser returns:
// '"hello' instead of 'hello'

// Similarly for single quotes:
const input2 = "'world'"
// Returns: "'world" instead of "world"
```

The opening quote character is being included in the parsed string output when it should be skipped.

### Expected behavior

String literals should be parsed without their surrounding quote characters. For example:
- Input: `"test"` → Expected output: `test`
- Input: `'test'` → Expected output: `test`

The opening quote should not be part of the final string token value.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: Latest

---
Repository: /testbed
