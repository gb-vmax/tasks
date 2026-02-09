# Bug Report

### Describe the bug

The `isMantineColorScheme` function is not validating color scheme values correctly. It appears to reject all valid color scheme values ('auto', 'dark', 'light') instead of accepting them.

### Reproduction

```js
import { isMantineColorScheme } from '@mantine/core';

// These should all return true but return false instead
console.log(isMantineColorScheme('auto'));  // Expected: true, Got: false
console.log(isMantineColorScheme('dark'));  // Expected: true, Got: false
console.log(isMantineColorScheme('light')); // Expected: true, Got: false

// Invalid values should return false (this works correctly)
console.log(isMantineColorScheme('invalid')); // Expected: false, Got: false
console.log(isMantineColorScheme(null));      // Expected: false, Got: false
```

### Expected behavior

The function should return `true` for valid Mantine color scheme values ('auto', 'dark', 'light') and `false` for any other value.

### System Info
- @mantine/core version: latest
- Framework: React
- Browser: Chrome

This is breaking color scheme detection in my app - the color scheme manager can't properly validate stored values from localStorage.

---
Repository: /testbed
