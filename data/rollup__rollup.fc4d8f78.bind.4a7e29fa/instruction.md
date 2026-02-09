# Bug Report

### Describe the bug

When accessing nested namespace members, the resolution is failing and treating the entire path as if it needs to be resolved instead of just the member portion. This causes namespace member lookups to fail incorrectly.

### Reproduction

```js
// Given a namespace import
import * as utils from './utils';

// Accessing a nested member
utils.helpers.formatDate()
```

The member expression resolution is not working correctly - it's trying to resolve the entire path including the base namespace variable instead of just the member access portion.

### Expected behavior

The namespace member should be resolved correctly by only processing the member path (everything after the base namespace variable), not including the base variable itself in the resolution.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently, possibly after some refactoring of the member expression binding logic. The namespace resolution is getting the wrong slice of the path.

---
Repository: /testbed
