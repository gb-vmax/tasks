# Bug Report

### Describe the bug

When closing the AskModal without making a choice (e.g., by pressing ESC or clicking outside), the modal doesn't properly notify the callback that the user dismissed it. The `onDone` callback is never triggered, leaving the application in an uncertain state about whether the user confirmed or cancelled the action.

### Reproduction

```js
// Open the AskModal
askModalRef.current?.show({
  title: 'Delete Item',
  message: 'Are you sure you want to delete this?',
  onDone: (confirmed) => {
    console.log('User choice:', confirmed);
    // This never gets called if modal is dismissed
  }
});

// Then dismiss the modal without clicking Yes or No
// (press ESC key or click outside)
// Expected: onDone(false) should be called
// Actual: onDone is never called
```

### Expected behavior

When the modal is dismissed without the user explicitly clicking "Yes" or "No", the `onDone` callback should be invoked with `false` to indicate the action was cancelled. This allows the application to properly handle the dismissal case.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
