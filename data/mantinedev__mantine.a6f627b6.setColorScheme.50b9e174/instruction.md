# Bug Report

### Describe the bug

When using `HeadlessMantineProvider` and calling `setColorScheme`, the class list manipulation seems to be inverted. The current scheme gets removed from the classList while the new scheme gets added, but the logic appears backwards - it removes the new scheme and adds the current (old) scheme instead.

### Reproduction

```jsx
import { HeadlessMantineProvider } from '@mantine/core';

function App() {
  return (
    <HeadlessMantineProvider>
      <button onClick={() => {
        // Try to switch from light to dark
        document.documentElement.setAttribute('data-color-scheme', 'light');
        document.documentElement.classList.add('light');
        
        // This should switch to dark mode
        setColorScheme('dark');
        
        // Expected: classList contains 'dark', removed 'light'
        // Actual: classList contains 'light', removed 'dark'
        console.log(document.documentElement.classList); // shows 'light' instead of 'dark'
      }}>
        Toggle Theme
      </button>
    </HeadlessMantineProvider>
  );
}
```

### Expected behavior

When switching color schemes, the old scheme class should be removed from the classList and the new scheme class should be added. For example, switching from 'light' to 'dark' should remove the 'light' class and add the 'dark' class.

### Actual behavior

The opposite happens - the new scheme class gets removed and the old scheme class gets added back, making it impossible to properly switch themes using classList.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox
- OS: Any

---
Repository: /testbed
