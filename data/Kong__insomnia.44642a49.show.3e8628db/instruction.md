# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with modal dialogs appearing multiple times or getting stuck. When trying to show a modal, sometimes it doesn't appear at all, or multiple modals get queued up and appear one after another even though I only called `show()` once.

### Reproduction

```js
// Try showing a modal
askModal.show({
  title: 'Confirm Action',
  message: 'Are you sure?',
  onDone: async (success) => {
    if (success) {
      // perform action
    }
  }
});

// The modal either doesn't show up, or if I call it multiple times quickly,
// they all get queued and show up sequentially
```

### Expected behavior

The modal should show immediately when `show()` is called. If a modal is already visible and `show()` is called again, the behavior should be predictable - either replace the current modal or ignore the new request, but not queue them up indefinitely.

### Additional context

This seems to have started happening after some changes to the AskModal component. The modal behavior was working fine before - it would just show the modal when requested without any queueing or debouncing logic interfering with the display.

---
Repository: /testbed
