# Bug Report

### Describe the bug

The plugin prompt dialog is not closing properly when the user cancels or dismisses it. After the recent changes, the modal remains open and the promise never resolves/rejects as expected.

### Reproduction

```js
// In a plugin context
await app.prompt('Enter value', {
  label: 'Input',
  defaultValue: 'test'
});

// Steps:
// 1. Open the prompt dialog
// 2. Click the cancel button or press ESC
// 3. The modal stays open and the promise hangs
```

### Expected behavior

When the user cancels the prompt (by clicking cancel, pressing ESC, or clicking outside), the modal should close immediately and the promise should be rejected with an error message like `Prompt <title> cancelled`.

### Additional context

This seems to have started happening recently. The promise just hangs indefinitely when trying to cancel the prompt, and the UI becomes unresponsive. The `onHide` callback doesn't seem to be working correctly anymore.

---
Repository: /testbed
