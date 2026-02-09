# Bug Report

### Describe the bug

The `round` function in the ColorPicker component is producing incorrect rounding results. When rounding numbers with specified decimal places, the output values are off by a factor of 10.

### Reproduction

```js
import { round } from '@mantine/core';

// Expected: 1.23, Actual: 1.2
console.log(round(1.234, 2));

// Expected: 5.68, Actual: 5.7
console.log(round(5.678, 2));

// Expected: 0.46, Actual: 0.5
console.log(round(0.456, 2));
```

### Expected behavior

The `round` function should round numbers to the specified number of decimal places correctly. For example, `round(1.234, 2)` should return `1.23`, not `1.2`.

This is affecting color values in the ColorPicker component, causing colors to be displayed/stored with incorrect precision.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
