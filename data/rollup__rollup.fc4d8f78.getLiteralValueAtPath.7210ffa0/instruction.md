# Bug Report

### Describe the bug

I'm experiencing an issue where `undefined` values are being treated as `null` in the bundled output. When accessing literal values for undefined variables, the system returns `null` instead of `undefined`, which breaks code that relies on strict equality checks or type checking.

### Reproduction

```js
// Source code
const value = undefined;

if (value === undefined) {
  console.log('This should execute');
}

if (value === null) {
  console.log('This should NOT execute');
}
```

After bundling, the behavior changes and the wrong branch executes. The undefined value is being transformed to null somewhere in the process.

### Expected behavior

`undefined` should remain as `undefined` throughout the bundling process. Code that checks for `undefined` using strict equality (`===`) should work correctly in the bundled output.

This is breaking our production code where we need to distinguish between `undefined` and `null` values.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
