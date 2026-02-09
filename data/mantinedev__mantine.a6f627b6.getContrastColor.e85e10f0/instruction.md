# Bug Report

### Describe the bug

The `getContrastColor` function is returning incorrect contrast colors. When `autoContrast` is enabled, it's always returning white instead of calculating the proper contrast color based on the background color's brightness. This makes text unreadable on light backgrounds.

### Reproduction

```js
import { getContrastColor } from '@mantine/core';

const theme = {
  autoContrast: true,
  primaryColor: 'blue'
};

// This returns white even though it should return black for light backgrounds
const contrastColor = getContrastColor({
  color: 'yellow.3', // light yellow background
  theme,
  autoContrast: true
});

console.log(contrastColor); // Expected: 'var(--mantine-color-black)', Got: 'var(--mantine-color-white)'
```

### Expected behavior

When `autoContrast` is enabled, the function should:
1. Parse the provided color
2. Determine if it's a light or dark color
3. Return black text for light backgrounds and white text for dark backgrounds

Currently it just returns white regardless of the background color when autoContrast is enabled, making text invisible on light backgrounds.

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
