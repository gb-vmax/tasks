# Bug Report

### Describe the bug

The `getPrimaryShade` function is returning incorrect shade values based on the color scheme. When using dark mode, it returns the light shade value and vice versa. Additionally, when `primaryShade` is configured as a number, it's not being returned correctly.

### Reproduction

```js
import { getPrimaryShade } from '@mantine/core';

const theme = {
  primaryShade: { light: 6, dark: 8 }
};

// In dark mode, this returns 6 (light shade) instead of 8
const darkShade = getPrimaryShade(theme, 'dark');
console.log(darkShade); // Expected: 8, Actual: 6

// In light mode, this returns 8 (dark shade) instead of 6
const lightShade = getPrimaryShade(theme, 'light');
console.log(lightShade); // Expected: 6, Actual: 8

// When using a number, it doesn't return the value at all
const themeWithNumber = {
  primaryShade: 5
};
const shade = getPrimaryShade(themeWithNumber, 'light');
console.log(shade); // Expected: 5, Actual: undefined or wrong value
```

### Expected behavior

- When `colorScheme` is `'dark'`, it should return `theme.primaryShade.dark`
- When `colorScheme` is `'light'`, it should return `theme.primaryShade.light`
- When `theme.primaryShade` is a number, it should return that number directly

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
