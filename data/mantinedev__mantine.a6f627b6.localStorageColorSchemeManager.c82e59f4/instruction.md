# Bug Report

### Describe the bug

The `localStorageColorSchemeManager` is not working correctly - it's returning the wrong color scheme value when retrieving from localStorage. When I have a valid color scheme stored in localStorage (like 'dark' or 'light'), the manager returns the `defaultValue` instead of the stored value.

Also, the storage event listener doesn't seem to trigger when the color scheme is changed in localStorage. When I update the color scheme in another tab or window, the current tab doesn't pick up the change.

### Reproduction

```js
import { localStorageColorSchemeManager } from '@mantine/core';

const manager = localStorageColorSchemeManager({ key: 'mantine-color-scheme' });

// Set color scheme to 'dark' in localStorage
localStorage.setItem('mantine-color-scheme', 'dark');

// Try to get the stored value
const colorScheme = manager.get('light'); // Returns 'light' instead of 'dark'
console.log(colorScheme); // Expected: 'dark', Actual: 'light'
```

For the storage event issue:
1. Open the app in two browser tabs
2. Change the color scheme in tab 1 (which updates localStorage)
3. Tab 2 doesn't update to reflect the change

### Expected behavior

1. When a valid color scheme is stored in localStorage, `manager.get()` should return that stored value, not the default value
2. When localStorage is updated in another tab/window, the storage event listener should trigger and update the color scheme across all tabs

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
