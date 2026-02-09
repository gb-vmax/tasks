# Bug Report

### Describe the bug

When building with the `output.globals` option, the global variable name is not being set correctly for chunks. The build completes but the generated bundle doesn't properly assign the module to the expected global variable name.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'iife',
    name: 'MyLibrary',
    globals: {
      'my-module': 'MyModule'
    }
  },
  external: ['my-module']
}
```

When building with this config, the global name mapping doesn't work as expected. The module should be accessible via `window.MyModule` but it's undefined.

### Expected behavior

The chunk should be assigned to the global variable name specified in the `globals` option. If a global name is provided via the `globals` option (either as an object or function), that name should be used in the generated output.

### Additional context

This seems to affect builds where external dependencies need to be mapped to global variables, which is common when creating UMD/IIFE bundles that depend on libraries loaded via CDN.

---
Repository: /testbed
