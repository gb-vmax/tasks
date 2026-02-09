# Bug Report

### Describe the bug

The ColorPicker component is not parsing hex color values correctly. When I pass a hex color string like `#ff0000` or `#abc`, the color doesn't get recognized and falls back to a default color instead.

### Reproduction

```js
import { parseColor } from '@mantine/core';

// This should parse correctly but returns wrong values
const color1 = parseColor('#ff0000');
console.log(color1); // Expected: red color in HSVA format

const color2 = parseColor('#abc');
console.log(color2); // Expected: light blue color in HSVA format

// RGB colors work fine
const color3 = parseColor('rgb(255, 0, 0)');
console.log(color3); // This works as expected
```

### Expected behavior

Hex color strings should be parsed correctly and converted to HSVA format. The function should recognize both 3-digit and 6-digit hex formats.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

This seems to have started happening recently. HSL and RGB formats work fine, but hex colors are broken.

---
Repository: /testbed
