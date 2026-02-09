# Bug Report

### Describe the bug

When using JSX spread children (`{...expression}`) with `jsx: 'preserve'` mode, the spread syntax is being incorrectly transformed. Instead of preserving the original JSX spread child syntax, it's being replaced with just `...`, which breaks the JSX output.

### Reproduction

```js
// Input JSX with spread child
const element = <div>{...items}</div>

// With jsx: 'preserve' mode
// Expected output: <div>{...items}</div>
// Actual output: <div>...</div>
```

The expression part of the spread child is being removed when it should be preserved in preserve mode.

### Expected behavior

When `jsx: 'preserve'` is set in the options, JSX spread children should remain unchanged in the output. The `{...expression}` syntax should be kept as-is rather than being transformed.

### System Info
- Rollup version: latest
- jsx mode: preserve

---
Repository: /testbed
