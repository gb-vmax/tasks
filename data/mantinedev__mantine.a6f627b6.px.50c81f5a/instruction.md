# Bug Report

### Describe the bug

The `px()` utility function is not correctly handling CSS values with `calc()` or `var()` functions. When I pass a string containing either `calc()` or `var()` (but not both), the function tries to parse it as a numeric value instead of returning the original string, which causes incorrect conversions.

Additionally, `rem` unit conversion seems to be using an incorrect multiplier - it's converting using `10` instead of the standard `16px` base font size.

### Reproduction

```js
import { px } from '@mantine/core';

// This should return the original string but gets parsed incorrectly
const calcValue = px('calc(100% - 20px)');
console.log(calcValue); // Expected: 'calc(100% - 20px)', Actual: tries to parse as number

const varValue = px('var(--my-spacing)');
console.log(varValue); // Expected: 'var(--my-spacing)', Actual: tries to parse as number

// rem conversion is also wrong
const remValue = px('2rem');
console.log(remValue); // Expected: 32 (2 * 16), Actual: 20 (2 * 10)
```

### Expected behavior

1. Values containing `calc()` OR `var()` should be returned as-is without attempting numeric conversion
2. `rem` units should convert using the standard 16px base (e.g., `2rem` → `32`)

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
