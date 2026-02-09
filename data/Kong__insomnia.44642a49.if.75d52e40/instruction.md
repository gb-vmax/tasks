# Bug Report

### Describe the bug

The `duplicate()` function in `request-operations.ts` is now returning a Promise instead of a synchronous value for WebSocket requests, but the function signature hasn't been updated to reflect this. This causes issues when calling code expects a synchronous return value.

### Reproduction

```js
// This code used to work synchronously
const duplicatedRequest = duplicate(webSocketRequest, { name: 'New Name' });

// Now it returns a Promise, but the function signature doesn't indicate this
// So the calling code breaks when trying to access properties directly
console.log(duplicatedRequest.name); // undefined (it's actually a Promise)
```

### Expected behavior

The `duplicate()` function should either:
1. Return a synchronous value like before, OR
2. Have its signature updated to `async` and return `Promise<T>` so calling code knows to await it

Currently it's returning a Promise for WebSocket requests but the function is not marked as `async`, which creates a mismatch between the function signature and actual behavior.

### System Info
- Insomnia version: latest
- Affected model: WebSocket requests

---
Repository: /testbed
