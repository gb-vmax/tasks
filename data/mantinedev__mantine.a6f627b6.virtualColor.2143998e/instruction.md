# Bug Report

### Describe the bug

When using `virtualColor()` to create virtual color tuples, the generated array only contains 9 color shades instead of the expected 10. This causes issues when trying to access the 10th shade (index 9) of a virtual color, as it returns `undefined` instead of the expected CSS variable reference.

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

Virtual colors should generate a complete color tuple with 10 shades (indices 0-9), matching the standard Mantine color format. All 10 shades should be accessible and reference the correct CSS variables.

### Additional context

This breaks compatibility with existing code that expects virtual colors to have the same structure as regular color tuples. Components that reference higher shade indices (like 8 or 9) will fail to apply the correct colors.

---
Repository: /testbed
