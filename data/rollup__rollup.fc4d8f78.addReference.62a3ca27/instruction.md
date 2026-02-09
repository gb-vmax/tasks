# Bug Report

### Describe the bug

I'm experiencing an issue with namespace imports where only the last reference to a namespace is being tracked. When a namespace is referenced multiple times in the code, all previous references seem to be lost and only the most recent one is retained.

### Reproduction

```js
import * as utils from './utils';

// First reference
const result1 = utils.helper();

// Second reference
const result2 = utils.formatter();

// Only the second reference appears to be tracked
// The first reference is lost
```

### Expected behavior

All references to a namespace import should be tracked and maintained. Each time the namespace is referenced in the code, it should be added to the list of references rather than replacing the existing ones.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have started recently, possibly after a recent update. It's causing issues with tree-shaking and bundle analysis since not all namespace usages are being properly tracked.

---
Repository: /testbed
