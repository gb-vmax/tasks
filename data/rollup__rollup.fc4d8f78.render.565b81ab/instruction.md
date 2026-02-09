# Bug Report

### Describe the bug

I'm experiencing an issue with JSX rendering in classic mode where it seems like the code is being executed twice or falling through to automatic mode. When I use JSX with `jsx: 'classic'` configuration, the output appears to include both classic mode transformations AND automatic mode transformations, which is causing duplicate or incorrect code generation.

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
function App() {
  return <div>Hello World</div>;
}
```

### Expected behavior

When using classic JSX mode, the output should only contain classic mode transformations (e.g., `React.createElement` calls). The automatic mode transformations should not be applied.

### Current behavior

The generated code appears to include transformations from both classic and automatic modes, suggesting that when classic mode is selected, it's not properly breaking out of the switch statement and continues to execute the automatic mode logic as well.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
