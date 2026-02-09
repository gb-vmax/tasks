# Bug Report

### Describe the bug

The `isMantineColorScheme` function is not correctly validating color scheme values. When I try to set a color scheme using the color scheme manager, it's not recognizing valid values like `'light'`, `'dark'`, or `'auto'`.

### Reproduction

```js
import { isMantineColorScheme } from '@mantine/core';

// These should all return true but they don't
console.log(isMantineColorScheme('light')); // returns false
console.log(isMantineColorScheme('dark'));  // returns false
console.log(isMantineColorScheme('auto'));  // returns false

// Invalid values should return false (this works as expected)
console.log(isMantineColorScheme('invalid')); // returns false
```

### Expected behavior

The function should return `true` for valid color scheme values (`'light'`, `'dark'`, `'auto'`) and `false` for any other values.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
