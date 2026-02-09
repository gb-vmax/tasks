# Bug Report

### Describe the bug

When checking if a modal is open using the `isOpen()` method, the returned value doesn't behave as expected in conditional statements. The method now returns an object instead of a simple boolean, which breaks existing code that relies on truthiness checks.

### Reproduction

```js
const modalRef = useRef();

// Later in code...
if (modalRef.current.isOpen()) {
  // This condition doesn't work as expected anymore
  doSomething();
}

// Also breaks in comparisons
const isModalOpen = modalRef.current.isOpen() === true; // Returns false even when modal is open
```

### Expected behavior

The `isOpen()` method should return a simple boolean value (`true` or `false`) that can be used directly in conditional statements and comparisons. Previously this worked fine, but now the return value seems to be an object which always evaluates to truthy even when the modal is closed.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
