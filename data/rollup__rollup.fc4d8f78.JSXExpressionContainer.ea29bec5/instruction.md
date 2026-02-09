# Bug Report

### Describe the bug

JSX expression containers are being stripped out when they shouldn't be. When using JSX with `jsx.mode` set to `'preserve'`, the curly braces around expressions are being removed from the output, which breaks the JSX syntax.

### Reproduction

```js
// Input JSX
const element = <div>{someExpression}</div>

// With jsx.mode: 'preserve'
// Expected output: <div>{someExpression}</div>
// Actual output: <div>someExpression</div>
```

The curly braces are being removed even though the mode is set to preserve the JSX syntax. This makes the output invalid JSX.

### Expected behavior

When `jsx.mode` is set to `'preserve'`, the JSX expression container syntax (curly braces) should be kept in the output. The braces should only be removed when the mode is NOT set to preserve (e.g., when transforming JSX).

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
