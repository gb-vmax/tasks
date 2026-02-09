# Bug Report

### Describe the bug

The `bufferChanges()` function is not working as expected after a recent update. When I call it with the default parameters, it seems to trigger a flush immediately or behaves inconsistently. The buffering behavior that was working before is now broken.

### Reproduction

```js
// This used to work fine
const bufferId = await database.bufferChanges(1000);

// Make some changes
await database.update(doc1);
await database.update(doc2);

// Changes seem to flush immediately instead of waiting
```

### Expected behavior

The function should buffer changes for the specified time period (1000ms in this case) before flushing. The changes should accumulate during this time and then be written together when the timer expires.

### Additional context

This was working correctly before the latest changes. Now it seems like the function signature or behavior has changed in a way that breaks existing code that doesn't pass the new parameters.

---
Repository: /testbed
