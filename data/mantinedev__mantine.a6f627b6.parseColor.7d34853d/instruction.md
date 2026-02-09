# Bug Report

### Describe the bug

The ColorPicker component is not parsing hex color values correctly. When I try to use a hex color string like `#ff0000`, it doesn't get recognized and falls through to an incorrect conversion.

### Reproduction

```js
import { parseColor } from '@mantine/core';

// This should parse as red hex color
const color = parseColor('#ff0000');
console.log(color);

// Expected: { h: 0, s: 100, v: 100, a: 1 }
// Actual: incorrect values or wrong conversion applied
```

### Expected behavior

Hex colors (like `#ff0000`, `#00ff00`, `#0000ff`) should be properly detected and converted to HSVA format. The parser should recognize the hex format pattern and apply the correct conversion.

### Additional context

This seems to have broken recently. The color parser appears to be skipping the hex color validation pattern and using a different converter instead. Other color formats might be affected too.

---
Repository: /testbed
