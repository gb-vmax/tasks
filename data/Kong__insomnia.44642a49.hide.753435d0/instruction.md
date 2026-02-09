# Bug Report

### Describe the bug

I'm experiencing an issue with the AlertModal component where the `onCancel` callback is being triggered unexpectedly when hiding the modal. It seems like closing the modal through any means (including confirming) might be triggering the cancel callback when it shouldn't.

### Reproduction

```jsx
const modalRef = useRef();

// Show alert with cancel callback
modalRef.current?.show({
  title: 'Confirm Action',
  message: 'Are you sure?',
  addCancel: true,
  onConfirm: () => {
    console.log('Confirmed!');
  },
  onCancel: () => {
    console.log('Cancelled!');
  }
});

// Later, hide the modal
modalRef.current?.hide();
// Expected: onCancel should be called
// Actual: onCancel is called even when confirming
```

### Expected behavior

The `onCancel` callback should only be triggered when the user explicitly cancels the action (e.g., clicking the cancel button or closing the modal without confirming). When the modal is hidden after confirmation, the `onCancel` callback should not be invoked.

### Additional context

This appears to have started happening recently. The modal's hide method doesn't seem to distinguish between different ways of closing, so the cancel callback fires regardless of whether the user confirmed or cancelled.

---
Repository: /testbed
