# Bug Report

### Describe the bug

I'm experiencing an issue where entry modules are not being included correctly in the bundle output. It seems like modules that should be treated as entry points are being filtered out unexpectedly.

### Reproduction

```js
// rollup.config.js
export default {
  input: '/absolute/path/to/entry.js',
  output: {
    dir: 'dist',
    format: 'es'
  }
}
```

When bundling with an absolute path as the entry point, the module doesn't appear to be processed as an entry module. This also affects builds using `preserveModules: true` where entry modules with absolute paths seem to be excluded from the output.

### Expected behavior

Entry modules should be correctly identified and included in the bundle regardless of whether their paths are absolute or relative. When `preserveModules` is enabled, all entry modules should be preserved in the output.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
