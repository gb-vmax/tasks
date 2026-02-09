# Bug Report

### Describe the bug

JSX spread children are being incorrectly transformed when using `jsx: 'preserve'` mode. The spread syntax is being removed entirely instead of being preserved as expected.

### Reproduction

```jsx
// Input JSX with spread child
const element = <div>{...items}</div>;
```

When compiling with `jsx: 'preserve'` option, the spread child syntax is being removed completely instead of being kept as-is.

### Expected behavior

With `jsx: 'preserve'` mode, the JSX spread child should remain unchanged in the output:
```jsx
<div>{...items}</div>
```

Instead, the spread syntax is being stripped out, resulting in malformed or empty output.

### System Info
- Rollup version: latest
- JSX mode: preserve

---
Repository: /testbed
