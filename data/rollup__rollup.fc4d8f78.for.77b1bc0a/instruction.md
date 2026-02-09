# Bug Report

### Describe the bug

I'm encountering an issue with entry module exports when `preserveSignature` is set to `false`. It seems like the exports are being included when they shouldn't be, or vice versa - the behavior appears inverted from what I would expect.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es',
    preserveModules: true
  },
  preserveEntrySignatures: false
}
```

When I build with `preserveSignature: false` on entry modules, the treeshaking behavior seems backwards. Exports that should be included are being excluded, and the build output doesn't match what I'd expect.

### Expected behavior

When `preserveSignature` is set to `false`, the module's exports should be handled appropriately during the treeshaking pass. Currently it seems like the condition is inverted - modules with `preserveSignature: false` are being treated as if they had `preserveSignature: true` and vice versa.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

This might be related to the treeshaking pass logic for entry modules. The behavior changed recently and I'm not sure if this is intentional or a regression.

---
Repository: /testbed
