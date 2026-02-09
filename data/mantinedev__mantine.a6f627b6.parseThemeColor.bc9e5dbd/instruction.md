# Bug Report

### Describe the bug

The `parseThemeColor` function is not respecting the `colorScheme` parameter when resolving theme colors without an explicit shade. When I use a theme color in light mode, it's returning the dark mode color value instead.

### Reproduction

```tsx
import { parseThemeColor } from '@mantine/core';

const theme = {
  colors: {
    blue: ['#e7f5ff', '#d0ebff', '#a5d8ff', '#74c0fc', '#4dabf7', '#339af0', '#228be6', '#1c7ed6', '#1971c2', '#1864ab'],
  },
  primaryColor: 'blue',
  primaryShade: { light: 6, dark: 8 },
  colorScheme: 'light'
};

// This should use shade 6 (light mode primary shade) but uses shade 8 (dark mode)
const result = parseThemeColor({
  color: 'blue',
  theme,
  colorScheme: 'light'
});

console.log(result.color); // Expected: #228be6 (shade 6), Actual: #1971c2 (shade 8)
```

### Expected behavior

When `colorScheme` is set to `'light'`, the function should use the light mode primary shade to resolve the color value. Currently it seems to always use the dark mode shade regardless of what `colorScheme` is passed.

This also affects the dimmed color - in light mode it should use `gray[6]` but it's using `gray[7]` instead.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
