# Bug Report

### Describe the bug

The `isOpen()` method on Modal components is returning an object instead of a boolean value, which breaks conditional checks and boolean operations throughout the codebase.

### Reproduction

```js
const modalRef = useRef();

// Later in code...
if (modalRef.current.isOpen()) {
  // This condition now fails because isOpen() returns an object
  // Expected: boolean true/false
  // Actual: object with valueOf, toString, open, openedAt, duration properties
}

// Also breaks negation checks
if (!modalRef.current.isOpen()) {
  // This always evaluates to false since objects are truthy
}
```

### Expected behavior

`isOpen()` should return a boolean value (`true` or `false`) indicating whether the modal is currently open, not an object. This is breaking existing code that relies on boolean checks.

### Additional context

This appears to have changed recently. The method used to return a simple boolean but now returns an object with multiple properties. While the object has `valueOf()` and `toString()` methods, it still breaks strict equality checks and negation operations.

---
Repository: /testbed
