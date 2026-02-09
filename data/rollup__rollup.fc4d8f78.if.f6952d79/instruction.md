# Bug Report

### Describe the bug

When using `output.file` with `output.preserveModules` set to `true`, rollup should throw an error telling me to use `output.dir` instead. However, the validation seems to be inverted - it's throwing the error when `preserveModules` is `false` instead of when it's `true`.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm',
    preserveModules: true  // This should trigger an error but doesn't
  }
}
```

Expected: Should error saying to use `output.dir` instead of `output.file`
Actual: Build proceeds without error

But if I set `preserveModules: false`:

```js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm',
    preserveModules: false  // This should NOT error
  }
}
```

Now it incorrectly throws: "you must set "output.dir" instead of "output.file" when using the "output.preserveModules" option"

### Expected behavior

The error should only be thrown when `preserveModules` is `true`, not when it's `false`. The validation logic appears to be backwards.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
