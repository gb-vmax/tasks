# Bug Report

### Describe the bug

The alert modal is not showing up when calling the `show()` method. After a recent update, the modal appears to be completely broken - nothing happens when I try to display an alert dialog.

### Reproduction

```js
alertModalRef.current?.show({
  title: 'Error',
  message: 'Something went wrong',
  okLabel: 'OK'
});
```

When this code runs, the modal doesn't appear at all. The application doesn't crash but the user never sees the alert.

### Expected behavior

The modal should display with the title "Error", message "Something went wrong", and an OK button. The modal should be visible to the user and allow them to dismiss it by clicking the button.

### Additional context

This was working fine before the latest changes. It seems like the modal initialization or display logic might have been affected. The `show()` method is being called correctly but nothing renders on screen.

---
Repository: /testbed
