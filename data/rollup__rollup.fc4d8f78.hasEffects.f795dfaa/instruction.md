# Bug Report

### Describe the bug

When using try-catch statements in my code with tree-shaking enabled, I'm seeing unexpected behavior where single-statement try blocks are being completely removed from the bundle even when they should be preserved.

### Reproduction

```js
try {
  someFunction();
} catch (e) {
  // error handling
}
```

After bundling with rollup, the entire try-catch block gets removed from the output even though `someFunction()` has side effects and should be preserved.

### Expected behavior

Try-catch blocks with a single statement should be included in the bundle when tree-shaking is enabled, especially when the statement inside has side effects. The block should only be removed if it's completely empty.

### System Info
- Rollup version: latest
- tryCatchDeoptimization: enabled

---
Repository: /testbed
