# Bug Report

### Describe the bug

When using JSX spread children (`{...expression}`) with `jsx: 'preserve'` mode, the spread syntax is being incorrectly removed from the output. The `...` operator disappears even though the JSX should be preserved as-is.

### Reproduction

```js
// Input JSX
const element = <div>{...items}</div>

// With jsx: 'preserve' option
// Expected output: <div>{...items}</div>
// Actual output: <div>{items}</div>
```

The spread operator gets stripped out when it should be kept intact in preserve mode.

### Expected behavior

When `jsx: 'preserve'` is set in the options, JSX spread children should remain unchanged in the output, including the `...` spread operator.

### Additional context

This appears to affect any JSX code using spread children syntax when preserve mode is enabled. The spread operator is critical for the syntax to be valid JSX.

---
Repository: /testbed
