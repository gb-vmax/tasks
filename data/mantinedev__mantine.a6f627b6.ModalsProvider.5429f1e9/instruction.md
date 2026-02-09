# Bug Report

### Describe the bug

When calling `closeAll()` without any arguments (or with `canceled: false`), the modals don't actually close. The function seems to do nothing in this case, leaving all modals open on the screen.

### Reproduction

```jsx
import { ModalsProvider, modals } from '@mantine/modals';

// Open some modals
modals.open({ title: 'Modal 1', children: 'Content 1' });
modals.open({ title: 'Modal 2', children: 'Content 2' });

// Try to close all modals
modals.closeAll(); // Does nothing - modals stay open

// This works though:
modals.closeAll(true); // Modals close properly
```

### Expected behavior

Calling `closeAll()` or `closeAll(false)` should close all open modals, just like `closeAll(true)` does. The `canceled` parameter should only affect the state passed to callbacks, not whether the modals actually close.

### System Info
- @mantine/modals version: latest
- React version: 18.x

---
Repository: /testbed
