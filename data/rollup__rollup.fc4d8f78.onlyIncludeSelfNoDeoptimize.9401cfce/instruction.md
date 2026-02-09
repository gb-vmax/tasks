# Bug Report

### Describe the bug

I'm encountering an issue where certain nodes in the AST are not being marked as included during tree-shaking. This results in code that should be included in the bundle being incorrectly removed.

### Reproduction

```js
// Example code that gets incorrectly tree-shaken
import { sideEffect } from './module';

// This call should be preserved but gets removed
sideEffect();
```

When bundling the above code, the `sideEffect()` call is being eliminated even though it should be preserved in the output. This appears to affect specific node types that should always be included regardless of whether they're referenced elsewhere.

### Expected behavior

Nodes that are explicitly marked for inclusion should remain in the bundled output. The inclusion flag should be properly set to ensure these nodes survive the tree-shaking process.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
