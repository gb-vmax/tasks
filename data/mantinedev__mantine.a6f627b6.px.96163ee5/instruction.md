# Bug Report

### Describe the bug

The `px()` utility function is not handling CSS string values correctly. When I pass values containing `calc()` or `var()`, they get converted to pixel values instead of being returned as-is. Also, `rem` unit conversions are producing incorrect pixel values.

### Reproduction

```js
import { px } from '@mantine/core';

// This should return the calc string as-is, but it's being converted
const result1 = px('calc(100% - 20px)');
console.log(result1); // Expected: 'calc(100% - 20px)', Actual: converted to number

// This should return the var string as-is
const result2 = px('var(--some-value)');
console.log(result2); // Expected: 'var(--some-value)', Actual: converted to number

// rem conversion is also wrong
const result3 = px('2rem');
console.log(result3); // Expected: 32 (2 * 16), Actual: 30 (2 * 15)
```

### Expected behavior

- Values containing `calc()` or `var()` should be returned as-is without conversion
- `rem` values should be converted using the standard 16px base (1rem = 16px)

### System Info

- @mantine/core version: latest
- Browser: Chrome
- OS: macOS

---
Repository: /testbed
