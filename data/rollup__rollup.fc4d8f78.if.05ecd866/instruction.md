# Bug Report

### Describe the bug

I'm encountering an issue where `output.manualChunks` is being rejected even when `output.inlineDynamicImports` is enabled. The error message says that `manualChunks` is not supported with `inlineDynamicImports`, but this should only be the case when `inlineDynamicImports` is actually set to `true`.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    inlineDynamicImports: true,
    manualChunks: {
      vendor: ['lodash']
    }
  }
}
```

When running this configuration, I get an error stating that `manualChunks` is not supported with `inlineDynamicImports`. However, since I have `inlineDynamicImports: true`, I would expect `manualChunks` to be ignored or to work without throwing an error.

### Expected behavior

When `inlineDynamicImports` is set to `true`, the `manualChunks` option should either:
1. Be silently ignored (since dynamic imports are being inlined anyway), or
2. Work as expected without throwing an error

The validation should only trigger when `inlineDynamicImports` is `false` or not set, not when it's explicitly enabled.

### Additional context

This seems like the validation logic might be inverted - it's currently blocking the combination when `inlineDynamicImports` is enabled, but it should probably be checking the opposite condition.

---
Repository: /testbed
