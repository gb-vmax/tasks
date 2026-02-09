# Bug Report

### Modal `isOpen()` method returning unexpected object instead of boolean

I'm experiencing an issue with the modal component where the `isOpen()` method is returning an object instead of a simple boolean value. This is breaking conditional checks in my code.

### Reproduction

```js
const modalRef = useRef();

// Later in code...
if (modalRef.current.isOpen()) {
  // This condition now behaves unexpectedly
  console.log('Modal is open');
}

// Also breaks strict equality checks
const isModalOpen = modalRef.current.isOpen();
console.log(isModalOpen === true); // Returns false even when modal is open
console.log(typeof isModalOpen); // Returns 'object' instead of 'boolean'
```

### Expected behavior

The `isOpen()` method should return a simple boolean value (`true` or `false`) that can be used in standard conditional checks and comparisons. Previously this worked fine with direct boolean comparisons.

### Additional context

This seems to have changed recently. The method now returns some kind of complex object when the modal is open, which breaks existing code that expects a boolean return value. While the object might be truthy, it fails strict equality checks and type comparisons.

---
Repository: /testbed
