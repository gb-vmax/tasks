# Bug Report

### Describe the bug

The `closeOnEscape` utility is not triggering callbacks when the Escape key is pressed. I have a modal/overlay component that should close when pressing Escape, but the close handler is never called.

### Reproduction

```js
import { closeOnEscape } from '@mantine/core';

const handleClose = () => {
  console.log('Modal should close');
  setOpened(false);
};

const handleKeyDown = closeOnEscape(handleClose, { active: true });

// When pressing Escape key, nothing happens
// The handleClose callback is never invoked
```

### Expected behavior

When the Escape key is pressed and a valid callback is provided with `active: true`, the callback should be executed and the modal/overlay should close.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox/Safari (tested on all)

---
Repository: /testbed
