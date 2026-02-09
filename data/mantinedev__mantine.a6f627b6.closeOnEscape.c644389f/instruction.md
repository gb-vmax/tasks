# Bug Report

### Describe the bug

The `closeOnEscape` utility is not working as expected. When pressing the Escape key, the callback function is not being triggered. It seems like the escape key handler is completely broken.

### Reproduction

```js
import { closeOnEscape } from '@mantine/core';

const handleClose = () => {
  console.log('Modal should close');
};

const keyDownHandler = closeOnEscape(handleClose, { active: true });

// Simulate pressing Escape key
const event = { key: 'Escape' };
keyDownHandler(event);

// Expected: handleClose should be called and log "Modal should close"
// Actual: Nothing happens
```

### Expected behavior

When the Escape key is pressed, the provided callback function should be invoked. This is critical for modals, popovers, and other overlay components that need to close on Escape.

### Additional context

This affects all components that rely on `closeOnEscape` for keyboard navigation, including:
- Modal
- Drawer
- Popover
- Menu

The issue makes these components unusable for keyboard users who expect standard Escape key behavior.

---
Repository: /testbed
