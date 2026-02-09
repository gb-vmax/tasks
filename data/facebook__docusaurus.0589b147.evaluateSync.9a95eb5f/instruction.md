# Bug Report

### Describe the bug

I'm encountering an issue where `evaluateSync` doesn't properly handle errors when evaluating expressions with unknown operators. When an invalid operator is used in an expression, the function returns `null` instead of throwing an error, even when `throwOnError` is set to `true` (which is the default).

### Reproduction

```js
const result = evaluateSync(['+', 'x', 'y'], { x: 5, y: 3 });
// Works fine, returns 8

const result2 = evaluateSync(['unknown_op', 'x', 'y'], { x: 5, y: 3 });
// Expected: Error thrown
// Actual: Returns null
```

The issue also occurs with other error conditions during evaluation. It seems like the error handling logic is swallowing exceptions incorrectly.

### Expected behavior

When `throwOnError` is `true` (the default), the function should throw an error when encountering unknown operators or other evaluation errors. The function should only return `null` silently when `throwOnError` is explicitly set to `false`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
