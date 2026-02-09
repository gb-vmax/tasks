# Bug Report

### Describe the bug

The `luminance()` function is returning incorrect values for color calculations. When using this function to determine if a color is light or dark (which affects text contrast decisions), the results are wrong and causing accessibility issues in my application.

### Reproduction

```js
import { luminance, isLightColor } from '@mantine/core';

// Testing with a known color
const blueColor = 'rgb(0, 100, 200)';
const luminanceValue = luminance(blueColor);

console.log('Luminance:', luminanceValue);
// Expected: ~0.15 (based on standard luminance calculation)
// Actual: Getting unexpected value

// This also affects isLightColor
const isLight = isLightColor(blueColor);
console.log('Is light color:', isLight);
// The classification is incorrect
```

I'm also seeing issues with OKLCH colors:

```js
const oklchColor = 'oklch(50% 0.1 180)';
const oklchLuminance = luminance(oklchColor);

console.log('OKLCH Luminance:', oklchLuminance);
// Expected: 0.5 (50% lightness)
// Actual: Getting 5.0 which doesn't make sense
```

### Expected behavior

The luminance function should return values between 0 and 1 following the standard relative luminance calculation (as defined in WCAG guidelines). This is critical for determining proper text contrast ratios.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

This is affecting my entire theme system since many components rely on this function to determine text colors. Any help would be appreciated!

---
Repository: /testbed
