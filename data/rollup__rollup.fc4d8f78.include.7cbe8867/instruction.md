# Bug Report

### Describe the bug

I'm experiencing an issue where modules are not being included correctly during tree-shaking. It seems like nodes that should be included based on `includeChildrenRecursively` are being skipped when they shouldn't be.

### Reproduction

```js
// main.js
import { foo } from './module.js';

// module.js
export function foo() {
  // This should be included
}

// When bundling with includeChildrenRecursively, 
// the function is not included in the output
```

The problem appears when:
1. A module has exports that should be included
2. The `shouldBeIncluded` check passes
3. But `includeChildrenRecursively` is true

In this case, the nodes are incorrectly filtered out and don't make it into the final bundle.

### Expected behavior

When `includeChildrenRecursively` is set, all nodes that pass the `shouldBeIncluded` check should be included in the bundle. The current behavior seems to use AND logic when it should use OR logic for determining inclusion.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
