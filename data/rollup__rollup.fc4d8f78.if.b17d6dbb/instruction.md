# Bug Report

### Describe the bug

When using the IIFE output format with `extend: true` and a named export, the bundle is incorrectly assigned to a `var` instead of extending the global object. This breaks the intended behavior where the module should extend an existing global object.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'iife',
    name: 'MyLib',
    extend: true
  }
}
```

With `extend: true`, the generated IIFE should assign to `this.MyLib` to extend the existing global, but instead it's being assigned to `var MyLib`.

### Expected behavior

When `extend` is set to `true`, the output should always use `this.MyLib = ...` instead of `var MyLib = ...` to properly extend the global object. The current behavior seems to ignore the `extend` option in certain cases.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
