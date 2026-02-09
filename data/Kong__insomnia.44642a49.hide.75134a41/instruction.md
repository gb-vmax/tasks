# Bug Report

### Describe the bug

When dismissing an alert modal using the `hide()` method, the `onCancel` callback is being triggered even when it shouldn't be. This causes unexpected behavior when programmatically closing modals.

### Reproduction

```js
const alertModalRef = useRef();

// Show alert with callbacks
alertModalRef.current?.show({
  title: 'Confirm Action',
  message: 'Are you sure?',
  addCancel: true,
  onConfirm: () => {
    console.log('Confirmed');
  },
  onCancel: () => {
    console.log('Cancelled');
  }
});

// Later, programmatically hide the modal
alertModalRef.current?.hide();

// Expected: No callback should fire
// Actual: onCancel gets called
```

### Expected behavior

When calling `hide()` directly, no callbacks should be triggered. The `onCancel` callback should only fire when the user explicitly clicks the cancel button, not when the modal is programmatically dismissed.

### Additional context

This is particularly problematic when you need to close the modal from external logic (like after a successful API call) without triggering the cancel behavior.

---
Repository: /testbed
