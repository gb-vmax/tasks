# Bug Report

### Describe the bug

After a recent update, I'm getting an error when trying to use the `closeAll` function from the modals context. The application crashes with a reference error saying that `state` is not defined.

### Reproduction

```jsx
import { useModals } from '@mantine/modals';

function MyComponent() {
  const modals = useModals();
  
  // This causes a crash
  const handleCloseAll = () => {
    modals.closeAll();
  };
  
  return <button onClick={handleCloseAll}>Close All Modals</button>;
}
```

### Expected behavior

The `closeAll` function should close all open modals without throwing any errors. This was working fine in previous versions.

### System Info
- @mantine/modals version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
