# Bug Report

### Describe the bug

When using `virtualColor()` to create virtual color tuples, the resulting array only contains 9 color shades instead of the expected 10. This causes issues when trying to access the 10th shade (index 9) of a virtual color, which should map to `var(--mantine-color-{name}-9)`.

### Reproduction

```js
import { virtualColor } from '@mantine/core';

const myVirtualColor = virtualColor({
  name: 'primary',
  dark: 'blue',
  light: 'cyan'
});

console.log(myVirtualColor.length); // Expected: 10, Actual: 9
console.log(myVirtualColor[9]); // Expected: 'var(--mantine-color-primary-9)', Actual: undefined
```

### Expected behavior

The virtual color tuple should contain 10 shades (indices 0-9) to match the standard Mantine color palette structure. All color shades from 0 to 9 should be accessible and map to their corresponding CSS variables.

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
