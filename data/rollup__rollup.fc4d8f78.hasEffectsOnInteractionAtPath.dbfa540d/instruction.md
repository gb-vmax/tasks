# Bug Report

### Describe the bug

I'm encountering an issue with multi-expression sequences where side effects are not being properly detected. When using comma-separated expressions, the bundler seems to be incorrectly analyzing which expressions have side effects, leading to unexpected behavior in the output.

### Reproduction

```js
// Example with multiple expressions in a sequence
const result = (sideEffect1(), sideEffect2(), getValue());

// The first expression in the sequence is being ignored
// when checking for side effects, causing incorrect
// tree-shaking or optimization decisions
```

This appears to affect any code pattern that uses the comma operator with multiple expressions, particularly when the first expression has side effects that should be preserved.

### Expected behavior

All expressions in a multi-expression sequence should be properly analyzed for side effects. If any expression in the sequence has side effects, the entire sequence should be treated accordingly. The first expression should not be skipped during side effect analysis.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
