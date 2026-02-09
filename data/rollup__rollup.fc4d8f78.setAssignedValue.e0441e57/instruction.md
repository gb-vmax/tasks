# Bug Report

### Describe the bug

I'm experiencing an issue with member expression assignments where the order of arguments seems to be incorrect. When assigning a value to an object property, the assignment interaction is not being tracked properly, which causes incorrect behavior in the deoptimization logic.

### Reproduction

```js
const obj = { prop: 1 };
obj.prop = 42;
// The assignment should track the value being assigned and the object correctly
// But the order appears to be swapped internally
```

This affects how the bundler handles property assignments during tree-shaking and optimization passes. The interaction tracking seems to have the arguments in the wrong order.

### Expected behavior

When assigning to a member expression like `obj.prop = value`, the assignment interaction should correctly track the relationship between the value being assigned and the object receiving it. The current behavior causes issues with side effect detection and optimization.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
