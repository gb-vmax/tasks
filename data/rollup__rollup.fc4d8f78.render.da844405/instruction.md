# Bug Report

### Describe the bug

JSX fragments are being incorrectly transformed when using `jsx: { mode: 'preserve' }` option. The fragments should remain unchanged in preserve mode, but they're being replaced with the fragment variable instead.

### Reproduction

```js
// Input JSX with fragment
const element = (
  <>
    <div>Content</div>
  </>
)

// rollup.config.js
export default {
  // ...
  jsx: {
    mode: 'preserve'
  }
}
```

### Expected behavior

When `mode: 'preserve'` is set, JSX fragments (`<>` and `</>`) should be left as-is in the output. Currently they're being transformed to use the fragment variable even though preserve mode is explicitly enabled.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
