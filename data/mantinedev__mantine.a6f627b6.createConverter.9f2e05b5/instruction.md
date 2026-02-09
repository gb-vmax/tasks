# Bug Report

### Describe the bug

I'm experiencing an issue with unit conversion functions in Mantine. When passing `0` or `'0'` as a value to converters like `rem()` or `em()`, the functions are returning values with units appended (e.g., `"0rem"`) instead of just `"0"` as expected. Additionally, comma-separated values without spaces after commas are not being properly split and converted.

### Reproduction

```js
import { rem } from '@mantine/core';

// This should return "0" but returns "0rem"
console.log(rem(0));      // Expected: "0", Actual: "0rem"
console.log(rem('0'));    // Expected: "0", Actual: "0rem"

// Comma-separated values without spaces don't work
console.log(rem('10,20,30'));  // Not being split and converted properly
```

### Expected behavior

- When value is `0` or `'0'`, the converter should return just `"0"` without any units (since `0px = 0rem = 0em`)
- Comma-separated values like `'10,20,30'` should be split and each value converted individually

### System Info
- @mantine/core version: latest
- Browser: Chrome

This seems to have broken recently. The unit converters were working fine before.

---
Repository: /testbed
