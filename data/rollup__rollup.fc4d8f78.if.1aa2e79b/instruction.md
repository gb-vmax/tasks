# Bug Report

### Describe the bug

I'm experiencing an issue with dynamic imports where the resolution behavior seems inverted. When a dynamic import references the same chunk it's in, it's being treated as an external resolution instead of an internal one, and vice versa.

### Reproduction

```js
// In a module that gets bundled into the same chunk
export const value = 42;

// Dynamic import in the same chunk
const module = await import('./same-chunk-module.js');
console.log(module.value);
```

The dynamic import is being resolved incorrectly - it appears to be using the wrong resolution path based on whether the import target is in the same chunk or a different chunk.

### Expected behavior

When a dynamic import references a module in the same chunk, it should use internal resolution. When it references a module in a different chunk, it should use external resolution with the correct import path.

### Additional context

This seems to affect how the import paths are generated and could lead to runtime errors or incorrect module loading behavior. The issue appears to be related to how the chunk comparison is done when determining the resolution type.

---
Repository: /testbed
