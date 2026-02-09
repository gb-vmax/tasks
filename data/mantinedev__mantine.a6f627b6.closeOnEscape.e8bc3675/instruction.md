# Bug Report

### Describe the bug

The `closeOnEscape` utility is not triggering the callback when the Escape key is pressed. It seems like the behavior is inverted - the callback gets triggered for every key *except* Escape, and it doesn't fire at all when Escape is actually pressed.

### Reproduction

```js
import { closeOnEscape } from '@mantine/core';

const handleClose = () => {
  console.log('Modal should close');
};

const handleKeyDown = closeOnEscape(handleClose, { active: true });

// Pressing Escape key does nothing
// Pressing any other key (a, b, Enter, etc.) triggers the callback
```

### Expected behavior

The callback should be invoked when the Escape key is pressed, not when other keys are pressed. The utility should ignore all other keys and only respond to Escape.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
