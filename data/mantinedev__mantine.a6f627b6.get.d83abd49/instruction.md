# Bug Report

### Describe the bug

The `localStorageColorSchemeManager` is not retrieving the stored color scheme correctly from localStorage. When I set a color scheme (e.g., 'dark' or 'light') and refresh the page, it always falls back to the default value instead of reading the previously saved preference.

### Reproduction

```js
import { MantineProvider, localStorageColorSchemeManager } from '@mantine/core';

const colorSchemeManager = localStorageColorSchemeManager({
  key: 'my-color-scheme'
});

function App() {
  return (
    <MantineProvider colorSchemeManager={colorSchemeManager} defaultColorScheme="light">
      {/* App content */}
    </MantineProvider>
  );
}
```

Steps to reproduce:
1. Set the color scheme to 'dark' using the color scheme toggle
2. Refresh the page
3. The color scheme reverts to 'light' instead of staying 'dark'

When I check localStorage in the browser devtools, I can see the value is properly stored under the correct key, but it's not being read back on page load.

### Expected behavior

The color scheme manager should read the stored value from localStorage and apply it on page load. If I stored 'dark', it should load as 'dark' after refresh.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
