# Bug Report

### Describe the bug

When using invalid annotations (like `@__PURE__` or `@__NO_SIDE_EFFECTS__`) in my code, the first invalid annotation is being silently ignored and not removed from the output bundle. Only subsequent invalid annotations are properly handled and removed.

### Reproduction

```js
// Input code with multiple invalid annotations
/*@__PURE__*/ const a = 1;
/*@__PURE__*/ const b = 2;
/*@__PURE__*/ const c = 3;
```

After bundling, the first annotation `/*@__PURE__*/` before `const a = 1;` remains in the output, while the others are correctly removed. Additionally, no warning is logged for the first invalid annotation.

### Expected behavior

All invalid annotations should be:
1. Removed from the output bundle
2. Generate a warning in the build logs

Currently only annotations after the first one are being processed correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to affect both `@__PURE__` and `@__NO_SIDE_EFFECTS__` annotations when they appear at the top level of a program.

---
Repository: /testbed
