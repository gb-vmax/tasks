# Bug Report

### Describe the bug

When using JSX spread children (`{...expression}`) with `jsx: 'preserve'` mode, the spread syntax is being incorrectly transformed instead of being preserved as-is. The spread operator and braces are being removed when they should remain untouched in preserve mode.

### Reproduction

```js
// Input JSX with spread child
const element = <div>{...items}</div>

// With jsx: 'preserve' in rollup config
export default {
  jsx: 'preserve'
}
```

### Expected behavior

When `jsx: 'preserve'` is set, the JSX spread child syntax should be left unchanged:
```js
<div>{...items}</div>
```

### Actual behavior

The spread syntax is being transformed/removed even in preserve mode, which breaks the original JSX structure.

### System Info
- Rollup version: latest
- JSX mode: preserve

---
Repository: /testbed
