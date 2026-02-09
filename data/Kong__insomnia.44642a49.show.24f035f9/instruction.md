# Bug Report

### Describe the bug
The error modal is not showing up when trying to display error messages. After a recent update, calling the error modal's `show` method doesn't seem to do anything - the modal just doesn't appear on screen.

### Reproduction
```js
// Trying to show an error modal
errorModalRef.current?.show({
  title: 'Request Failed',
  message: 'Something went wrong',
  error: new Error('Network error')
});

// Modal doesn't appear
```

Also noticed that when trying to show the same error multiple times (like in a retry scenario), only the first one shows up but subsequent ones are silently ignored.

### Expected behavior
The error modal should display whenever `show()` is called with valid options. If I call it multiple times with the same error, it should still show each time (or at least have predictable behavior).

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
