# Bug Report

### Describe the bug

I'm experiencing an issue with color parsing in the MantineProvider. When I pass valid color values in formats like `rgb()`, `hsl()`, or CSS color names, they're not being converted correctly to RGBA format. It seems like only hex colors are being processed, and all other formats are returning unexpected values.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// RGB colors not working
const rgb = toRgba('rgb(255, 0, 0)');
console.log(rgb); // Expected: { r: 255, g: 0, b: 0, a: 1 }

// HSL colors not working
const hsl = toRgba('hsl(120, 100%, 50%)');
console.log(hsl); // Expected: { r: 0, g: 255, b: 0, a: 1 }

// CSS color names not working
const named = toRgba('blue');
console.log(named); // Expected: { r: 0, g: 0, b: 255, a: 1 }
```

All of these are returning `{ r: 0, g: 0, b: 0, a: 0 }` instead of the correct color values. Only hex colors like `#ff0000` seem to work properly.

### Expected behavior

The `toRgba` function should correctly parse all valid CSS color formats (hex, rgb, rgba, hsl, hsla, and named colors) and convert them to RGBA objects with the proper alpha channel value.

### System Info

- @mantine/core version: latest
- Browser: Chrome 121

---
Repository: /testbed
