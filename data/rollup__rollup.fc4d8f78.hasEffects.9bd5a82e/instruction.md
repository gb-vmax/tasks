# Bug Report

### Describe the bug

I'm experiencing an issue where sequence expressions (comma operator) are not being properly evaluated for side effects. It seems like expressions that should be considered as having side effects are being treated as if they don't have any effects at all.

### Reproduction

```js
// This sequence expression contains side effects but they're not being detected
const result = (sideEffect1(), sideEffect2(), finalValue);

// Similarly, this pattern is also affected:
(console.log('test'), someFunction(), value)
```

When bundling code that uses the comma operator with expressions that have side effects (like function calls, assignments, etc.), the behavior is inverted - code that should be preserved due to side effects is being removed, and code without side effects might be kept.

### Expected behavior

Sequence expressions should correctly identify when any of their sub-expressions have side effects. If any expression in the sequence has side effects, the entire sequence should be marked as having effects.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The detection logic for side effects in comma-separated expressions appears to be backwards.

---
Repository: /testbed
