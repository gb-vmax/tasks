# Bug Report

### Describe the bug

The `rem()` function is producing incorrect output when converting pixel values to rem units. Instead of returning a properly formatted rem value, it's generating invalid strings.

### Reproduction

```js
import { rem } from '@mantine/core';

// This returns an invalid value
const result = rem(16);
console.log(result); // Expected: "1rem", but getting something else

// Also affects px string values
const result2 = rem('32px');
console.log(result2); // Expected: "2rem", but getting unexpected output
```

### Expected behavior

- `rem(16)` should return `"1rem"`
- `rem('32px')` should return `"2rem"`
- The function should properly convert numeric pixel values and pixel strings to rem units

### System Info

- @mantine/core version: latest
- This appears to be a regression as it was working in previous versions

---
Repository: /testbed
