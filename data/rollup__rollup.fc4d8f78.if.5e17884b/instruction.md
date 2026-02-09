# Bug Report

### Describe the bug

I'm encountering an issue where `output.manualChunks` is being incorrectly rejected when used with `output.inlineDynamicImports: false`. The error message says that `manualChunks` is not supported for `inlineDynamicImports`, but this should only be the case when `inlineDynamicImports` is set to `true`.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    inlineDynamicImports: false,
    manualChunks: {
      vendor: ['lodash']
    }
  }
}
```

When running the build with this configuration, I get an error saying:
```
Invalid value for option "output.manualChunks" - this option is not supported for "output.inlineDynamicImports"
```

### Expected behavior

The build should succeed without errors. `manualChunks` should only be incompatible with `inlineDynamicImports: true`, not when it's set to `false`. When `inlineDynamicImports` is disabled (false), manual chunks should work normally.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like the validation logic might be inverted? It was working fine in previous versions.

---
Repository: /testbed
