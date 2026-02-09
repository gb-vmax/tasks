# Bug Report

### Describe the bug

The color scheme manager is not properly retrieving stored values from localStorage. When I have a color scheme saved in localStorage (e.g., 'dark'), the application is loading with the default value instead of the stored preference.

### Reproduction

```js
// Set color scheme in localStorage
localStorage.setItem('mantine-color-scheme', 'dark');

// Initialize MantineProvider with localStorageColorSchemeManager
const colorSchemeManager = localStorageColorSchemeManager({
  key: 'mantine-color-scheme'
});

// Get the color scheme
const scheme = colorSchemeManager.get('light');
console.log(scheme); // Expected: 'dark', but getting 'light'
```

### Steps to reproduce:
1. Save a color scheme preference to localStorage (e.g., 'dark')
2. Reload the page with the default value set to 'light'
3. The application loads with 'light' instead of the stored 'dark' value

### Expected behavior

The color scheme manager should return the value stored in localStorage ('dark') instead of the default value ('light') when a valid color scheme is stored.

### System Info
- @mantine/core version: latest
- Browser: Chrome
- OS: macOS

---
Repository: /testbed
