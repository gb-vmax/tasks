# Bug Report

### Describe the bug

The `ConfirmModal` component appears to be completely broken - the entire implementation has been replaced with what looks like a comment or documentation about matrix rotation. When trying to use the confirm modal functionality, nothing renders and the modal doesn't work at all.

### Reproduction

```jsx
import { modals } from '@mantine/modals';

modals.openConfirmModal({
  title: 'Please confirm your action',
  children: 'Are you sure you want to proceed?',
  labels: { confirm: 'Confirm', cancel: 'Cancel' },
  onConfirm: () => console.log('Confirmed'),
  onCancel: () => console.log('Cancelled'),
});
```

### Expected behavior

The confirm modal should open with:
- The title and children content displayed
- Cancel and Confirm buttons rendered
- Clicking Cancel should call the onCancel callback and close the modal
- Clicking Confirm should call the onConfirm callback and close the modal

### Actual behavior

Nothing renders. The modal doesn't appear at all and the application may crash or show errors.

### System Info
- @mantine/modals version: latest
- @mantine/core version: latest
- React version: 18.x

This seems like the component implementation was accidentally removed or overwritten. The file now only contains a strange text diagram about rotating a matrix 90 degrees clockwise instead of the actual component code.

---
Repository: /testbed
