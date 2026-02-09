# Bug Report

### Describe the bug

The `isLightColor` function is returning `false` for all CSS variable colors (e.g., `var(--my-color)`). It seems like the function immediately returns `false` when a color is passed as a CSS variable, which prevents proper luminance checking for theme colors.

### Reproduction

```js
import { isLightColor } from '@mantine/core';

// This always returns false, regardless of the actual color value
const result = isLightColor('var(--mantine-color-blue-5)');
console.log(result); // Expected: true or false based on luminance, Actual: false

// Regular color values work fine
const result2 = isLightColor('#ffffff');
console.log(result2); // Works correctly
```

### Expected behavior

When passing a CSS variable like `var(--mantine-color-blue-5)` to `isLightColor`, it should evaluate the luminance of that color and return `true` if the color is light (based on the threshold), or `false` if it's dark. Currently it just returns `false` for all CSS variables without checking their actual luminance.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
