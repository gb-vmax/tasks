# Bug Report

### Describe the bug

The `localStorageColorSchemeManager` is not properly handling color scheme values from localStorage. When a valid color scheme is stored in localStorage, it's being ignored and the default value is returned instead. Additionally, storage events from the same window's localStorage are not being processed correctly.

### Reproduction

```js
import { localStorageColorSchemeManager } from '@mantine/core';

const manager = localStorageColorSchemeManager({ key: 'mantine-color-scheme' });

// Store a valid color scheme in localStorage
window.localStorage.setItem('mantine-color-scheme', 'dark');

// Try to get the stored value
const colorScheme = manager.get('light'); // Expected: 'dark', Actual: 'light'
```

The manager returns the default value ('light') even though 'dark' is stored in localStorage.

Also, when localStorage changes in the same window, the subscription callback is not triggered:

```js
const manager = localStorageColorSchemeManager({ key: 'mantine-color-scheme' });

manager.subscribe((newScheme) => {
  console.log('Color scheme changed:', newScheme);
});

// This should trigger the callback but doesn't
window.localStorage.setItem('mantine-color-scheme', 'dark');
window.dispatchEvent(new StorageEvent('storage', {
  key: 'mantine-color-scheme',
  newValue: 'dark',
  storageArea: window.localStorage
}));
```

### Expected behavior

1. When a valid color scheme is stored in localStorage, `manager.get()` should return that stored value instead of the default
2. Storage events from the same window's localStorage should trigger the subscription callback

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
