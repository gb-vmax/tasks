# Bug Report

### Describe the bug

The Clear action in the prompt template tag is broken. When clicking the Clear button, nothing happens and the stored values remain in place. The button appears to do nothing at all.

### Reproduction

1. Use a prompt template tag with stored values
2. Click the "Clear" action button
3. The stored data is not cleared

Example:
```js
// Set up a prompt with storage
{% prompt "Test", "Enter value", "", "my-storage-key" %}

// Try to clear using the Clear action
// Expected: storage should be cleared
// Actual: nothing happens, values remain stored
```

### Expected behavior

The Clear action should remove all stored prompt values when clicked. Previously this was working fine but now the button doesn't seem to do anything.

### Additional context

This appears to have started happening recently. The Clear button is visible in the actions menu but clicking it has no effect on the stored data.

---
Repository: /testbed
