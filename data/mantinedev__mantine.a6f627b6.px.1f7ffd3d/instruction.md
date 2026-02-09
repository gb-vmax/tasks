# Bug Report

### Describe the bug

The `px()` utility function is not handling CSS values correctly. When I pass in strings with `calc()` or `var()`, they're not being returned as-is anymore. Also, the `rem` to pixel conversion seems off - I'm getting unexpected values.

### Reproduction

```js
import { px } from '@mantine/core';

// This should return the string as-is but doesn't
const calcValue = px('calc(100% - 20px)');
console.log(calcValue); // Expected: 'calc(100% - 20px)'

// This should also return the string as-is but doesn't
const varValue = px('var(--some-variable)');
console.log(varValue); // Expected: 'var(--some-variable)'

// rem conversion is giving wrong values
const remValue = px('2rem');
console.log(remValue); // Expected: 32, but getting 30
```

### Expected behavior

1. CSS `calc()` expressions should be returned unchanged
2. CSS `var()` references should be returned unchanged  
3. `rem` values should convert to pixels using the standard 16px base (e.g., `2rem` = 32px)

### System Info

- @mantine/core version: latest
- Browser: Chrome

This is breaking my layouts where I use CSS variables and calc expressions. Any help would be appreciated!

---
Repository: /testbed
