# Bug Report

### Describe the bug

I'm experiencing an issue with modal IDs when opening multiple modals. It seems like the modal IDs are not being generated correctly - they're always returning `modal-0` regardless of how many modals I open. Additionally, I'm noticing that the modal settings are being stored with incorrect keys, which causes modals to not receive their proper configuration.

### Reproduction

```js
import { openModal } from '@mantine/modals';

// Open first modal
const firstModalId = openModal({
  title: 'First Modal',
  children: <div>First modal content</div>,
});
console.log(firstModalId); // Expected: modal-0, Actual: modal-0

// Open second modal
const secondModalId = openModal({
  title: 'Second Modal', 
  children: <div>Second modal content</div>,
});
console.log(secondModalId); // Expected: modal-1, Actual: modal-0 (wrong!)

// Both modals have the same ID, causing conflicts
```

### Expected behavior

Each modal should receive a unique ID that increments properly:
- First modal: `modal-0`
- Second modal: `modal-1`
- Third modal: `modal-2`
- etc.

The modal settings should also be stored correctly so that each modal can access its own configuration.

### System Info
- @mantine/modals version: latest
- @mantine/core version: latest
- React version: 18.x

This is blocking our ability to have multiple modals open at the same time. Any help would be appreciated!

---
Repository: /testbed
