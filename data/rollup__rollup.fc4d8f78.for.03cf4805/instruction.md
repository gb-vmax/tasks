# Bug Report

### Describe the bug

When building with `preserveSignature: false` configured for entry modules, the exports are being incorrectly included during tree-shaking. It seems like the behavior is inverted - modules with `preserveSignature: false` are having their exports included when they shouldn't be, while modules without this setting (or with `preserveSignature: true`) are not including exports as expected.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es',
    preserveSignature: false
  },
  // ... other config
}
```

With the above configuration, the bundler includes all exports from the entry module even though `preserveSignature` is set to `false`. This results in larger bundle sizes than expected because unused exports are not being tree-shaken.

### Expected behavior

When `preserveSignature: false` is set, the entry module's exports should be tree-shaken normally. Only modules with `preserveSignature !== false` should have all their exports included.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
