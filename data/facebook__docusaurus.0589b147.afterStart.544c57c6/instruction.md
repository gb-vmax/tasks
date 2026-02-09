# Bug Report

### Describe the bug

I'm experiencing an issue with directive label parsing where empty labels are being handled incorrectly. When a directive has an empty label (i.e., `[]`), the parser seems to be processing it in an unexpected way.

### Reproduction

```js
// Example directive with empty label
const input = ':directive[]'

// The parser should recognize this as a directive with an empty label
// but it's not being parsed correctly
```

### Expected behavior

Directives with empty labels like `:directive[]` should be properly recognized and parsed. The closing bracket immediately after the opening bracket should be detected as an empty label, not treated as regular content.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
