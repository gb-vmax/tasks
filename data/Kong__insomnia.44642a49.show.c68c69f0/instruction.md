# Bug Report

### Describe the bug
The prompt modal is not displaying correctly after a recent update. When calling `show()` on the modal, it doesn't appear or behaves unexpectedly. The modal seems to be having issues with its state management.

### Reproduction
```js
// Try to show a prompt modal with options
promptModalRef.current?.show({
  title: 'Enter value',
  defaultValue: 'test',
  submitName: 'OK',
  onComplete: (value) => console.log(value)
});

// Modal either doesn't show or shows with incorrect state
```

### Expected behavior
The modal should display properly with the provided options. The title, default value, and other properties should be set correctly when the modal is shown.

### Additional context
This appears to have broken after some changes to the modal's state handling. The modal worked fine in previous versions but now has issues when trying to display it with configuration options.

---
Repository: /testbed
