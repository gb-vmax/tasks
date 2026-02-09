# Bug Report

### Describe the bug

I'm getting an error when trying to use `manualChunks` in my rollup configuration, even though I'm not using `preserveModules` at all. The error message says:

```
[!] RollupError: Invalid value "output.preserveModules" - this option is not supported for "output.preserveModules"
```

This doesn't make sense because I haven't enabled `preserveModules` in my config. The error appears as soon as I add any `manualChunks` configuration.

### Reproduction

```js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    format: 'es',
    manualChunks: {
      vendor: ['lodash', 'react']
    }
  }
}
```

### Expected behavior

The build should work normally when `manualChunks` is specified without `preserveModules`. These two options should be independent unless `preserveModules` is actually enabled.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
