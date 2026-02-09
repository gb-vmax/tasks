# Bug Report

### Describe the bug

When setting `output.file` in the configuration, I'm getting an error message that doesn't match the actual problem. The error says I need to set `output.dir` instead of `output.file` when using `preserveModules`, but I'm not even using `preserveModules` in my config.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
    // Note: preserveModules is NOT set
  }
}
```

When running this config, I get an error telling me:
```
you must set "output.dir" instead of "output.file" when using the "output.preserveModules" option
```

But I'm not using `preserveModules` at all! The error message is confusing and seems backwards.

### Expected behavior

The build should work fine when using `output.file` without `preserveModules`, or if there's an actual validation issue, the error message should accurately describe what's wrong.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
