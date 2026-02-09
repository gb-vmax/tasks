# Bug Report

### Describe the bug

When using JSX with `jsx.mode: 'preserve'`, the curly braces from JSX expression containers are being removed from the output. This is breaking the JSX syntax in the preserved output.

### Reproduction

```js
// Input JSX
const element = <div>{someVariable}</div>;

// With jsx.mode: 'preserve'
// Expected output: <div>{someVariable}</div>
// Actual output: <div>someVariable</div>
```

The curly braces that wrap the expression are being stripped out even though the JSX mode is set to preserve the original syntax.

### Expected behavior

When `jsx.mode` is set to `'preserve'`, the JSX syntax including expression container braces should remain intact in the output. The braces should only be removed when the mode is set to transform the JSX (e.g., `'classic'` or `'automatic'`).

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
