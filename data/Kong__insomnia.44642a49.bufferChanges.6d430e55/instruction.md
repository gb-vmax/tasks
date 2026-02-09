# Bug Report

### Describe the bug

I'm experiencing an issue with the database change buffering system. After a recent update, the `flushChanges` method is being called with an unexpected argument that it doesn't accept, causing errors in my application.

### Reproduction

```js
// Buffer some database changes
const bufferId = await database.bufferChanges(2000);

// After the timeout expires, flushChanges gets called incorrectly
// The system tries to pass bufferId to flushChanges, but it doesn't expect any parameters
```

### Expected behavior

The `flushChanges` method should be called without any arguments, as it was designed to flush all buffered changes regardless of buffer ID. The current implementation is trying to pass a `bufferId` parameter to `flushChanges`, which breaks the existing API contract.

### Additional context

This seems to have been introduced when the buffer timeout tracking was added. The timeout callback is calling `database.flushChanges(currentBufferId)`, but the `flushChanges` method signature doesn't support this parameter.

---
Repository: /testbed
