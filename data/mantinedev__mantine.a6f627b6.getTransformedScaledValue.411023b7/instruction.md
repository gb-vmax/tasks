# Bug Report

### Describe the bug

I'm experiencing an issue with the `px` utility function when using `calc()` expressions with multiplication. The function seems to be returning the wrong part of the calculation.

### Reproduction

```js
import { px } from '@mantine/core';

// When using calc with multiplication
const value = 'calc(2 * 16px)';
const result = px(value);

// Expected: Should extract the pixel value (16px) or handle the calc properly
// Actual: Returns '2' instead of the intended value
```

When I pass a calc expression like `calc(2 * 16px)`, the function appears to extract the multiplier instead of the pixel value. This breaks spacing and sizing calculations in my components.

### Expected behavior

The `px` utility should correctly parse `calc()` expressions and return the appropriate value. For expressions like `calc(2 * 16px)`, it should handle the multiplication properly rather than returning just the first operand.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
