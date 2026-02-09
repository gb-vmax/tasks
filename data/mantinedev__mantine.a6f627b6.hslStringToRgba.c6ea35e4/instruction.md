# Bug Report

### Describe the bug

I'm experiencing incorrect color conversion results when using HSL color strings. The colors are coming out completely wrong - they look washed out and the hues are off.

### Reproduction

```js
import { toRgba } from '@mantine/core';

// Converting HSL to RGBA produces incorrect results
const color1 = toRgba('hsl(240, 100%, 50%)'); // Should be pure blue
const color2 = toRgba('hsl(300, 50%, 50%)');  // Should be a purple/magenta

console.log(color1); // RGB values are incorrect
console.log(color2); // RGB values are incorrect
```

The converted RGB values don't match what they should be for the given HSL inputs. Testing with various HSL values shows the conversion is producing wrong colors consistently.

### Expected behavior

HSL to RGBA conversion should produce accurate RGB color values that match the input HSL color. For example, `hsl(240, 100%, 50%)` should convert to pure blue `rgb(0, 0, 255)`.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
