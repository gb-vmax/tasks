# Bug Report

### Describe the bug

The ColorPicker component is returning incorrect color values when converting HSVA colors to different formats. Instead of returning the converted color, it's always returning black (`#000000`) when a valid color object is passed in, and returning the hex conversion when an invalid format is specified.

### Reproduction

```js
import { convertHsvaTo } from '@mantine/core';

const color = { h: 120, s: 100, v: 100, a: 1 }; // Green color

// This returns '#000000' instead of the actual color
const hex = convertHsvaTo('hex', color);
console.log(hex); // Expected: '#00ff00', Actual: '#000000'

// This also returns '#000000' for other formats
const rgb = convertHsvaTo('rgb', color);
console.log(rgb); // Expected: 'rgb(0, 255, 0)', Actual: '#000000'

// Using an invalid format returns a hex value instead of defaulting properly
const invalid = convertHsvaTo('invalid', color);
console.log(invalid); // Returns hex value instead of expected behavior
```

### Expected behavior

- When passing a valid color object and format, the function should return the color converted to the specified format
- When passing an invalid format, it should fall back to hex conversion
- The function should only return `#000000` when the color object is null/undefined

### System Info
- @mantine/core version: latest
- Framework: React

---
Repository: /testbed
