# Bug Report

### Describe the bug

When loading a CommonJS config file that has a `default` export, the config is not being properly extracted. The default export seems to be ignored and the entire namespace object is returned instead.

### Reproduction

```js
// rollup.config.js (CommonJS format)
module.exports = {
  default: {
    input: 'src/index.js',
    output: {
      file: 'dist/bundle.js',
      format: 'es'
    }
  },
  someOtherProperty: 'value'
}
```

When loading this config, Rollup doesn't use the `default` export and instead tries to use the entire module object as the config.

### Expected behavior

When a CommonJS config file has a `default` property, that should be used as the actual config. The loader should properly extract `namespace.default` when it exists.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have broken recently - my configs with explicit `default` exports are no longer working as expected.

---
Repository: /testbed
