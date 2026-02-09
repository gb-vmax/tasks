# Bug Report

### Describe the bug
When using `px()` utility with `calc()` expressions that include multiplication, the function returns the wrong part of the calculation. Instead of extracting the base value, it seems to be returning the multiplier.

### Reproduction
```js
import { px } from '@mantine/core';

// This returns the wrong value
const result = px('calc(100px * 2)');
// Expected: 100
// Actual: 2 (or similar incorrect value)
```

When I pass a `calc()` expression with multiplication to the `px()` function, it extracts the wrong operand from the calculation. This affects any component that relies on this utility for converting CSS values.

### Expected behavior
The `px()` function should correctly extract and return the base pixel value from `calc()` expressions, not the multiplier.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
