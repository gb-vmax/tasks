# Bug Report

### Describe the bug

I'm experiencing an issue with the `nodeTypes` export from `@mdx-js/mdx`. When accessing `nodeTypes`, it appears to be returning a modified copy instead of the original reference. This breaks code that relies on checking object identity or mutating the nodeTypes object.

### Reproduction

```js
import { nodeTypes } from '@mdx-js/mdx';

// Store a reference
const originalNodeTypes = nodeTypes;

// Access it again
const nodeTypesAgain = nodeTypes;

// These should be the same reference but they're not
console.log(originalNodeTypes === nodeTypesAgain); // Expected: true, Actual: false
```

### Expected behavior

The `nodeTypes` export should return the same object reference each time it's accessed, not a new copy. This is breaking compatibility with code that expects consistent object identity.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: latest

---
Repository: /testbed
