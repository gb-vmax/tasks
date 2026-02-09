# Bug Report

### Describe the bug
The error modal is not displaying when the same error occurs multiple times within a short time window. After the recent update, duplicate errors are being suppressed and won't show up even if they're legitimate errors that users need to see.

### Reproduction
```js
// Show an error
errorModal.show({
  title: 'Network Error',
  message: 'Failed to connect to server'
});

// Try to show the same error again immediately
errorModal.show({
  title: 'Network Error',
  message: 'Failed to connect to server'
});

// The second error modal doesn't appear
```

### Expected behavior
Each error should be displayed to the user, even if it's the same error occurring multiple times. The modal should show every time `show()` is called, allowing users to see that multiple errors are happening.

### Additional context
This seems to be happening with any error that has the same title and message. If I trigger the same API error twice in a row, only the first one shows up. The second call to `show()` appears to be ignored.

---
Repository: /testbed
