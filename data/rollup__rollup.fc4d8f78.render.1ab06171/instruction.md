# Bug Report

### Describe the bug

When using JSX with `jsx: 'preserve'` mode, the JSX text nodes are being incorrectly transformed/stringified. The text content should remain as-is when preserve mode is enabled, but instead it's being converted to JSON strings.

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
const Component = () => {
  return <div>Hello World</div>
}
```

### Expected behavior

With `jsx: 'preserve'` mode, the JSX should remain unchanged in the output:
```jsx
const Component = () => {
  return <div>Hello World</div>
}
```

### Actual behavior

The text content is being transformed even though preserve mode is set:
```js
const Component = () => {
  return <div>"Hello World"</div>
}
```

The text nodes shouldn't be processed at all when preserve mode is active. This is breaking our build pipeline where we need to preserve JSX for further processing by other tools.

---
Repository: /testbed
