# Bug Report

### Describe the bug

I'm experiencing an issue with argument deoptimization in functions. When a function's `arguments` object is referenced and then included in the dependency path, the first argument doesn't get properly deoptimized while subsequent arguments do.

### Reproduction

```js
function test() {
  // Reference arguments to trigger deoptimization tracking
  var args = arguments;
  
  // First argument should be deoptimized but isn't
  return arguments[0];
}

test(someComplexObject, anotherObject);
```

The problem appears when:
1. A function references the `arguments` object
2. The arguments variable gets added to the inclusion path
3. Only arguments starting from index 1 are deoptimized, skipping the first argument at index 0

### Expected behavior

All arguments (starting from index 0) should be deoptimized when the `arguments` object is referenced and included in the path. The first argument should not be treated differently from the rest.

### Additional context

This seems to affect tree-shaking and optimization behavior where the first function argument might not be properly tracked for side effects or deoptimization, potentially leading to incorrect code elimination or transformation.

---
Repository: /testbed
