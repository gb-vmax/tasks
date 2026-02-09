# Bug Report

### Describe the bug

When accessing properties on namespace imports, the member expression resolution is including the base namespace variable itself instead of just the nested path. This causes incorrect variable resolution for namespace member accesses.

### Reproduction

```js
// Given a namespace import
import * as utils from './utils';

// Accessing a member on the namespace
utils.helper();

// The path resolution incorrectly includes 'utils' in the slice
// instead of starting from the first member after the base
```

The issue occurs when resolving namespace variables - the path slicing is starting at index 0 instead of index 1, which means the base variable name is being included when it should only be processing the member access path.

### Expected behavior

When resolving namespace member accesses like `namespace.member.property`, the resolution should only process the member access chain (`member.property`) and not include the base namespace identifier (`namespace`) in the path.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing namespace member access tracking to fail since the full path including the base variable is being passed instead of just the nested member path.

---
Repository: /testbed
