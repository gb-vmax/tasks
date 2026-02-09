# Bug Report

### Describe the bug

When using `HeadlessMantineProvider`, calling `setColorScheme` causes the application to crash with a runtime error. The function appears to be trying to access `this.currentScheme`, `this.applyScheme()`, and `this.savePreference()` which don't exist in the context.

### Reproduction

```jsx
import { HeadlessMantineProvider } from '@mantine/core';

function App() {
  const { setColorScheme } = useMantineColorScheme();
  
  return (
    <HeadlessMantineProvider>
      <button onClick={() => setColorScheme('dark')}>
        Switch to dark mode
      </button>
    </HeadlessMantineProvider>
  );
}
```

When clicking the button, the app throws an error because `this` is undefined in the `setColorScheme` function.

### Expected behavior

The `setColorScheme` function should either be a no-op (like it was before) or properly handle color scheme changes without throwing errors. In a headless provider context, it probably shouldn't try to apply schemes or save preferences since there's no actual theme management happening.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
