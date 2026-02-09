# Bug Report

### Describe the bug

I'm experiencing an issue with the prompt modal after a recent update. When trying to use the modal, I'm getting a `TypeError` about `currentResolver` being null. The modal appears to be trying to call `currentResolver(undefined)` after it's already been set to null, which causes the application to crash.

### Reproduction

```js
// Open the prompt modal
const result = await promptModal.show({
  title: 'Confirm',
  message: 'Are you sure?'
});

// Then close it
promptModal.hide();
```

The error occurs when `hide()` is called. It looks like there's a logic issue where `currentResolver` is set to `null` and then immediately called on the next line.

### Expected behavior

The modal should close gracefully without throwing errors. The promise should resolve properly when the modal is dismissed.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
