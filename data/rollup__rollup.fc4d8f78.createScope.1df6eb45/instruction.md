# Bug Report

### Describe the bug

I'm experiencing an issue with block scoping behavior that seems to be inverted. When a parent node has `preventChildBlockScope` set to true, a new BlockScope is being created instead of using the parent scope. Conversely, when `preventChildBlockScope` is false, the parent scope is being used directly instead of creating a new BlockScope.

This is causing scope resolution problems in my code - variables that should be accessible in a block scope are not found, and variables that should be isolated to a block are leaking to parent scopes.

### Reproduction

```js
// Case 1: When preventChildBlockScope is true
// Expected: Should use parent scope directly
// Actual: Creates a new BlockScope

function testPreventChildBlock() {
  const node = {
    preventChildBlockScope: true
  };
  
  // The block statement creates a new scope when it shouldn't
  // Variables defined in parent scope become inaccessible
}

// Case 2: When preventChildBlockScope is false
// Expected: Should create a new BlockScope
// Actual: Uses parent scope directly

function testNormalBlock() {
  const node = {
    preventChildBlockScope: false
  };
  
  // The block statement uses parent scope when it should create new one
  // Variables leak out of the block scope
}
```

### Expected behavior

- When `preventChildBlockScope` is `true`, the block should use the parent scope directly
- When `preventChildBlockScope` is `false` (or undefined), the block should create a new BlockScope

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
