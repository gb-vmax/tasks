# Bug Report

### Describe the bug

The `isLightColor` function is returning incorrect results for CSS variable colors and edge case luminance values. When passing a color defined as a CSS variable (e.g., `var(--my-color)`), the function returns `true` instead of properly handling the variable. Additionally, colors with luminance exactly equal to the threshold are being treated inconsistently.

### Reproduction

```js
import { isLightColor } from '@mantine/core';

// Case 1: CSS variables return true instead of being handled properly
const result1 = isLightColor('var(--primary-color)');
console.log(result1); // Returns: true
// Expected: Should handle CSS variables differently or return false

// Case 2: Edge case with luminance exactly at threshold
const result2 = isLightColor('#some-color-with-luminance-0.179', 0.179);
// Inconsistent behavior when luminance equals threshold
```

### Expected behavior

1. CSS variable colors should be handled consistently (the previous behavior was returning `false`)
2. Colors with luminance exactly equal to the threshold should be treated consistently with the comparison logic

### System Info

- @mantine/core version: latest
- This affects theme color calculations and contrast determination

---
Repository: /testbed
