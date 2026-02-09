# Bug Report

### Describe the bug

I'm encountering an issue with function deoptimization when accessing nested properties. It seems like the deoptimization logic isn't being triggered correctly for certain path configurations.

### Reproduction

```js
const myFunction = () => {
  return { nested: { value: 42 } };
};

// Accessing properties through unknown keys
const result = myFunction()[unknownKey];
```

When the path has a single unknown key element, the function's return expression and parameters should be deoptimized, but this doesn't seem to be happening. The deoptimization is only triggered for paths with length greater than 1, which means single-element unknown key paths are being skipped.

### Expected behavior

When a path contains an unknown key at the first position (regardless of path length), the function scope should deoptimize the return expression and all parameters to ensure correctness in tree-shaking and side-effect detection.

### Additional context

This affects how rollup handles function calls where the return value is accessed with dynamic property access. The optimization assumptions might be too aggressive in these cases, potentially leading to incorrect code elimination.

---
Repository: /testbed
