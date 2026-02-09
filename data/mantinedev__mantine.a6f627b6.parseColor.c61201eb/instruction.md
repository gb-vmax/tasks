# Bug Report

### Describe the bug

The `parseColor` function is not correctly parsing hex color values. When I pass a hex color string like `#ff0000` or `#00ff00`, it's not being recognized and instead returns an unexpected result.

### Reproduction

```js
import { parseColor } from '@mantine/core';

// This doesn't work as expected
const color1 = parseColor('#ff0000');
console.log(color1); // Should parse the hex color but doesn't

const color2 = parseColor('#00ff00');
console.log(color2); // Same issue here

// Other formats might be affected too
const color3 = parseColor('rgb(255, 0, 0)');
console.log(color3);
```

### Expected behavior

The function should correctly parse hex color strings (and potentially other color formats) and return the corresponding HSVA color object. For example, `#ff0000` should be converted to its HSVA representation.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

This seems to have started recently. The color picker component is affected by this as it relies on `parseColor` internally.

---
Repository: /testbed
