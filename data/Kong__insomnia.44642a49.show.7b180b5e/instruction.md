# Bug Report

### Describe the bug

The prompt modal is not displaying correctly after recent changes. When opening the modal with hints, the behavior seems off - hints appear to be accumulating or merging unexpectedly across multiple modal invocations instead of showing only the hints passed in the current call.

### Reproduction

```js
// First modal invocation
promptModal.show({
  title: 'Enter name',
  hints: ['John', 'Jane', 'Bob']
});

// Close modal and open again with different hints
promptModal.show({
  title: 'Enter email',
  hints: ['test@example.com', 'user@example.com']
});

// Expected: Only 2 hints shown
// Actual: Previous hints from first invocation are still present
```

### Expected behavior

Each time the modal is opened with a new set of hints, only those hints should be displayed. Previous hints from earlier modal invocations should not carry over or merge with the new hints.

### Additional context

This appears to be affecting the modal's hint functionality. The hints seem to persist or merge between different modal calls, which makes the autocomplete suggestions confusing for users.

---
Repository: /testbed
