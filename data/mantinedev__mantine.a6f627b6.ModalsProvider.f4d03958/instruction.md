# Bug Report

### Describe the bug

The `closeAll()` method from ModalsProvider doesn't work anymore unless you explicitly pass `true` as the canceled parameter. Calling `closeAll()` without arguments or with `false` doesn't close any modals.

### Reproduction

```jsx
import { ModalsProvider, modals } from '@mantine/modals';

function MyComponent() {
  const handleCloseAll = () => {
    // This doesn't close modals anymore
    modals.closeAll();
    
    // Also doesn't work
    modals.closeAll(false);
    
    // Only this works now
    modals.closeAll(true);
  };

  return (
    <button onClick={handleCloseAll}>Close All Modals</button>
  );
}
```

### Expected behavior

Calling `closeAll()` without any arguments should close all open modals. The `canceled` parameter should be optional and default behavior should be to close all modals regardless of whether it's called with no args, `false`, or `true`.

### System Info
- @mantine/modals: latest
- @mantine/core: latest
- React: 18.x

---
Repository: /testbed
