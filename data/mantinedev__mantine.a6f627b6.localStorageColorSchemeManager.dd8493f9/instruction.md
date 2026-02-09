# Bug Report

### Describe the bug

The local storage color scheme manager is returning incorrect values when retrieving the stored color scheme. When a valid color scheme is stored in localStorage, it returns the default value instead of the stored value, and vice versa.

### Reproduction

```js
import { localStorageColorSchemeManager } from '@mantine/core';

const manager = localStorageColorSchemeManager({ key: 'mantine-color-scheme' });

// Store 'dark' in localStorage
localStorage.setItem('mantine-color-scheme', 'dark');

// Try to get the color scheme
const colorScheme = manager.get('light'); // Expected: 'dark', Actual: 'light'
```

### Steps to reproduce:
1. Set up a MantineProvider with localStorageColorSchemeManager
2. Store a valid color scheme value ('light' or 'dark') in localStorage
3. Refresh the page or retrieve the color scheme
4. The manager returns the default value instead of the stored value

### Expected behavior

When a valid color scheme is stored in localStorage, the manager should return that stored value. If the stored value is invalid or doesn't exist, then it should fall back to the default value.

### Additional context

Also noticed that storage events from localStorage changes don't seem to trigger updates anymore. The color scheme doesn't sync across tabs like it used to.

---
Repository: /testbed
