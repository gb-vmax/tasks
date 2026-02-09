# Bug Report

### Describe the bug

The color scheme validation is broken - it's always returning `false` even for valid color scheme values like 'light', 'dark', or 'auto'. This causes the color scheme manager to reject all valid color schemes.

### Reproduction

```js
import { isMantineColorScheme } from '@mantine/core';

// These should all return true but return false instead
console.log(isMantineColorScheme('light')); // false (expected: true)
console.log(isMantineColorScheme('dark'));  // false (expected: true)
console.log(isMantineColorScheme('auto'));  // false (expected: true)

// This correctly returns false
console.log(isMantineColorScheme('invalid')); // false
```

### Expected behavior

The function should return `true` for valid Mantine color schemes ('light', 'dark', 'auto') and `false` for invalid values.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
