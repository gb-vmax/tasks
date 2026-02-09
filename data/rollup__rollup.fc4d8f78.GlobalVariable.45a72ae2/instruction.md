# Bug Report

### Describe the bug

I'm experiencing an issue with global variable path resolution in nested property access scenarios. When accessing deeply nested properties on global objects, the path slicing logic appears to be incorrect, causing the wrong path segments to be checked.

### Reproduction

```js
// Accessing a nested property on a global object
const result = globalObject.property.nested.value;

// The path checking logic seems to be off by one
// Expected: Check if globalObject.property.nested exists
// Actual: Appears to skip or incorrectly slice path segments
```

This affects both property access and assignment operations on global variables with nested paths.

### Expected behavior

When checking if a global variable path exists (e.g., `globalObject.property.nested`), the system should correctly validate the entire path up to the accessed property. The path slicing should include all necessary segments to properly determine if the global exists at that path.

### Additional context

This seems related to how path arrays are being sliced when validating global variable access. The logic for determining whether to deoptimize arguments or mark side effects depends on correctly identifying whether a global exists at a given path, but the current slicing appears to be checking the wrong segments.

---
Repository: /testbed
