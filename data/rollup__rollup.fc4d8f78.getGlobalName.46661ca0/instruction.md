# Bug Report

### Describe the bug

When building UMD bundles with the `globals` option, the global variable name is not being set correctly. Instead of using the provided global name or falling back to the chunk's variable name, it appears that `undefined` is being returned in cases where it should use the actual global name.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'umd',
    name: 'MyLibrary',
    globals: {
      'external-lib': 'ExternalLib'
    }
  },
  external: ['external-lib']
}
```

When building with this configuration, the generated UMD bundle doesn't properly reference `ExternalLib` as the global variable for `external-lib`. Instead, it seems to be using `undefined` or not resolving the global name correctly.

### Expected behavior

The UMD bundle should correctly map external dependencies to their global variable names as specified in the `globals` option. When a global name is provided, it should be used. When no global name is provided but the chunk has exports, it should fall back to the chunk's variable name with a warning.

### System Info

- Rollup version: latest
- Node version: 18.x

This is causing issues when trying to use the built library in a browser environment where external dependencies are loaded via script tags.

---
Repository: /testbed
