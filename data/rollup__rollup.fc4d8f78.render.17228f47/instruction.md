# Bug Report

### Describe the bug

I'm experiencing incorrect JSX transformation behavior after a recent update. When using `jsx: 'classic'` mode, the output is not being transformed correctly - it seems like the code is falling through to the wrong transformation mode.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.jsx',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  plugins: [
    // ... other plugins
  ],
  jsx: 'classic'
}

// src/index.jsx
const App = () => {
  return <div>Hello World</div>
}
```

When bundling this, the JSX is being transformed using the wrong mode. Instead of getting the expected classic mode transformation, it appears to be using automatic mode transformation.

### Expected behavior

With `jsx: 'classic'` configured, JSX elements should be transformed using the classic `React.createElement` style transformation. The transformation mode should not fall through to other modes.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
