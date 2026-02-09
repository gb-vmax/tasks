# Bug Report

### Describe the bug

When using the SystemJS output format with multiple exports, the first export is being excluded from the generated exports object. Only exports after the first one are included in the final output.

### Reproduction

```js
// Input module with multiple named exports
export const foo = 'value1';
export const bar = 'value2';
export const baz = 'value3';

// Expected SystemJS output should include all three exports:
// exports({
//   foo: value1,
//   bar: value2,
//   baz: value3
// });

// Actual output only includes bar and baz, foo is missing
```

### Expected behavior

All named exports should be included in the SystemJS exports object when there are multiple exports. The first export should not be omitted.

### System Info
- Rollup version: latest
- Output format: system

---
Repository: /testbed
