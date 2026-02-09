# Bug Report

### Describe the bug

When using `HeadlessMantineProvider`, the `setColorScheme` function doesn't work as expected. The function appears to execute some logic internally, but the color scheme doesn't actually change in the application. This seems to be a regression as it was working fine in previous versions.

### Reproduction

```tsx
import { HeadlessMantineProvider, useMantineColorScheme } from '@mantine/core';

function App() {
  return (
    <HeadlessMantineProvider>
      <MyComponent />
    </HeadlessMantineProvider>
  );
}

function MyComponent() {
  const { setColorScheme } = useMantineColorScheme();
  
  // This doesn't actually change the color scheme
  const handleClick = () => {
    setColorScheme('dark');
  };
  
  return <button onClick={handleClick}>Toggle Dark Mode</button>;
}
```

### Expected behavior

Calling `setColorScheme('dark')` should update the color scheme to dark mode. The UI should reflect the change accordingly.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
