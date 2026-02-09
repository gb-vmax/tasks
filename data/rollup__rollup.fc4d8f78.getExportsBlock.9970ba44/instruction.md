# Bug Report

### Describe the bug

When generating SystemJS output with multiple exports, the generated code is incorrect. The `exports` function is being called with an array instead of an object, which breaks the module loading.

### Reproduction

```js
// Input module with multiple exports
export const foo = 'foo';
export const bar = 'bar';

// Generated SystemJS output incorrectly uses array syntax:
// exports([
//   foo: 'foo',
//   bar: 'bar'
// ]);

// Should be using object syntax:
// exports({
//   foo: 'foo',
//   bar: 'bar'
// });
```

### Expected behavior

The `exports` function should be called with an object `{}` when there are multiple exports, not an array `[]`. The current output generates invalid JavaScript syntax that will fail at runtime.

### System Info
- Rollup version: latest
- Output format: system

---
Repository: /testbed
