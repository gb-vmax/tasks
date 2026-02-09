# Bug Report

### Describe the bug

The ColorPicker component is returning black (`#000000`) for all valid color values, regardless of the actual color or format specified. When passing a valid HsvaColor object, the converter always outputs `#000000` instead of the correct color representation.

### Reproduction

```js
import { convertHsvaTo } from '@mantine/core';

const color = {
  h: 180,
  s: 50,
  v: 75,
  a: 1
};

// This returns '#000000' instead of the actual color
const hexColor = convertHsvaTo('hex', color);
console.log(hexColor); // Expected: '#5fbfbf', Actual: '#000000'

const rgbColor = convertHsvaTo('rgb', color);
console.log(rgbColor); // Expected: 'rgb(95, 191, 191)', Actual: '#000000'
```

### Expected behavior

The `convertHsvaTo` function should convert the provided HsvaColor object to the requested format (hex, rgb, rgba, hsl, hsla) and return the correct color string representation. Instead, it's returning black for all valid color inputs.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

This is breaking color selection in the ColorPicker component as all selected colors appear as black.

---
Repository: /testbed
