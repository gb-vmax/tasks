# Bug Report

### Describe the bug

I'm experiencing an issue with the unicode whitespace checking in the remark-directive parser. When processing markdown content with certain edge cases, the parser is incorrectly accepting `null` character codes as valid whitespace characters, which causes unexpected behavior in directive parsing.

### Reproduction

```js
// When the parser encounters a null character code
const code = null;
// The whitespace check incorrectly returns true
// This causes the parser to treat null as valid whitespace
```

This happens when parsing directives that have unusual formatting or when the input stream ends unexpectedly. The parser should reject null character codes but instead is treating them as valid.

### Expected behavior

The `regexCheck` function should only return `true` for valid character codes that actually match the regex pattern. Null character codes should be rejected and not treated as valid whitespace.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
