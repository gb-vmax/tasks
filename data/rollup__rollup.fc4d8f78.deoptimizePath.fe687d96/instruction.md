# Bug Report

### Describe the bug

I'm experiencing an issue with parameter variable deoptimization that appears to be causing infinite recursion or stack overflow errors in certain edge cases. When deoptimizing paths on parameter variables, the code seems to get stuck in a loop under specific conditions involving nested property access.

### Reproduction

```js
function test(obj) {
  // Access nested properties that trigger deoptimization
  obj.a.b.c = value;
  obj.a.b.d = anotherValue;
  
  // This causes issues when the same path is deoptimized multiple times
  return obj.a.b;
}
```

The problem occurs when:
1. A parameter variable has nested property access
2. Multiple properties at the same level are being deoptimized
3. The deoptimization process triggers recursive calls

### Expected behavior

The deoptimization should complete without getting stuck in recursive loops. Each field should only be deoptimized once, and the tracking should prevent redundant operations.

### System Info

- Rollup version: latest main branch
- Node version: 18.x

This seems related to how the deoptimization tracking works with the `deoptimizedFields` set. The issue wasn't present in earlier versions, so something might have changed in how we handle the order of operations during path deoptimization.

---
Repository: /testbed
