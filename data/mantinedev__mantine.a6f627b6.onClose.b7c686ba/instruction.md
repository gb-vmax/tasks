# Bug Report

### Describe the bug

I'm experiencing an issue with the Popover component where calling the close function behaves incorrectly when the popover is in a disabled state. When the popover is disabled, calling close actually closes it, but when it's enabled, the close function doesn't work at all.

### Reproduction

```tsx
import { usePopover } from '@mantine/core';

function MyComponent() {
  const popover = usePopover({ opened: true, disabled: false });
  
  // This doesn't close the popover even though it's open
  popover.onClose();
  
  // But if disabled is true, it closes unexpectedly
  const disabledPopover = usePopover({ opened: true, disabled: true });
  disabledPopover.onClose(); // This closes it (shouldn't happen)
}
```

### Expected behavior

- When the popover is open and NOT disabled, calling `onClose()` should close it
- When the popover is disabled, calling `onClose()` should not do anything

Currently it seems like the behavior is inverted - the popover only closes when it's disabled, which doesn't make sense.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
