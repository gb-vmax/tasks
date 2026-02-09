# Bug Report

### Describe the bug

I'm experiencing an issue with modal state checking after a recent update. When checking if a modal is open using `isOpen()`, the behavior has changed and is causing problems with conditional logic in my code.

Previously, `isOpen()` returned a simple boolean value, but now it seems to return an object (or null) instead. This breaks existing code that relies on boolean checks.

### Reproduction

```js
const modalRef = useRef();

// Later in code...
if (modalRef.current.isOpen()) {
  // This condition now behaves differently
  console.log('Modal is open');
}

// This also breaks:
const isModalOpen = modalRef.current.isOpen();
if (!isModalOpen) {
  // Expected to enter here when modal is closed
  // But doesn't work as expected anymore
}
```

### Expected behavior

`isOpen()` should return a boolean value (true/false) that can be used directly in conditional statements. The current implementation returns an object when open and null when closed, which breaks existing boolean logic.

### Additional context

This appears to have changed recently. Code that was working fine before now fails because:
- Checking `!isOpen()` when the modal is closed returns `!null` which is `true`
- The return value can't be used directly in boolean contexts without additional checks

Would appreciate if this could return a simple boolean like before, or at least maintain backward compatibility.

---
Repository: /testbed
