# Bug Report

### Describe the bug

The `rgba()` function is returning the fallback color `rgba(0, 0, 0, 1)` for valid alpha values between 0 and 1, which should be accepted. This causes colors to unexpectedly render as black when using valid alpha transparency values.

### Reproduction

```js
import { rgba } from '@mantine/core';

// These should work but return 'rgba(0, 0, 0, 1)' instead
console.log(rgba('#ff0000', 0.5));  // Expected: rgba(255, 0, 0, 0.5), Got: rgba(0, 0, 0, 1)
console.log(rgba('#00ff00', 0.8));  // Expected: rgba(0, 255, 0, 0.8), Got: rgba(0, 0, 0, 1)
console.log(rgba('blue', 0.3));     // Expected: rgba(0, 0, 255, 0.3), Got: rgba(0, 0, 0, 1)
```

All valid alpha values (0 to 1) are being rejected and the function falls back to returning black. This makes it impossible to create transparent colors using the rgba helper.

### Expected behavior

The `rgba()` function should accept alpha values between 0 and 1 (inclusive) and return the properly formatted rgba color string with the specified transparency.

### Additional context

Also noticed that for `oklch` colors, the alpha replacement seems to be removing more than just the alpha value when the color already includes an alpha channel. The regex pattern might be too greedy.

---
Repository: /testbed
