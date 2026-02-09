# Bug Report

### Describe the bug
When using JSX spread children syntax (`{...expression}`) with `jsx: 'preserve'` mode, the spread operator and braces are being incorrectly removed from the output. The code should be preserved as-is when using preserve mode, but instead it's getting transformed.

### Reproduction
```jsx
// Input JSX with preserve mode enabled
const element = (
  <div>
    {...items}
  </div>
)

// Expected output (preserved):
// <div>
//   {...items}
// </div>

// Actual output (incorrectly transformed):
// <div>
//   items
// </div>
```

### Expected behavior
When `jsx: 'preserve'` is set in the options, JSX spread children should remain unchanged in the output. The `{...expression}` syntax should be preserved exactly as written.

### System Info
- Rollup version: latest
- JSX mode: preserve

---
Repository: /testbed
