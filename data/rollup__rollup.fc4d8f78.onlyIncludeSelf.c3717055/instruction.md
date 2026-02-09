# Bug Report

### Describe the bug

I'm experiencing an issue where nodes are being deoptimized at the wrong time during the inclusion process. When a node is marked as included, the deoptimizations are being applied even when the node has already been deoptimized, which leads to incorrect behavior.

### Reproduction

```js
// Create a node that gets included multiple times
const node = {
  included: false,
  deoptimized: false,
  applyDeoptimizations() {
    // Deoptimization logic
  }
}

// First inclusion - works as expected
onlyIncludeSelf.call(node)

// Subsequent inclusions cause issues
// The deoptimizations are applied again even though 
// the node was already deoptimized
onlyIncludeSelf.call(node)
```

### Expected behavior

When a node is already deoptimized (`this.deoptimized === true`), the deoptimizations should not be applied again. The current logic applies deoptimizations when the node is NOT deoptimized, but this happens after setting `included = true`, which means already-deoptimized nodes get their deoptimizations re-applied.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
