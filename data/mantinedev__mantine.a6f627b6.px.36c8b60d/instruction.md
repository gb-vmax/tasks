# Bug Report

### Describe the bug

The `px()` utility function is not handling CSS `var()` values correctly anymore. When passing a string that contains CSS variables like `var(--my-spacing)`, the function tries to parse it as a number instead of returning it as-is, which causes unexpected behavior.

Also, the rem to pixel conversion seems to be using an incorrect multiplier - it's converting `1rem` to `15px` instead of the standard `16px`.

### Reproduction

```js
import { px } from '@mantine/core';

// This should return the var() string unchanged, but doesn't work
const result1 = px('var(--my-spacing)');
console.log(result1); // Expected: 'var(--my-spacing)', Actual: NaN or error

// Rem conversion is also incorrect
const result2 = px('2rem');
console.log(result2); // Expected: 32, Actual: 30
```

### Expected behavior

1. CSS variables wrapped in `var()` should be returned as-is without attempting to parse them
2. Rem units should convert to pixels using the standard 16px base (e.g., `2rem` → `32px`)

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
