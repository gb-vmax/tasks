# Bug Report

### Describe the bug

When using JSX with `jsx: 'preserve'` mode, the factory function is being incorrectly included in the output even though it shouldn't be transformed. The JSX elements should be left as-is in preserve mode, but it seems like the factory is still being processed.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.jsx',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  jsx: 'preserve'
}

// src/index.jsx
const Component = () => {
  return <div>Hello World</div>
}
```

### Expected behavior

In preserve mode, the JSX should remain untransformed in the output:
```js
const Component = () => {
  return <div>Hello World</div>
}
```

Instead, it appears the factory function is being included/processed when it shouldn't be.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
