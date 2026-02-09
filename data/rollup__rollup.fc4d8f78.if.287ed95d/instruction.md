# Bug Report

### Describe the bug

When generating IIFE bundles with both `extend: true` and a named export, the output format is incorrect. The variable assignment seems to be inverted - it's using `var` when it should use `this` property access, and vice versa.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'iife',
    name: 'MyLibrary',
    extend: true,
    file: 'dist/bundle.js'
  }
}
```

With `extend: true`, the generated code uses `var MyLibrary = ...` instead of `this.MyLibrary = ...`, which means it doesn't properly extend the existing global object.

Similarly, when using named exports mode without extend, the behavior is also reversed.

### Expected behavior

When `extend: true` is set, the bundle should assign to `this.MyLibrary` to extend the global object. When using variable assignment mode without extend, it should use `var MyLibrary`.

The current output is generating the opposite of what's expected based on these configuration options.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
