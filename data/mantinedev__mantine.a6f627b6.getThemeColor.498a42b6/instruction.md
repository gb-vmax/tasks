# Bug Report

### Describe the bug

The `getThemeColor` function is returning incorrect values when working with theme colors. When a color is passed that doesn't have a CSS variable defined, the function returns `undefined` instead of the actual color value.

### Reproduction

```js
import { getThemeColor } from '@mantine/core';

const theme = {
  primaryColor: 'blue',
  colors: {
    blue: ['#e7f5ff', '#d0ebff', '#a5d8ff', '#74c0fc', '#4dabf7', '#339af0', '#228be6', '#1c7ed6', '#1971c2', '#1864ab']
  }
};

// This returns undefined instead of the actual color
const color = getThemeColor('#ff0000', theme);
console.log(color); // Expected: '#ff0000', Actual: undefined
```

### Expected behavior

When a color string is provided (like a hex color or any valid CSS color), the function should return that color value if it doesn't have a corresponding CSS variable. Currently it's returning `undefined` for colors without variables.

### System Info
- @mantine/core version: latest
- Browser: Any

---
Repository: /testbed
