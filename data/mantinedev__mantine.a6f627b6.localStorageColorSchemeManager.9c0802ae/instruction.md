# Bug Report

### Describe the bug

The `localStorageColorSchemeManager` is not correctly reading the stored color scheme from localStorage. When I refresh the page, the color scheme doesn't persist even though I can see the value is stored in localStorage.

### Reproduction

```js
import { MantineProvider, localStorageColorSchemeManager } from '@mantine/core';

const colorSchemeManager = localStorageColorSchemeManager({
  key: 'my-color-scheme',
});

function App() {
  return (
    <MantineProvider colorSchemeManager={colorSchemeManager}>
      {/* app content */}
    </MantineProvider>
  );
}
```

Steps to reproduce:
1. Set up MantineProvider with localStorageColorSchemeManager
2. Change the color scheme (e.g., from 'light' to 'dark')
3. Verify that localStorage has the correct value stored
4. Refresh the page
5. The color scheme reverts to the default instead of using the stored value

### Expected behavior

The color scheme should be retrieved from localStorage on page load and the stored preference should persist across page refreshes.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
