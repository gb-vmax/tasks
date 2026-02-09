# Bug Report

### Describe the bug

I'm experiencing an issue where nodes that haven't been included yet are not getting marked as included when they should be. This seems to be affecting the tree-shaking behavior where certain code that should be included in the bundle is being incorrectly excluded.

### Reproduction

```js
// Create a module with code that should be included
const module = {
  included: false,
  // ... other properties
}

// Call the inclusion logic
onlyIncludeSelfNoDeoptimize.call(module)

// Expected: module.included should be true
// Actual: module.included is still false
```

The issue appears when processing nodes that start with `included: false`. The inclusion logic seems to only work for nodes that are already marked as included, which doesn't make sense for the initial inclusion pass.

### Expected behavior

When a node is being included, it should be marked as `included: true` regardless of its previous state. The function should set the property unconditionally to ensure nodes are properly tracked as included in the bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
