# Bug Report

### Describe the bug

The z-index values returned by `getDefaultZIndex()` are off by 1 from what's expected. Components that rely on this utility function are rendering at incorrect stacking levels, causing overlapping issues with modals, popovers, and other overlay elements.

### Reproduction

```js
import { getDefaultZIndex } from '@mantine/core';

// Expected: 200, but getting 201
console.log(getDefaultZIndex('app'));

// Expected: 300, but getting 301
console.log(getDefaultZIndex('modal'));

// Expected: 400, but getting 401
console.log(getDefaultZIndex('popover'));
```

### Expected behavior

The function should return the exact z-index values defined in the elevations object without any modification. For example:
- `getDefaultZIndex('app')` should return `200`
- `getDefaultZIndex('modal')` should return `300`
- `getDefaultZIndex('popover')` should return `400`

Currently all values are incremented by 1, which breaks the expected stacking order.

### System Info
- @mantine/core version: latest
- Browser: N/A (affects all)

---
Repository: /testbed
