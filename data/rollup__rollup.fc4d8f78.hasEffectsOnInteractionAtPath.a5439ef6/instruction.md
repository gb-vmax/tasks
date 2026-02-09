# Bug Report

### Describe the bug

I'm experiencing an issue with binary expressions where property access on the result is not being handled correctly. It seems like the side effect detection for binary expression results has changed behavior.

When accessing properties on binary expression results (like `(a + b).toString()` or `(x || y).prop`), the code is now treating these accesses differently than before, which is causing unexpected behavior in my build output.

### Reproduction

```js
// Example case that's behaving unexpectedly
const result = (value1 + value2).toString();

// Or when accessing properties on logical expressions
const data = (obj1 || obj2).property;

// These property accesses seem to be evaluated differently now
```

The issue appears to be related to how property paths are being evaluated on binary expression results. Previously, accessing properties on these expressions worked as expected, but now there seems to be a change in how the interaction paths are being checked.

### Expected behavior

Property access on binary expression results should work consistently. When you access a property like `.toString()` or `.prop` on the result of a binary expression, it should be treated the same way as accessing properties on any other value.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
