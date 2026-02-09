# Bug Report

### Describe the bug

When using `getThemeColor()` function with theme colors, the returned value is incorrect. Instead of returning the CSS variable wrapped in `var()` or the actual color value, it's returning the raw variable name or a different property.

### Reproduction

```js
import { getThemeColor } from '@mantine/core';

const theme = {
  primaryColor: 'blue',
  colors: {
    blue: ['#e7f5ff', '#d0ebff', /* ... */]
  }
};

// Expected: 'var(--mantine-color-blue-filled)' or the actual color
// Actual: Returns something else
const color = getThemeColor('blue', theme);
console.log(color);
```

### Expected behavior

The function should return either:
- `var(--mantine-color-name)` when a CSS variable is available
- The actual color value when no variable exists

Currently it's not wrapping the variable in `var()` syntax which breaks CSS styling.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
