# Bug Report

### Describe the bug

I'm experiencing an issue with `HeadlessMantineProvider` where the `clearColorScheme` function seems to be removing data attributes incorrectly. After calling this function, some color-related attributes remain on the document root element, causing inconsistent styling behavior.

### Reproduction

```jsx
import { HeadlessMantineProvider } from '@mantine/core';

function App() {
  return (
    <HeadlessMantineProvider>
      {/* Your app content */}
    </HeadlessMantineProvider>
  );
}
```

Steps to reproduce:
1. Set up a component with `HeadlessMantineProvider`
2. Add multiple `data-color-*` attributes to the document root (e.g., `data-color-scheme`, `data-color-mode`, `data-color-theme`)
3. Call the `clearColorScheme` method from the color scheme context
4. Inspect the document root element

### Expected behavior

All `data-color-*` attributes should be removed from the document root element when `clearColorScheme` is called. Currently, the last attribute in the list is not being removed, which causes the color scheme to not fully reset.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox
- React version: 18.x

This appears to be affecting the cleanup logic when switching between color schemes or resetting to default values.

---
Repository: /testbed
