# Bug Report

### Describe the bug

When building with `preserveModules: false`, entry modules are not being included in the output. The bundler seems to be skipping entry modules unless `preserveModules` is explicitly set to `true`.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    format: 'esm'
  },
  preserveModules: false
}
```

With this configuration, the entry module is not included in the bundle output. The build completes without errors, but the entry point is missing from the generated files.

### Expected behavior

Entry modules should be included in the output regardless of the `preserveModules` setting. Setting `preserveModules: false` should only affect how non-entry modules are bundled, not whether entry modules are included.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
