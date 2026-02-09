# Bug Report

### Describe the bug

The `trackSegmentEvent` function throws an error when called without arguments in test environments. This breaks existing tests that were previously working fine.

### Reproduction

```js
// This now throws an error in tests
global.main.trackSegmentEvent();
```

The error message is:
```
Error: Event name required
```

### Expected behavior

The function should accept being called with no arguments (like it did before) and simply do nothing, similar to how `trackPageView` behaves. This is especially important for test mocks where we often don't care about the actual parameters.

### System Info
- Running in Jest test environment
- Started happening recently, possibly after a test setup change

---
Repository: /testbed
