# Bug Report

### Describe the bug

I'm encountering an issue with interop helper generation where the variable names are being swapped in the generated code. When using imports that require interop helpers, the generated code has incorrect variable references - it's trying to use the helper variable name as the source and the dependency variable name as the target, which is backwards.

### Reproduction

```js
// When bundling a module with default imports that need interop
import defaultExport from 'some-module';

// The generated interop code ends up with swapped variable names
// Expected: const helperVar = /*#__PURE__*/interopHelper(dependency);
// Actual: const dependency = /*#__PURE__*/interopHelper(helperVar);
```

This results in undefined references since the variables are used in the wrong order.

### Expected behavior

The interop helper should be called with the dependency variable name as the argument, and the result should be assigned to the helper variable name. The generated code should have the correct variable assignment order.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
