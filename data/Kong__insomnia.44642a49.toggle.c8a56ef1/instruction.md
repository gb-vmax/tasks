# Bug Report

### Describe the bug
The `toggle()` method on Modal components is not working as expected after a recent update. When calling `toggle()` without any arguments, the modal fails to open/close properly.

### Reproduction
```js
const modalRef = useRef();

// This no longer works
modalRef.current?.toggle();

// Modal doesn't respond to toggle calls
```

The toggle functionality was working fine in the previous version, but after updating it seems like the method signature changed and now requires parameters even for basic toggle operations.

### Expected behavior
Calling `toggle()` without any arguments should simply toggle the modal's visibility state - opening it if closed, closing it if open. The method should work with or without optional parameters.

### System Info
- Insomnia version: latest
- Component: base/modal.tsx

---
Repository: /testbed
