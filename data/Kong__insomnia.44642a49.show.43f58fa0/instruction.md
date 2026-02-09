# Bug Report

### Describe the bug

After a recent update, the error modal component is throwing a syntax error and failing to render. The application crashes when trying to display error dialogs.

### Reproduction

```js
// Trigger any error that would show the error modal
// For example, an API request failure or validation error
try {
  throw new Error('Test error');
} catch (error) {
  errorModal.show({
    title: 'Something went wrong',
    error: error
  });
}
```

The error modal component fails to initialize and the app becomes unresponsive.

### Expected behavior

The error modal should display properly with the error message and allow users to dismiss it. The component should initialize without syntax errors.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
