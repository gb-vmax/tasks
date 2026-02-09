# Bug Report

### Describe the bug

I'm experiencing an issue with virtual colors where only 9 color shades are being generated instead of the expected 10. When using `virtualColor()` to create a color tuple, the resulting array is missing the last shade (index 9).

### Reproduction

```js
import { virtualColor } from '@mantine/core';

const customColor = virtualColor({ name: 'custom' });

console.log(customColor.length); // Expected: 10, Actual: 9
console.log(customColor[9]); // Expected: 'var(--mantine-color-custom-9)', Actual: undefined
```

### Expected behavior

The `virtualColor()` function should generate a complete color tuple with all 10 shades (indices 0-9), matching the standard Mantine color format. All CSS variable references from `--mantine-color-{name}-0` through `--mantine-color-{name}-9` should be included.

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
