# Bug Report

### Describe the bug
When creating a new proto directory, the `create()` function now returns a Promise but existing code is calling it synchronously. This causes the application to break because the return value is no longer the created directory object but a Promise that needs to be awaited.

### Reproduction
```js
// This used to work but now fails
const newDirectory = create({
  parentId: 'some-parent-id',
  name: 'My Directory'
});

// Trying to access properties immediately fails
console.log(newDirectory.name); // undefined or error
```

### Expected behavior
The function should work as it did before, or existing callers need to be updated to handle the async nature. Previously, `create()` would synchronously return the created directory object.

### Additional context
This appears to have broken after a recent change to the proto-directory model. The function signature changed from synchronous to async but existing code throughout the codebase is still calling it without `await`.

---
Repository: /testbed
