# Bug Report

### Describe the bug
When trying to show the AlertModal in quick succession, the modal doesn't respond to subsequent `show()` calls. It seems like there's some kind of blocking mechanism that prevents the modal from being opened multiple times rapidly.

### Reproduction
```js
// Try to show the alert modal twice in a row
alertModalRef.current?.show({
  title: 'First Alert',
  message: 'This is the first message',
  onConfirm: () => console.log('First confirmed')
});

// This call is ignored/blocked
alertModalRef.current?.show({
  title: 'Second Alert', 
  message: 'This is the second message',
  onConfirm: () => console.log('Second confirmed')
});
```

### Expected behavior
The second `show()` call should either:
- Queue and display after the first modal is closed, OR
- Replace the first modal with the second one immediately

Instead, the second call appears to be silently ignored and nothing happens.

### Additional context
This is causing issues in our workflow where users might trigger multiple alerts quickly (e.g., validation errors from multiple fields). The first alert shows but subsequent ones are lost.

---
Repository: /testbed
