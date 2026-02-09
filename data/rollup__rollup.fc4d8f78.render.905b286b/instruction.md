# Bug Report

### Describe the bug

When using JSX fragments (`<>...</>`) with `jsx: 'preserve'` mode, the fragments are being incorrectly transformed instead of being preserved as-is. The output contains variable references that shouldn't be there when preserve mode is enabled.

### Reproduction

```js
// Input code with JSX fragment
const element = (
  <>
    <div>Content</div>
  </>
)

// rollup.config.js
export default {
  // ...
  jsx: 'preserve'
}
```

### Expected behavior

With `jsx: 'preserve'` mode, JSX fragments should remain untouched in the output:
```js
const element = (
  <>
    <div>Content</div>
  </>
)
```

### Actual behavior

The fragments are being transformed even though preserve mode is set, resulting in unexpected variable references in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
