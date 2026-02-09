# Bug Report

### Describe the bug

When using `preserveModules` with external chunks, the dependency variable name deconfliction is not working correctly. The variable names are being assigned even when `preserveModules` is false, and when it is true, the deconfliction logic appears to be passing incorrect parameters.

### Reproduction

```js
// Configuration with preserveModules enabled
const config = {
  preserveModules: true,
  external: ['some-external-module']
}

// When bundling with external dependencies
// The generated variable names for external chunks may conflict
// or not be properly deconflicted
```

### Expected behavior

External chunk variable names should only be deconflicted when `preserveModules` is true AND the dependency is an ExternalChunk. The deconfliction should use the appropriate parameters to ensure unique variable names are generated.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
