# Bug Report

### Describe the bug

The `useModalsStack` hook appears to be broken - I'm getting a TypeScript error saying the function doesn't return anything. When I try to use it in my component, I get runtime errors about undefined properties.

### Reproduction

```tsx
import { useModalsStack } from '@mantine/core';

function MyComponent() {
  const modals = useModalsStack(['login', 'signup']);
  
  // This throws an error - modals is undefined
  const handleOpen = () => {
    modals.open('login');
  };
  
  return <button onClick={handleOpen}>Open Modal</button>;
}
```

### Expected behavior

The hook should return an object with `state`, `open`, `close`, `toggle`, `closeAll`, and `register` methods that can be used to manage modal state.

### System Info
- @mantine/core version: latest
- React version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
