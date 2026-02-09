# Bug Report

### Describe the bug

The `getPrimaryContrastColor` function is not working correctly - it seems to be looking up colors using `theme.primaryShade` instead of `theme.primaryColor`. This causes the function to fail or return incorrect contrast colors.

### Reproduction

```js
const theme = {
  primaryColor: 'blue',
  primaryShade: 6,
  colors: {
    blue: ['#e7f5ff', '#d0ebff', '#a5d8ff', '#74c0fc', '#4dabf7', '#339af0', '#228be6', '#1c7ed6', '#1971c2', '#1864ab'],
  },
  // ... other theme properties
};

// Try to get primary contrast color
const contrastColor = getPrimaryContrastColor(theme, 'light');
// This will fail because it tries to access theme.colors[6] instead of theme.colors['blue']
```

### Expected behavior

The function should use `theme.primaryColor` to look up the correct color array from `theme.colors`, not `theme.primaryShade` which is just a number index.

### System Info
- @mantine/core version: latest
- Browser: any

---
Repository: /testbed
