# Bug Report

### Describe the bug

When using `using` or `await using` declarations, the disposal side effects are not being tracked correctly. It seems like the tree-shaking logic is not properly detecting when these declarations should be included in the bundle.

### Reproduction

```js
// Case 1: Regular using declaration
using resource = getResource();
// Resource disposal is not included when it should be

// Case 2: Async using declaration  
await using asyncResource = getAsyncResource();
// Async disposal is not included when it should be
```

The issue appears when only one type of using declaration is present. The disposal paths (`Symbol.dispose` or `Symbol.asyncDispose`) are not being included properly during tree-shaking.

### Expected behavior

Both `using` and `await using` declarations should have their respective disposal side effects tracked and included in the output bundle independently. Each declaration type should trigger inclusion of its corresponding disposal symbol path regardless of whether the other type is present.

### System Info
- Rollup version: latest main branch
- Node.js version: 20.x

---
Repository: /testbed
