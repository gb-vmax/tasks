# Bug Report

### Describe the bug

I'm experiencing an issue where documents are being removed multiple times from the database. When I call `unsafeRemove()` on a document, it seems like the function is executing the removal logic twice - once with the new code path and once with what looks like leftover code at the end of the function.

### Reproduction

```js
const doc = {
  _id: 'test-123',
  type: 'request',
  name: 'Test Request'
};

// Call unsafeRemove
await database.unsafeRemove(doc);

// The document gets removed but I'm seeing duplicate removal notifications
// and the function seems to be executing removal code twice
```

### Expected behavior

The document should be removed once, with a single notification event. The function should not execute duplicate removal logic.

### Additional context

Looking at the code, it appears there might be some duplicate code or incomplete refactoring in the `unsafeRemove` function. The removal logic at the end of the function seems to be executing even when it shouldn't.

This is causing issues with our sync logic as we're getting multiple removal events for the same document.

---
Repository: /testbed
