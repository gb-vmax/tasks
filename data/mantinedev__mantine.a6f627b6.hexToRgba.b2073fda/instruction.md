# Bug Report

### Describe the bug

When using hex colors with alpha channel (8-digit hex format like `#RRGGBBAA`), the color conversion is producing incorrect RGBA values. The red, green, blue, and alpha channels appear to be getting mixed up or parsed from wrong positions.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// Using an 8-digit hex color with alpha
const result = toRgba('#FF0000FF'); // Red with full opacity
console.log(result);
// Expected: { r: 255, g: 0, b: 0, a: 1 }
// Getting incorrect values

// Another example
const result2 = toRgba('#00FF0080'); // Green with 50% opacity
console.log(result2);
// Expected: { r: 0, g: 255, b: 0, a: 0.5 }
// Getting incorrect values
```

Also noticed that 3-digit shorthand hex colors like `#RGB` are not expanding correctly - the color channels seem to be in the wrong order.

```js
const result3 = toRgba('#F00'); // Should be red
console.log(result3);
// Expected: { r: 255, g: 0, b: 0, a: 1 }
// Getting unexpected color
```

### Expected behavior

The `toRgba` function should correctly parse hex colors and return the proper RGBA values:
- For 8-digit hex (`#RRGGBBAA`), it should extract R, G, B, and A from the correct positions
- For 3-digit shorthand (`#RGB`), it should expand to `#RRGGBB` correctly

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
