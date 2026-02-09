# Bug Report

### Describe the bug

I'm experiencing an issue where property assignments on member expressions are not being properly deoptimized in certain cases. It seems like the tree-shaking behavior has changed and some side effects are not being tracked correctly.

### Reproduction

```js
// When assigning to a member expression where the variable is defined
// but isUndefined is also true, the deoptimization doesn't happen
const obj = {};
obj.property = someValue;

// The assignment should trigger deoptimization but it doesn't
// This affects tree-shaking and can cause incorrect code elimination
```

The issue appears when:
1. A member expression has a bound variable
2. The variable exists (`this.variable` is truthy)
3. `isUndefined` is also true
4. Property read side effects are enabled

In this scenario, the assignment deoptimization is not applied even though it should be.

### Expected behavior

Assignments to member expressions should consistently trigger deoptimization when appropriate, ensuring that side effects are properly tracked and tree-shaking doesn't incorrectly remove code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
