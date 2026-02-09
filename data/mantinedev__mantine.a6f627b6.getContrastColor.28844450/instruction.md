# Bug Report

### Describe the bug

The `getContrastColor` function is returning black text for both light and dark backgrounds, making text unreadable on dark backgrounds. It seems like the function always returns black regardless of the background color's luminance.

### Reproduction

```jsx
import { getContrastColor } from '@mantine/core';

const theme = {
  autoContrast: true,
  primaryColor: 'blue'
};

// Test with a dark color
const darkBg = getContrastColor({ 
  color: 'dark.9', 
  theme, 
  autoContrast: true 
});

console.log(darkBg); // Expected: white, Actual: black

// Test with a light color
const lightBg = getContrastColor({ 
  color: 'gray.1', 
  theme, 
  autoContrast: true 
});

console.log(lightBg); // Expected: black, Actual: black
```

### Expected behavior

When using `autoContrast`, the function should return:
- Black text (`var(--mantine-color-black)`) for light backgrounds
- White text (`var(--mantine-color-white)`) for dark backgrounds

Currently, it's returning black for both cases, which makes text invisible on dark backgrounds.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
