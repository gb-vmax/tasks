# Bug Report

### Describe the bug

After a recent update, request updates are failing with unexpected behavior. When trying to update a request object with a partial patch, the function seems to hang or not complete properly. The update operation doesn't return as expected.

### Reproduction

```js
const request = {
  _id: 'req_123',
  name: 'My Request',
  url: 'https://example.com'
};

const patch = {
  name: 'Updated Request'
};

// This call doesn't complete properly
await update(request, patch);
```

### Expected behavior

The `update()` function should apply the patch to the request object and return the updated request. The operation should complete successfully without hanging.

### Additional context

This seems to have started happening after some changes to the request-operations.ts file. The update function appears to have some logic issues that prevent it from executing correctly. Regular HTTP requests, gRPC requests, and WebSocket requests are all affected.

---
Repository: /testbed
