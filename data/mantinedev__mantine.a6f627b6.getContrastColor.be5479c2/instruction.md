# Bug Report

### Describe the bug

The `getContrastColor` function is returning incorrect contrast colors. When `autoContrast` is disabled, it returns black instead of white, and when enabled, the light/dark logic appears to be inverted - light colors get white text and dark colors get black text, which results in poor contrast and unreadable text.

### Reproduction

```js
import { getContrastColor } from '@mantine/core';

const theme = {
  autoContrast: false,
  primaryColor: 'blue'
};

// With autoContrast disabled, this returns black instead of white
const color1 = getContrastColor({ 
  color: 'blue', 
  theme, 
  autoContrast: false 
});
console.log(color1); // Returns: var(--mantine-color-black)
// Expected: var(--mantine-color-white)

// With autoContrast enabled on a light color
const color2 = getContrastColor({ 
  color: 'yellow', // light color
  theme: { ...theme, autoContrast: true }, 
  autoContrast: true 
});
console.log(color2); // Returns: var(--mantine-color-white) 
// Expected: var(--mantine-color-black) for good contrast
```

### Expected behavior

- When `autoContrast` is `false`, the function should return white as the default contrast color
- When `autoContrast` is `true`, light colors should get black text and dark colors should get white text for proper contrast

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
