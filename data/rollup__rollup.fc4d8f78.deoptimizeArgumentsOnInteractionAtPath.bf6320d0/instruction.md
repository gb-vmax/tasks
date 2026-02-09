# Bug Report

### Describe the bug

I'm experiencing an issue with global variable path resolution when accessing nested properties. It seems like the bundler is not correctly handling the full path to global variables, causing incorrect optimization behavior.

### Reproduction

```js
// When accessing nested properties on global objects
const obj = {
  foo: {
    bar: globalVar.nested.property
  }
};

// The bundler doesn't properly track the global variable path
// Expected: Should include 'globalVar' in the path resolution
// Actual: The variable name is being excluded from the path
```

This appears to affect how the bundler determines whether a property access should be optimized or deoptimized. The path resolution is missing the global variable's own name when checking if it exists at a certain path.

### Expected behavior

When resolving paths for global variables like `globalVar.nested.property`, the full path including the variable name itself should be used for lookups. Currently it seems like the variable name is being stripped from the path before checking if the global exists.

### Additional context

This is causing issues with tree-shaking and dead code elimination for global variable accesses. Properties that should be recognized as global built-ins are not being handled correctly.

---
Repository: /testbed
