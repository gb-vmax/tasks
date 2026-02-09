# Bug Report

### Describe the bug

When using JSX with `jsx.mode: 'preserve'`, the closing tags are being incorrectly transformed to `)` instead of being preserved as-is. The JSX syntax should remain unchanged when preserve mode is enabled, but the closing elements are getting modified.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.jsx',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  jsx: {
    mode: 'preserve'
  }
}

// src/index.jsx
const Component = () => <div>Hello</div>;
```

### Expected behavior

With `jsx.mode: 'preserve'`, the JSX closing tags should remain as `</div>` in the output. Instead, they're being replaced with `)`.

Expected output:
```jsx
const Component = () => <div>Hello</div>;
```

Actual output:
```js
const Component = () => <div>Hello)
```

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have the logic inverted - preserve mode should keep JSX intact, not transform it.

---
Repository: /testbed
