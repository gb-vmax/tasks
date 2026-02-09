# Bug Report

### Describe the bug

When using `HeadlessMantineProvider`, calling `clearColorScheme()` in a server-side rendering (SSR) environment causes the application to crash with a ReferenceError. The function tries to access `document` which is not available on the server.

### Reproduction

```jsx
import { HeadlessMantineProvider, useColorScheme } from '@mantine/core';

function MyComponent() {
  const { clearColorScheme } = useColorScheme();
  
  // This crashes during SSR
  clearColorScheme();
  
  return <div>Hello</div>;
}

function App() {
  return (
    <HeadlessMantineProvider>
      <MyComponent />
    </HeadlessMantineProvider>
  );
}
```

### Expected behavior

The `clearColorScheme()` function should be safe to call in SSR environments. It should either:
- Check if `document` exists before accessing it
- Be a no-op when running on the server

### System Info
- @mantine/core version: latest
- Framework: Next.js 14 (SSR enabled)
- Node version: 18.x

### Additional context

This happens specifically with `HeadlessMantineProvider`. The error occurs because the implementation directly accesses `document.documentElement` and `document.body` without checking if we're in a browser environment first.

---
Repository: /testbed
