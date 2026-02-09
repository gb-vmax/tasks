# Bug Report

### Describe the bug

I'm experiencing an issue with global variable path resolution when accessing nested properties. It seems like the deoptimization logic isn't correctly handling paths for global variables, causing incorrect behavior when interacting with deeply nested global properties.

### Reproduction

```js
// When accessing a nested property on a global variable
global.someObject.property.nestedValue

// The path resolution appears to be incorrect, leading to
// unexpected deoptimization behavior
```

The issue manifests when:
1. Accessing properties on global variables with multiple levels of nesting
2. The code tries to determine if a global path exists
3. The slice operation on the path array doesn't include the correct elements

### Expected behavior

Global variable path resolution should correctly identify whether a given path exists in the global scope, including the variable name itself in the path check. The deoptimization should only occur when the path genuinely doesn't exist as a global.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to affect how global variables are tracked and optimized during the bundling process. The path slicing logic might be cutting off too many or too few elements from the path array.

---
Repository: /testbed
