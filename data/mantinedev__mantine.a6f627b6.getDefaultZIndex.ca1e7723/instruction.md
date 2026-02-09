# Bug Report

### Describe the bug

The `getDefaultZIndex` function is returning `undefined` for all valid elevation levels instead of returning the correct z-index values. This breaks any component that relies on default z-index values like modals, popovers, and tooltips.

### Reproduction

```js
import { getDefaultZIndex } from '@mantine/core';

// These should return numeric values but return undefined instead
console.log(getDefaultZIndex('app')); // Expected: 100, Actual: undefined
console.log(getDefaultZIndex('modal')); // Expected: 200, Actual: undefined
console.log(getDefaultZIndex('popover')); // Expected: 300, Actual: undefined
console.log(getDefaultZIndex('overlay')); // Expected: 400, Actual: undefined
console.log(getDefaultZIndex('max')); // Expected: 9999, Actual: undefined
```

### Expected behavior

The function should return the corresponding z-index value for each valid elevation level:
- `app` → 100
- `modal` → 200
- `popover` → 300
- `overlay` → 400
- `max` → 9999

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

This seems to have broken after a recent update. All overlays and modals are now rendering at the default browser z-index instead of the proper stacking order.

---
Repository: /testbed
