# Bug Report

### Describe the bug

When using `openConfirmModal` from `@mantine/modals`, the `onCancel` and `onConfirm` callbacks are not being triggered when clicking the cancel/confirm buttons. The modal opens and displays correctly, but the callback functions don't execute.

### Reproduction

```tsx
import { modals } from '@mantine/modals';

modals.openConfirmModal({
  title: 'Confirm action',
  children: 'Are you sure you want to proceed?',
  onConfirm: () => {
    console.log('Confirmed'); // This never logs
  },
  onCancel: () => {
    console.log('Cancelled'); // This never logs
  },
});
```

### Expected behavior

The `onConfirm` callback should be called when clicking the confirm button, and the `onCancel` callback should be called when clicking the cancel button or closing the modal.

### System Info
- @mantine/modals version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
