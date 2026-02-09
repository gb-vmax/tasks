# Bug Report

### Describe the bug

When using `output.manualChunks` together with `output.preserveModules`, the validation logic seems to be inverted. The error is being thrown when `preserveModules` is `false` instead of when it's `true`, which is the opposite of what should happen.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    preserveModules: false,
    manualChunks: {
      vendor: ['lodash']
    }
  }
}
```

When running this configuration, I get an error saying:

```
Invalid option "output.preserveModules" - this option is not supported for "output.preserveModules"
```

This doesn't make sense because:
1. I'm NOT using `preserveModules` (it's set to `false`)
2. The error message itself is confusing - it mentions the same option twice
3. According to the docs, `manualChunks` should only be incompatible when `preserveModules` is `true`

### Expected behavior

The configuration should work fine when `preserveModules` is `false`. The error should only be thrown when both `preserveModules: true` AND `manualChunks` are specified together, since those options are mutually exclusive.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
