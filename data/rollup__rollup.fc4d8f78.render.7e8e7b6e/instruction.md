# Bug Report

### Describe the bug

When using logical expressions (e.g., `||` or `&&`) in code that gets tree-shaken, the output is incorrectly formatted with extra whitespace or missing operators. This appears to happen specifically when the right side of a logical expression is included in the output but the left side is removed.

### Reproduction

```js
// Input code
const result = false || someFunction();

// After tree-shaking, the output might be:
const result = |someFunction();
// or have incorrect spacing around the operator
```

The issue seems to occur when the bundler attempts to remove dead code from logical expressions. The operator character itself or surrounding whitespace gets mangled in the process.

### Expected behavior

When tree-shaking logical expressions, the output should maintain proper syntax. If the left side is removed, the entire logical expression should be replaced with just the right side operand, without leaving behind operator fragments or incorrect spacing.

Expected output:
```js
const result = someFunction();
```

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing syntax errors in the bundled output and breaking production builds. Any help would be appreciated!

---
Repository: /testbed
