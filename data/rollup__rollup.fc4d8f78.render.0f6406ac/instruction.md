# Bug Report

### Describe the bug

When using JSX with `jsxMode` set to `'automatic'`, the rendering falls through to the default case and calls `super.render()` instead of properly handling the automatic mode. This causes JSX elements to be rendered incorrectly when using automatic JSX runtime.

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
    mode: 'automatic',
    importSource: 'react'
  }
}

// src/index.jsx
function App() {
  return <div>Hello World</div>;
}
```

When bundling with the automatic JSX mode, the JSX element gets processed by both `renderAutomaticMode()` and the default `super.render()`, resulting in incorrect output.

### Expected behavior

JSX elements should be transformed correctly using only the automatic mode transformation when `jsxMode.mode` is set to `'automatic'`. The switch statement should not fall through to the default case after handling automatic mode.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
