# Bug Report

### Describe the bug

I'm experiencing an issue where member expressions used as assignment targets are not being properly analyzed for side effects. It seems like the tree-shaking logic is incorrectly removing assignments that should be kept because they have observable effects.

### Reproduction

```js
// This assignment gets incorrectly removed during tree-shaking
const obj = {};
obj.property = sideEffectFunction();

// Expected: sideEffectFunction() should be called
// Actual: The entire assignment is removed as if it has no effects
```

The problem appears when assigning to object properties where the right-hand side has side effects. The bundler is treating these assignments as if they can be safely removed, but they shouldn't be.

### Expected behavior

Assignments to member expressions should be preserved when:
1. The property access itself has side effects (e.g., getters)
2. The assigned value has side effects
3. The object being accessed has side effects

The current behavior seems to be inverting some of the logic around when to check for access effects, causing valid side-effectful code to be incorrectly eliminated.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
