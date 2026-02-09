# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where it seems to be silently catching errors in the `onsuccessfulcheck` callback. The function now returns early when `info` is falsy and wraps the `restore()` call in a try-catch block that swallows exceptions.

### Reproduction

```js
// When the tokenizer's onsuccessfulcheck is called with undefined/null info
// The function now returns early instead of attempting to restore state

const result = onsuccessfulcheck(_, null);
// Expected: Should throw an error or handle the missing info properly
// Actual: Function returns early without any indication of the problem
```

The issue appears to be in the tokenizer logic where state restoration is being skipped silently. This could lead to corrupted parser state that's difficult to debug since errors are being suppressed.

### Expected behavior

The parser should either:
1. Properly handle the case when `info` is missing with appropriate error messaging
2. Not call `onsuccessfulcheck` with invalid parameters in the first place

Silently catching and ignoring errors makes it very difficult to diagnose parsing issues.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
