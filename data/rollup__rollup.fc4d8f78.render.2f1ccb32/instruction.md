# Bug Report

### Describe the bug

When using JSX with `jsx: 'preserve'` mode, the closing tags are being incorrectly transformed to `)` instead of being preserved as-is. This breaks the expected behavior where JSX syntax should remain unchanged when preserve mode is enabled.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.jsx',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  jsx: 'preserve'
}

// src/index.jsx
const element = <div>Hello World</div>;
```

Expected output with `jsx: 'preserve'`:
```jsx
const element = <div>Hello World</div>;
```

Actual output:
```js
const element = <div>Hello World)
```

### Expected behavior

When `jsx: 'preserve'` is set, JSX closing tags should remain as valid JSX syntax (e.g., `</div>`) and not be transformed into parentheses or other characters.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
