# Bug Report

### Describe the bug

I'm experiencing an issue with the `sizeResolver` function where numeric string values are not being converted to `rem` units as expected. When passing numeric strings like `"16"` or `"24"` to style props, they're returned as-is instead of being converted to rem values.

### Reproduction

```js
import { sizeResolver } from '@mantine/core';

// This should return rem value but returns the string instead
const result1 = sizeResolver("16");
console.log(result1); // Expected: "1rem", Actual: "16"

const result2 = sizeResolver("24");
console.log(result2); // Expected: "1.5rem", Actual: "24"

// Number values work correctly
const result3 = sizeResolver(16);
console.log(result3); // Returns "1rem" as expected
```

This affects components that accept size props when passing numeric strings instead of numbers. The values aren't being normalized to rem units, which can lead to inconsistent styling.

### Expected behavior

Numeric strings should be converted to numbers and then to rem units, just like regular number values are. Both `sizeResolver(16)` and `sizeResolver("16")` should produce the same output.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
