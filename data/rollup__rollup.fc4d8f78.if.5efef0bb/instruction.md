# Bug Report

### Describe the bug

When `strictDeprecations` is enabled, deprecation warnings are being logged twice - once as an error and once as a warning. This results in duplicate console output for the same deprecation message.

### Reproduction

```js
// Set strictDeprecations to true
const config = {
  strictDeprecations: true
}

// Trigger any deprecation warning
// You'll see the same message logged twice:
// 1. First as an error
// 2. Then as a warning
```

### Expected behavior

When `strictDeprecations` is true, the deprecation should only be logged as an error and should not also appear as a warning. The function should exit after logging the error to avoid duplicate messages.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
