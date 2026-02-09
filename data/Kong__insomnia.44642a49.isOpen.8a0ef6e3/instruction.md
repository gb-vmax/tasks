# Bug Report

### Describe the bug

The modal's `isOpen()` method is returning an object instead of a boolean value, which breaks code that expects a simple true/false check. This causes conditional logic and comparisons to fail unexpectedly.

### Reproduction

```js
const modalRef = useRef();

// Later in code...
if (modalRef.current.isOpen()) {
  // This condition doesn't work as expected anymore
  console.log('Modal is open');
}

// Direct boolean checks also fail
const isModalOpen = modalRef.current.isOpen();
console.log(typeof isModalOpen); // Expected: 'boolean', Actual: 'object'

// Comparisons break
if (modalRef.current.isOpen() === true) {
  // Never executes even when modal is open
}
```

### Expected behavior

`isOpen()` should return a simple boolean value (`true` or `false`) that can be used directly in conditional statements and boolean comparisons.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started recently. The method used to work fine for checking modal state in our custom modal management code.

---
Repository: /testbed
