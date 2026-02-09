# Bug Report

### Describe the bug

When building with `preserveSignature: false` on entry modules, the exports are being incorrectly included during the treeshaking pass. This causes unexpected behavior where modules that should not have all their exports included are getting them included anyway.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es',
    preserveEntrySignatures: false
  }
}
```

When running a build with the above configuration, entry modules with `preserveSignature: false` are having their exports included when they shouldn't be.

### Expected behavior

Entry modules with `preserveSignature` set to `false` should NOT have all their exports included during the first treeshaking pass. Only modules where `preserveSignature !== false` should include all exports.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to be affecting the treeshaking logic and causing unnecessary code to be included in the final bundle.

---
Repository: /testbed
