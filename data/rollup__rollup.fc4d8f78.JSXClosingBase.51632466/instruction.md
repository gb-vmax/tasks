# Bug Report

### Describe the bug

I'm encountering an issue with JSX rendering when using `jsx: { mode: 'preserve' }` in the configuration. The closing JSX tags are not being rendered correctly - it seems like the last character of the closing tag is being removed/replaced incorrectly.

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
  return <div>Hello World</div>
}
```

When bundling with `mode: 'preserve'`, the closing tag gets mangled. The output should preserve the JSX syntax as-is, but instead the closing tags are being modified.

### Expected behavior

With `mode: 'preserve'`, the JSX syntax should remain unchanged in the output. The closing tags like `</div>` should be preserved exactly as written in the source code.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
