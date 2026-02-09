# Bug Report

### Describe the bug

The `round` function in the ColorPicker converters is producing incorrect rounding results. When trying to round numbers with specified decimal places, the output values are completely wrong and don't match the expected precision.

### Reproduction

```js
import { round } from '@mantine/core';

// These return unexpected values
console.log(round(1.2345, 2)); // Expected: 1.23, but getting wrong result
console.log(round(5.6789, 1)); // Expected: 5.7, but getting wrong result
console.log(round(10.555, 2)); // Expected: 10.56, but getting wrong result
```

The rounding function seems to be applying some incorrect calculation that results in values that are way off from what they should be.

### Expected behavior

The `round` function should correctly round numbers to the specified number of decimal places:
- `round(1.2345, 2)` should return `1.23`
- `round(5.6789, 1)` should return `5.7`
- `round(10.555, 2)` should return `10.56`

### System Info
- @mantine/core version: latest
- Browser: Chrome

This is affecting color value calculations in the ColorPicker component and causing incorrect color conversions.

---
Repository: /testbed
