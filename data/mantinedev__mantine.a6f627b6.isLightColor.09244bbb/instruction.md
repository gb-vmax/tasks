# Bug Report

### Describe the bug

The `isLightColor` function is returning incorrect results. When I pass in light colors, it returns `false`, and when I pass in dark colors, it returns `true`. The behavior seems completely inverted from what it should be.

### Reproduction

```js
import { isLightColor } from '@mantine/core';

// Light color (white) - should return true but returns false
console.log(isLightColor('#ffffff')); // Expected: true, Actual: false

// Dark color (black) - should return false but returns true  
console.log(isLightColor('#000000')); // Expected: false, Actual: true

// Light gray - should return true but returns false
console.log(isLightColor('#e0e0e0')); // Expected: true, Actual: false
```

Also noticed that when using CSS variables, the function always returns `true` now, which doesn't seem right either:

```js
console.log(isLightColor('var(--some-color)')); // Always returns true
```

### Expected behavior

`isLightColor` should return `true` for light colors (high luminance values) and `false` for dark colors (low luminance values). CSS variables should probably return a sensible default rather than always being treated as light.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
