# Bug Report

### Describe the bug

The color scheme validation is broken - when I try to set any color scheme value (auto, dark, or light), the `isMantineColorScheme` function always returns false. This prevents the color scheme from being applied correctly.

### Reproduction

```js
import { isMantineColorScheme } from '@mantine/core';

console.log(isMantineColorScheme('light')); // Expected: true, Actual: false
console.log(isMantineColorScheme('dark'));  // Expected: true, Actual: false
console.log(isMantineColorScheme('auto'));  // Expected: true, Actual: false
```

All valid color scheme values are being rejected, which breaks the color scheme manager functionality.

### Expected behavior

The function should return `true` for valid Mantine color scheme values ('auto', 'dark', 'light') and `false` for invalid values.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
