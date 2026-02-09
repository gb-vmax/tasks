# Bug Report

### Describe the bug

When using JSX with `jsx.mode` set to `'preserve'`, the closing tags are being incorrectly transformed to `)` instead of being preserved as-is. This breaks the JSX syntax when trying to keep the original JSX structure intact.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.jsx',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  jsx: {
    mode: 'preserve'
  }
}

// src/index.jsx
const Component = () => {
  return <div>Hello World</div>;
}
```

### Expected behavior

When `jsx.mode` is set to `'preserve'`, the JSX closing tags like `</div>` should remain unchanged in the output. Instead, they're being replaced with `)`, resulting in invalid JSX syntax like `<div>Hello World)`.

The preserve mode should keep the original JSX structure intact without any transformations.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
