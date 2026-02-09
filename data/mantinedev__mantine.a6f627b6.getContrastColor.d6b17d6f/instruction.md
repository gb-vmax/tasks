# Bug Report

### Describe the bug

The `getContrastColor` function is returning inverted contrast colors. When `autoContrast` is enabled, it always returns white regardless of the background color. Additionally, when `autoContrast` is disabled or when it falls through to the light/dark check, light backgrounds get white text and dark backgrounds get black text, which is the opposite of what should happen for proper contrast.

### Reproduction

```tsx
import { getContrastColor } from '@mantine/core';

const theme = {
  autoContrast: true,
  primaryColor: 'blue',
  // ... other theme properties
};

// Case 1: autoContrast enabled
const result1 = getContrastColor({ 
  color: 'blue.6', 
  theme, 
  autoContrast: true 
});
// Returns white, but should return the appropriate contrast color based on luminance

// Case 2: Light background color
const result2 = getContrastColor({ 
  color: '#ffffff', 
  theme: { ...theme, autoContrast: false }, 
  autoContrast: false 
});
// Returns white text on white background (no contrast)

// Case 3: Dark background color  
const result3 = getContrastColor({ 
  color: '#000000', 
  theme: { ...theme, autoContrast: false }, 
  autoContrast: false 
});
// Returns black text on black background (no contrast)
```

### Expected behavior

- When `autoContrast` is **disabled**, the function should return white (the default contrast color)
- When `autoContrast` is **enabled**, it should calculate the appropriate contrast:
  - Light backgrounds should get **black** text for readability
  - Dark backgrounds should get **white** text for readability

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
