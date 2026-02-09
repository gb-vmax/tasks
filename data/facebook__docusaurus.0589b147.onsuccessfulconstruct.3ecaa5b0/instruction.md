# Bug Report

### Describe the bug

I'm experiencing an issue with the tokenizer where it crashes with a `TypeError` when processing certain markdown constructs. The error occurs when `info` is undefined or when `info.from` is not available during token construction.

### Reproduction

```js
// This causes a crash when tokenizing specific markdown patterns
const parser = createTokenizer(parserInstance, initializeFn, fromValue);

// The error happens during construct processing when info object
// is missing or doesn't have the expected properties
```

The issue appears when processing edge cases in markdown parsing where the construct callback receives an undefined or incomplete info object.

### Expected behavior

The tokenizer should handle cases where `info` might be undefined or where `info.from` is not set, without throwing errors. It should gracefully fall back or skip processing in these scenarios.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
