# Bug Report

### Describe the bug

The `getThemeColor` function is returning incorrect values when CSS variables are used. Instead of returning the actual color value or CSS variable reference, it's returning the variable name itself without proper formatting.

### Reproduction

```js
import { getThemeColor } from '@mantine/core';

const theme = {
  primaryColor: 'blue',
  colors: {
    blue: ['#e7f5ff', '#d0ebff', '#a5d8ff', '#74c0fc', '#4dabf7', '#339af0', '#228be6', '#1c7ed6', '#1971c2', '#1864ab']
  }
};

// When using a color that should resolve to a CSS variable
const result = getThemeColor('blue', theme);
console.log(result); // Expected: 'var(--mantine-color-blue-filled)' or similar
// Actual: returns the variable name without var() wrapper or just the variable reference
```

### Expected behavior

The function should return either:
1. The CSS variable wrapped in `var()` syntax when a variable is available (e.g., `var(--mantine-color-blue-filled)`)
2. The original color value when no variable is available

Currently it seems to be returning just the variable reference itself, which won't work in CSS.

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
