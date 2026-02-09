# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking behavior when `moduleSideEffects` is set to `'no-treeshake'`. It seems like the logic is inverted - modules that should be fully included are being selectively tree-shaken, and modules that should be tree-shaken are being fully included.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  treeshake: {
    moduleSideEffects: 'no-treeshake'
  }
}
```

When I build with this configuration, modules marked with `moduleSideEffects: 'no-treeshake'` are having their unused exports removed, but they should be included entirely in the bundle. Conversely, modules without this flag are being fully included when they should be tree-shaken.

### Expected behavior

When `moduleSideEffects` is set to `'no-treeshake'`, the entire module should be included in the bundle without any tree-shaking. Other modules should undergo normal tree-shaking to remove unused code.

The current behavior seems backwards from what's documented.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
