# Bug Report

### Describe the bug

The error modal component is not displaying correctly after a recent change. When trying to show an error modal, the application crashes or the modal doesn't appear at all.

### Reproduction

```js
// Try to show an error modal
errorModalRef.current?.show({
  title: 'Error',
  message: 'Something went wrong',
  error: new Error('Test error')
});
```

The modal fails to render and the component seems to be broken.

### Expected behavior

The error modal should display properly with the provided title, message, and error details. It should show up on screen without any issues.

### Additional context

This appears to have started happening recently. The modal was working fine before but now it's completely broken. Looking at the code, it seems like there might be a syntax or structural issue in the component definition that's preventing it from working correctly.

---
Repository: /testbed
