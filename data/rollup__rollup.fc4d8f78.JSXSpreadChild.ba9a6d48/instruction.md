# Bug Report

### Describe the bug

When using JSX spread children with `jsx: 'preserve'` mode, the output is being incorrectly transformed. The spread syntax should be preserved as-is when using preserve mode, but instead it appears to be getting mangled or removed.

### Reproduction

```jsx
const element = <div>{...items}</div>
```

With `jsx: 'preserve'` in the rollup config:

```js
export default {
  // ...
  jsx: 'preserve'
}
```

### Expected behavior

When `jsx: 'preserve'` is set, the JSX spread child syntax `{...items}` should remain unchanged in the output. The preserve mode should keep the original JSX syntax intact.

### Actual behavior

The spread syntax is being transformed/removed even when preserve mode is enabled. It seems like the condition for when to apply transformations might be inverted.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
