# Bug Report

### Describe the bug

When using JSX with `jsx: 'preserve'` mode, text nodes inside JSX elements are being incorrectly transformed. The text content gets wrapped in quotes and stringified even though preserve mode should keep the JSX syntax as-is.

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
const element = <div>Hello World</div>
```

### Expected behavior

With `jsx: 'preserve'` mode, the JSX text should remain unchanged in the output:
```js
const element = <div>Hello World</div>
```

### Actual behavior

The text gets stringified:
```js
const element = <div>"Hello World"</div>
```

This breaks the JSX syntax and causes issues when the output is processed by other tools expecting valid JSX.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
