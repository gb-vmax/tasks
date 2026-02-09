# Bug Report

### Describe the bug

When calling `getThemeColor()` without passing a color argument (or passing `undefined`/`null`), the function returns the wrong value. Instead of returning the theme's primary color, it seems to be returning something unexpected.

### Reproduction

```js
import { getThemeColor } from '@mantine/core';

const theme = {
  primaryColor: 'blue',
  // ... other theme properties
};

// This should return the primary color but doesn't work correctly
const color1 = getThemeColor(undefined, theme);
console.log(color1); // Expected: primary color value, Actual: undefined

const color2 = getThemeColor(null, theme);
console.log(color2); // Expected: primary color value, Actual: null
```

### Expected behavior

When no color is provided (undefined or null), `getThemeColor()` should fall back to using `theme.primaryColor` and return the appropriate color value or CSS variable.

### System Info
- @mantine/core version: latest
- Framework: React 18

---
Repository: /testbed
