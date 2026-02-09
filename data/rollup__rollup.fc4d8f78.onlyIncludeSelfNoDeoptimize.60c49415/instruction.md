# Bug Report

### Describe the bug

I'm experiencing an issue where nodes that should be excluded from the bundle are still being included. It seems like the inclusion logic isn't properly respecting when a node has been explicitly marked as excluded.

### Reproduction

When a node is explicitly set to `included = false` and then `onlyIncludeSelfNoDeoptimize` is called on it, the node gets incorrectly marked as included again, overriding the exclusion.

This happens in scenarios where:
1. A node is marked as not included (`included = false`)
2. Later in the bundling process, `onlyIncludeSelfNoDeoptimize` is invoked on that same node
3. The node becomes included even though it was previously excluded

### Expected behavior

Once a node is explicitly excluded (`included = false`), calling `onlyIncludeSelfNoDeoptimize` should not override that exclusion. The node should remain excluded from the bundle.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
