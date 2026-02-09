# Bug Report

### Describe the bug

When passing an empty string `''` as a color prop to Mantine components, the function doesn't handle it correctly and returns the empty string instead of falling back to the theme's primary color. This causes components to render without any color applied.

### Reproduction

```js
import { getThemeColor } from '@mantine/core';

const theme = {
  primaryColor: 'blue',
  // ... other theme properties
};

// This should fall back to theme.primaryColor but returns empty string instead
const result = getThemeColor('', theme);
console.log(result); // Expected: CSS variable for blue, Actual: ''
```

Steps to reproduce:
1. Pass an empty string as the color value
2. The function treats empty string as truthy and doesn't fall back to `theme.primaryColor`
3. Component renders without color

### Expected behavior

Empty strings should be treated the same as `undefined` or `null` and fall back to the theme's primary color. The function should only use the provided color if it's a non-empty string.

### System Info
- @mantine/core version: latest
- Browser: Any

---
Repository: /testbed
