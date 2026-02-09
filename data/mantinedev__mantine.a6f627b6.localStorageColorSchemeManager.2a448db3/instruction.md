# Bug Report

### Describe the bug

The local storage color scheme manager is not working correctly. When I try to retrieve the stored color scheme from localStorage, it's returning invalid values instead of the actual stored scheme or the default value.

### Reproduction

```js
import { localStorageColorSchemeManager } from '@mantine/core';

const manager = localStorageColorSchemeManager({ key: 'my-color-scheme' });

// Store a valid color scheme
localStorage.setItem('my-color-scheme', 'dark');

// Try to get the stored value
const scheme = manager.get('light'); // Expected: 'dark', Actual: returns something else
```

Also noticed that the storage event listener doesn't seem to trigger properly when the color scheme changes in another tab. The subscription callback isn't being called when it should be.

### Expected behavior

1. When a valid color scheme ('light', 'dark', or 'auto') is stored in localStorage, `manager.get()` should return that value
2. When an invalid value is stored, it should return the provided default value
3. The subscription should trigger when the color scheme changes in localStorage from another tab/window

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
