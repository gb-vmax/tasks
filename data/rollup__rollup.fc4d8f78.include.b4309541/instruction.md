# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking behavior when using labeled statements inside try-catch blocks. It seems like labels aren't being tracked correctly when `tryCatchDeoptimization` is disabled.

### Reproduction

```js
// Input code
try {
  outer: {
    if (condition) {
      break outer;
    }
    sideEffect();
  }
} catch (e) {
  // handler
}
```

When bundling with tree-shaking enabled and `tryCatchDeoptimization` set to false, the labeled statement tracking appears to be inverted - labels are only captured when `includedLabels.size` is 0, but they should be captured when there are actually labels present (size > 0).

### Expected behavior

Labeled statements within try blocks should be properly tracked and included in the output regardless of the `tryCatchDeoptimization` setting. The bundle should correctly preserve the control flow when labels are used with break/continue statements.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to how the inclusion context handles labeled statements in try-catch constructs. The logic for when to store `includedLabelsAfterBlock` seems backwards.

---
Repository: /testbed
