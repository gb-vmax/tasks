# Bug Report

### Describe the bug

I'm experiencing an issue where nodes are being marked as included before deoptimizations are applied. This causes the deoptimization logic to be skipped in certain cases, leading to incorrect tree-shaking behavior.

### Reproduction

```js
// When a node is included via onlyIncludeSelf
// The included flag is set before applyDeoptimizations runs
// This means the deoptimization check fails and optimizations aren't applied

const node = {
  included: false,
  deoptimized: false,
  applyDeoptimizations() {
    // This should run before marking as included
  }
};

// Current behavior:
// 1. node.included = true (set first)
// 2. Check if (!node.deoptimized) - fails because deoptimized is still false
// 3. Deoptimizations never applied properly
```

### Expected behavior

The node should be deoptimized before being marked as included. The deoptimization flag should be set first, then deoptimizations applied, and only after that should the node be marked as included.

This is causing issues with code that relies on proper deoptimization ordering during the inclusion phase.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
