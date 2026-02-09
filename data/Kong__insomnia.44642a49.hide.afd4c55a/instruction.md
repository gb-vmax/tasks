# Bug Report

### Describe the bug

The `AskModal` component's `hide()` method is calling the `onDone` callback multiple times when the modal is closed. This causes duplicate callback executions which can lead to unexpected behavior in the application.

### Reproduction

```js
const modalRef = useRef();

// Show the modal with an onDone callback
modalRef.current?.show({
  title: 'Confirm Action',
  message: 'Are you sure?',
  onDone: async (success) => {
    console.log('Callback executed:', success);
    // This gets called multiple times
  }
});

// Later, hide the modal
modalRef.current?.hide();
```

### Expected behavior

The `onDone` callback should only be invoked once when the modal is closed, not multiple times. Each callback execution should happen exactly once regardless of how the modal is dismissed.

### Additional context

This appears to be related to how the callback tracking is implemented. The callback gets invoked but the tracking mechanism doesn't properly prevent subsequent calls in all cases.

---
Repository: /testbed
