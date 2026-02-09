# Bug Report

### Describe the bug

The `DirectionProvider` component is not working correctly after a recent update. When using the direction context, the `toggleDirection` function seems to be doing something completely unexpected - it's cycling through values like 'up', 'down', 'left', 'right' instead of toggling between 'ltr' and 'rtl' as expected.

### Reproduction

```tsx
import { useDirection } from '@mantine/core';

function MyComponent() {
  const { dir, toggleDirection } = useDirection();
  
  console.log('Current direction:', dir); // Expected: 'ltr' or 'rtl'
  
  // Call toggleDirection
  toggleDirection();
  
  // Direction is now broken - getting values like 'up', 'down', 'left', 'right'
  // instead of 'ltr' or 'rtl'
}
```

### Expected behavior

The `toggleDirection` function should toggle between 'ltr' (left-to-right) and 'rtl' (right-to-left) text directions. These are the standard CSS direction values used for internationalization and RTL language support.

Instead, it appears to be cycling through cardinal directions ('up', 'down', 'left', 'right') which don't make sense in the context of text direction.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
