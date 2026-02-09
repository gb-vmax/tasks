# Bug Report

### Describe the bug

When using the IIFE output format with named exports and the `extend` option enabled, the generated bundle is using incorrect variable assignment syntax. Instead of using `var` when `useVariableAssignment` is true, it's doing the opposite - using `var` when it's false and using `this` when it should use `var`.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'iife',
    name: 'MyLibrary',
    extend: true,
    exports: 'named'
  }
}
```

With a simple export:
```js
// src/index.js
export const foo = 'bar';
```

### Expected behavior

When `extend: true` and named exports are used, the wrapper should correctly choose between `var MyLibrary` or `this.MyLibrary` based on the `useVariableAssignment` configuration. Currently it's using the wrong one.

The generated output is malformed and causes runtime errors in certain environments.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
