# Bug Report

### Describe the bug

I'm experiencing incorrect color conversions when using HSL color strings with the Mantine color functions. The RGB values returned from HSL inputs are completely wrong, making colors appear drastically different than expected.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// Convert HSL to RGBA
const result = toRgba('hsl(120, 50%, 50%)');
console.log(result);
// Output shows incorrect RGB values

// Another example with different hue
const result2 = toRgba('hsl(180, 100%, 50%)');
console.log(result2);
// Also produces wrong colors
```

### Expected behavior

The HSL to RGB conversion should produce accurate RGB values. For example:
- `hsl(120, 50%, 50%)` should convert to a proper green color
- `hsl(180, 100%, 50%)` should convert to cyan

Instead, the colors are coming out completely different than what they should be.

### System Info
- @mantine/core version: latest
- Browser: Chrome 121

This is breaking color theming in my application. Any help would be appreciated!

---
Repository: /testbed
